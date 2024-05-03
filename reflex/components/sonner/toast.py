"""Sonner toast component."""

from __future__ import annotations

from typing import Any, Literal, Optional

from reflex.base import Base
from reflex.components.component import Component, ComponentNamespace
from reflex.components.lucide.icon import Icon
from reflex.event import (
    EventHandler,
    EventSpec,
    call_event_fn,
    call_event_handler,
    call_script,
)
from reflex.style import Style, color_mode
from reflex.utils import format
from reflex.utils.imports import ImportVar
from reflex.utils.serializers import serialize, serializer
from reflex.vars import Var, VarData

LiteralPosition = Literal[
    "top-left",
    "top-center",
    "top-right",
    "bottom-left",
    "bottom-center",
    "bottom-right",
]


toast_ref = Var.create_safe("refs['__toast']")


class ToastAction(Base):
    """A toast action that render a button in the toast."""

    label: str
    on_click: Any


@serializer
def serialize_action(action: ToastAction) -> dict:
    """Serialize a toast action.

    Args:
        action: The toast action to serialize.

    Returns:
        The serialized toast action with on_click formatted to queue the given event.
    """
    if action.on_click is not None:
        events = []
        on_click_specs = action.on_click
        if not isinstance(on_click_specs, list):
            on_click_specs = [on_click_specs]
        for spec in on_click_specs:
            if isinstance(spec, EventHandler):
                specs = [call_event_handler(spec, lambda: [])]
            elif isinstance(spec, type(lambda: None)):
                specs = call_event_fn(spec, lambda: [])
            else:
                specs = [spec]
            events.extend(format.format_event(s) for s in specs)
        on_click = Var.create(
            f"() => {{queueEvents([{','.join(events)}], socket); processEvent(socket)}}",
            _var_is_string=False,
            _var_is_local=False,
        )
    else:
        on_click = Var.create("() => null", _var_is_string=False, _var_is_local=False)

    return {
        "label": action.label,
        "onClick": on_click,
    }


class PropsBase(Base):
    """Base class for all props classes."""

    def json(self) -> str:
        """Convert the object to a json string.

        Returns:
            The object as a json string.
        """
        from reflex.utils.serializers import serialize

        return format.unwrap_vars(
            self.__config__.json_dumps(
                {
                    format.to_camel_case(key): value
                    for key, value in self.dict().items()
                },
                default=serialize,
            )
        )


class ToastProps(PropsBase):
    """Props for the toast component."""

    # Toast's description, renders underneath the title.
    description: Optional[str]

    # Whether to show the close button.
    close_button: Optional[bool]

    # Dark toast in light mode and vice versa.
    invert: Optional[bool]

    # Control the sensitivity of the toast for screen readers
    important: Optional[bool]

    # Time in milliseconds that should elapse before automatically closing the toast.
    duration: Optional[int]

    # Position of the toast.
    position: Optional[LiteralPosition]

    # If false, it'll prevent the user from dismissing the toast.
    dismissible: Optional[bool]

    # TODO: fix serialization of icons for toast? (might not be possible yet)
    # Icon displayed in front of toast's text, aligned vertically.
    # icon: Optional[Icon] = None

    # TODO: fix implementation for action / cancel buttons
    # Renders a primary button, clicking it will close the toast.
    action: Optional[ToastAction]

    # Renders a secondary button, clicking it will close the toast.
    cancel: Optional[ToastAction]

    # Custom id for the toast.
    id: Optional[str]

    # Removes the default styling, which allows for easier customization.
    unstyled: Optional[bool]

    # Custom style for the toast.
    style: Optional[Style]

    # XXX: These still do not seem to work
    # Custom style for the toast primary button.
    action_button_styles: Optional[Style]

    # Custom style for the toast secondary button.
    cancel_button_styles: Optional[Style]

    def dict(self, *args, **kwargs) -> dict:
        """Convert the object to a dictionary.

        Args:
            *args: The arguments to pass to the base class.
            **kwargs: The keyword arguments to pass to the base

        Returns:
            The object as a dictionary with ToastAction fields intact.
        """
        kwargs.setdefault("exclude_none", True)
        d = super().dict(*args, **kwargs)
        # Keep these fields as ToastAction so they can be serialized specially
        if d.get("action") is not None:
            d["action"] = self.action
            if isinstance(self.action, dict):
                d["action"] = ToastAction(**self.action)
        if d.get("cancel") is not None:
            d["cancel"] = self.cancel
            if isinstance(self.cancel, dict):
                d["cancel"] = ToastAction(**self.cancel)
        return d


class Toaster(Component):
    """A Toaster Component for displaying toast notifications."""

    library = "sonner@1.4.41"

    tag = "Toaster"

    # the theme of the toast
    theme: Var[str] = color_mode

    # whether to show rich colors
    rich_colors: Var[bool] = Var.create_safe(True)

    # whether to expand the toast
    expand: Var[bool] = Var.create_safe(True)

    # the number of toasts that are currently visible
    visible_toasts: Var[int]

    # the position of the toast
    position: Var[LiteralPosition] = Var.create_safe("bottom-right")

    # whether to show the close button
    close_button: Var[bool] = Var.create_safe(False)

    # offset of the toast
    offset: Var[str]

    # directionality of the toast (default: ltr)
    dir: Var[str]

    # Keyboard shortcut that will move focus to the toaster area.
    hotkey: Var[str]

    # Dark toasts in light mode and vice versa.
    invert: Var[bool]

    # These will act as default options for all toasts. See toast() for all available options.
    toast_options: Var[ToastProps]

    # Gap between toasts when expanded
    gap: Var[int]

    # Changes the default loading icon
    loading_icon: Var[Icon]

    # Pauses toast timers when the page is hidden, e.g., when the tab is backgrounded, the browser is minimized, or the OS is locked.
    pause_when_page_is_hidden: Var[bool]

    def _get_hooks(self) -> Var[str]:
        hook = Var.create_safe(f"{toast_ref} = toast", _var_is_local=True)
        hook._var_data = VarData(  # type: ignore
            imports={
                "/utils/state": [ImportVar(tag="refs")],
                self.library: [ImportVar(tag="toast", install=False)],
            }
        )
        return hook

    @staticmethod
    def send_toast(message: str, level: str | None = None, **props) -> EventSpec:
        """Send a toast message.

        Args:
            message: The message to display.
            level: The level of the toast.
            **props: The options for the toast.

        Returns:
            The toast event.
        """
        toast_command = f"{toast_ref}.{level}" if level is not None else toast_ref
        if props:
            args = serialize(ToastProps(**props))
            toast = f"{toast_command}(`{message}`, {args})"
        else:
            toast = f"{toast_command}(`{message}`)"

        toast_action = Var.create(toast, _var_is_string=False, _var_is_local=True)
        return call_script(toast_action)  # type: ignore

    @staticmethod
    def toast_info(message: str, **kwargs):
        """Display an info toast message.

        Args:
            message: The message to display.
            kwargs: Additional toast props.

        Returns:
            The toast event.
        """
        return Toaster.send_toast(message, level="info", **kwargs)

    @staticmethod
    def toast_warning(message: str, **kwargs):
        """Display a warning toast message.

        Args:
            message: The message to display.
            kwargs: Additional toast props.

        Returns:
            The toast event.
        """
        return Toaster.send_toast(message, level="warning", **kwargs)

    @staticmethod
    def toast_error(message: str, **kwargs):
        """Display an error toast message.

        Args:
            message: The message to display.
            kwargs: Additional toast props.

        Returns:
            The toast event.
        """
        return Toaster.send_toast(message, level="error", **kwargs)

    @staticmethod
    def toast_success(message: str, **kwargs):
        """Display a success toast message.

        Args:
            message: The message to display.
            kwargs: Additional toast props.

        Returns:
            The toast event.
        """
        return Toaster.send_toast(message, level="success", **kwargs)

    def toast_dismiss(self, id: str | None):
        """Dismiss a toast.

        Args:
            id: The id of the toast to dismiss.

        Returns:
            The toast dismiss event.
        """
        if id is None:
            dismiss = f"{toast_ref}.dismiss()"
        else:
            dismiss = f"{toast_ref}.dismiss({id})"
        dismiss_action = Var.create(dismiss, _var_is_string=False, _var_is_local=True)
        return call_script(dismiss_action)  # type: ignore


# TODO: figure out why loading toast stay open forever
# def toast_loading(message: str, **kwargs):
#     return _toast(message, level="loading", **kwargs)


class ToastNamespace(ComponentNamespace):
    """Namespace for toast components."""

    provider = staticmethod(Toaster.create)
    options = staticmethod(ToastProps)
    info = staticmethod(Toaster.toast_info)
    warning = staticmethod(Toaster.toast_warning)
    error = staticmethod(Toaster.toast_error)
    success = staticmethod(Toaster.toast_success)
    dismiss = staticmethod(Toaster.toast_dismiss)
    # loading = staticmethod(toast_loading)
    __call__ = staticmethod(Toaster.send_toast)


toast = ToastNamespace()
