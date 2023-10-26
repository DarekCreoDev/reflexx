"""Stub file for reflex/components/typography/heading.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Literal, overload, Dict, Optional, Union, List
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from reflex.components.libs.chakra import ChakraComponent, LiteralHeadingSize
from reflex.vars import Var

class Heading(ChakraComponent):
    ...

    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_: Optional[Union[Var[str], str]] = None,
        size: Optional[
            Union[
                Var[Literal["lg", "md", "sm", "xs", "xl", "2xl", "3xl", "4xl"]],
                Literal["lg", "md", "sm", "xs", "xl", "2xl", "3xl", "4xl"],
            ]
        ] = None,
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
    ) -> "Heading":
        """Create the component.

        Args:
            *children: The children of the component.
            as_: Override the tag. The default tag is `<h2>`.
            size: "4xl" | "3xl" | "2xl" | "xl" | "lg" | "md" | "sm" | "xs"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
