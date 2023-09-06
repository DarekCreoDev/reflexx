"""Stub file for accordion.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Optional, List, Union, overload
from reflex.components.component import Component
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class Accordion(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, items, icon_pos, allow_multiple: Optional[Union[Var[bool], bool]] = None, allow_toggle: Optional[Union[Var[bool], bool]] = None, default_index: Optional[Union[Var[Optional[List[int]]], Optional[List[int]]]] = None, index: Optional[Union[Var[Union[int, List[int]]], Union[int, List[int]]]] = None, reduce_motion: Optional[Union[Var[bool], bool]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Accordion":  # type: ignore
        """Create an accordion component.

        Args:
            children: The children of the component.
            items: The items of the accordion component: list of tuples (label,panel)
            icon_pos: The position of the arrow icon of the accordion. "right", "left" or None
            allow_multiple: The allow_multiple property of the accordion. (True or False)
            allow_toggle: The allow_toggle property of the accordion. (True or False)
            props: The properties of the component.

        Returns:
            The accordion component
        """
        ...

class AccordionItem(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, id_: Optional[Union[Var[str], str]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_focusable: Optional[Union[Var[bool], bool]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "AccordionItem":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            id_: A unique id for the accordion item.
            is_disabled: If true, the accordion item will be disabled.
            is_focusable: If true, the accordion item will be focusable.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class AccordionButton(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "AccordionButton":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class AccordionPanel(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "AccordionPanel":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class AccordionIcon(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "AccordionIcon":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
