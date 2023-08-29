"""Wrapper around react-debounce-input."""

from typing import Any, Dict, Tuple

from reflex.components import Component
from reflex.components.tags import Tag
from reflex.vars import Var


class DebounceInput(Component):
    """The DebounceInput component is used to buffer input events on the client side.

    It is intended to wrap various form controls and should be used whenever a
    fully-controlled input is needed to prevent lost input data when the backend
    is experiencing high latency.
    """

    library = "react-debounce-input"
    tag = "DebounceInput"

    # Minimum input characters before triggering the on_change event
    min_length: Var[int]

    # Time to wait between end of input and triggering on_change
    debounce_timeout: Var[int]

    # If true, notify when Enter key is pressed
    force_notify_by_enter: Var[bool]

    # If true, notify when form control loses focus
    force_notify_on_blur: Var[bool]

    # If provided, create a fully-controlled input
    value: Var[str]

    def _render(self) -> Tag:
        """Carry first child props directly on this tag.

        Since react-debounce-input wants to create and manage the underlying
        input component itself, we carry all props, events, and styles from
        the child, and then neuter the child's render method so it produces no output.

        Returns:
            The rendered debounce element wrapping the first child element.

        Raises:
            RuntimeError: unless exactly one child element is provided.
        """
        child, props = _collect_first_child_and_props(self)
        if isinstance(child, type(self)) or len(self.children) > 1:
            raise RuntimeError(
                "Provide a single child for DebounceInput, such as rx.input() or "
                "rx.text_area()",
            )
        self.children = []
        tag = super()._render()
        tag.add_props(
            **props,
            **child.event_triggers,
            sx=child.style,
            id=child.id,
            class_name=child.class_name,
            element=Var.create("{%s}" % child.tag, is_local=False, is_string=False),
        )
        # do NOT render the child, DebounceInput will create it
        object.__setattr__(child, "render", lambda: "")
        return tag


def props_not_none(c: Component) -> Dict[str, Any]:
    """Get all properties of the component that are not None.

    Args:
        c: the component to get_props from

    Returns:
        dict of all props that are not None.
    """
    cdict = {a: getattr(c, a) for a in c.get_props() if getattr(c, a, None) is not None}
    return cdict


def _collect_first_child_and_props(c: Component) -> Tuple[Component, Dict[str, Any]]:
    """Recursively find the first child of a different type than `c` with props.

    This function is used to collapse nested DebounceInput components by
    applying props from each level. Parent props take precedent over child
    props. The first child component that differs in type will be returned
    along with all combined parent props seen along the way.

    Args:
        c: the component to get_props from

    Returns:
        tuple containing the first nested child of a different type and the collected
        props from each component traversed.
    """
    props = props_not_none(c)
    if not c.children:
        return c, props
    child = c.children[0]
    if not isinstance(child, type(c)):
        return child, {**props_not_none(child), **props}
    # carry props from nested DebounceInput components
    recursive_child, child_props = _collect_first_child_and_props(child)
    return recursive_child, {**child_props, **props}
