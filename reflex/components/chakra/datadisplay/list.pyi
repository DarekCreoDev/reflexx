"""Stub file for reflex/components/chakra/datadisplay/list.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Optional, Union, overload

from reflex.components.chakra import ChakraComponent
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from reflex.vars import BaseVar, Var

class List(ChakraComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        items: Optional[Union[Var[list], list]] = None,
        spacing: Optional[Union[Var[str], str]] = None,
        style_position: Optional[Union[Var[str], str]] = None,
        style_type: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        **props,
    ) -> "List":
        """Create a list component.

        Args:
            *children: The children of the component.
            items: A list of items to add to the list.
            spacing: The space between each list item
            style_position: Shorthand prop for listStylePosition
            style_type: Shorthand prop for listStyleType
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list component.
        """
        ...

class ListItem(ChakraComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        **props,
    ) -> "ListItem":
        """Create the component.

        Args:
            *children: The children of the component.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class OrderedList(List):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        items: Optional[Union[Var[list], list]] = None,
        spacing: Optional[Union[Var[str], str]] = None,
        style_position: Optional[Union[Var[str], str]] = None,
        style_type: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        **props,
    ) -> "OrderedList":
        """Create a list component.

        Args:
            *children: The children of the component.
            items: A list of items to add to the list.
            spacing: The space between each list item
            style_position: Shorthand prop for listStylePosition
            style_type: Shorthand prop for listStyleType
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list component.
        """
        ...

class UnorderedList(List):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        items: Optional[Union[Var[list], list]] = None,
        spacing: Optional[Union[Var[str], str]] = None,
        style_position: Optional[Union[Var[str], str]] = None,
        style_type: Optional[Union[Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        **props,
    ) -> "UnorderedList":
        """Create a list component.

        Args:
            *children: The children of the component.
            items: A list of items to add to the list.
            spacing: The space between each list item
            style_position: Shorthand prop for listStylePosition
            style_type: Shorthand prop for listStyleType
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The list component.
        """
        ...
