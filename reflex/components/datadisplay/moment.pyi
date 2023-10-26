"""Stub file for reflex/components/datadisplay/moment.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Literal, overload, Dict, Optional, Union, List, Any
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Dict, List
from reflex.components.component import Component, NoSSRComponent
from reflex.utils import imports
from reflex.vars import ImportVar, Var

class Moment(NoSSRComponent):
    def get_event_triggers(self) -> Dict[str, Any]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        interval: Optional[Union[Var[int], int]] = None,
        format: Optional[Union[Var[str], str]] = None,
        trim: Optional[Union[Var[bool], bool]] = None,
        parse: Optional[Union[Var[str], str]] = None,
        from_now: Optional[Union[Var[bool], bool]] = None,
        from_now_during: Optional[Union[Var[int], int]] = None,
        to_now: Optional[Union[Var[bool], bool]] = None,
        with_title: Optional[Union[Var[bool], bool]] = None,
        title_format: Optional[Union[Var[str], str]] = None,
        diff: Optional[Union[Var[str], str]] = None,
        decimal: Optional[Union[Var[bool], bool]] = None,
        unit: Optional[Union[Var[str], str]] = None,
        duration: Optional[Union[Var[str], str]] = None,
        date: Optional[Union[Var[str], str]] = None,
        duration_from_now: Optional[Union[Var[bool], bool]] = None,
        unix: Optional[Union[Var[bool], bool]] = None,
        local: Optional[Union[Var[bool], bool]] = None,
        tz: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_change: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        **props
    ) -> "Moment":
        """Create a Moment component.

        Args:
            *children: The children of the component.
            interval: How often the date update (how often time update / 0 to disable).
            format: Formats the date according to the given format string.
            trim: When formatting duration time, the largest-magnitude tokens are automatically trimmed when they have no value.
            parse:  Use the parse attribute to tell moment how to parse the given date when non-standard.
            from_now: NOT IMPLEMENTED :  add  substract  Displays the date as the time from now, e.g. "5 minutes ago".
            from_now_during: Setting fromNowDuring will display the relative time as with fromNow but just during its value in milliseconds, after that format will be used instead.
            to_now: Similar to fromNow, but gives the opposite interval.
            with_title: Adds a title attribute to the element with the complete date.
            title_format: How the title date is formatted when using the withTitle attribute.
            diff: Show the different between this date and the rendered child.
            decimal: Display the diff as decimal.
            unit: Display the diff in given unit.
            duration: Shows the duration (elapsed time) between two dates. duration property should be behind date property time-wise.
            date: The date to display (also work if passed as children).
            duration_from_now: Shows the duration (elapsed time) between now and the provided datetime.
            unix: Tells Moment to parse the given date value as a unix timestamp.
            local: Outputs the result in local time.
            tz: Display the date in the given timezone.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The Moment Component.
        """
        ...
