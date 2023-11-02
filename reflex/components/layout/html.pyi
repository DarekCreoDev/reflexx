"""Stub file for reflex/components/layout/html.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Dict, overload, Optional, Literal, Any, Union, List
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any
from reflex.components.layout.box import Box

class Html(Box):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        dangerouslySetInnerHTML: Optional[Any] = None,
        element: Optional[Union[Var[str], str]] = None,
        src: Optional[Union[Var[str], str]] = None,
        alt: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_blur: Optional[
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
    ) -> "Html":
        """Create a html component.

        Args:
            *children: The children of the component.
            dangerouslySetInnerHTML: The HTML to render.
            element: The type element to render. You can specify an image, video, or any other HTML element such as iframe.
            src: The source of the content.
            alt: The alt text of the content.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props to pass to the component.

        Returns:
            The html component.

        Raises:
            ValueError: If children are not provided or more than one child is provided.
        """
        ...
