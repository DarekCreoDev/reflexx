"""Stub file for reflex/components/el/elements/metadata.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Union
from reflex.components.el.element import Element
from reflex.vars import Var as Var
from .base import BaseHTML

class Base(BaseHTML):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        href: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        target: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        access_key: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Base":
        """Create the component.

        Args:
            *children: The children of the component.
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
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

class Head(BaseHTML):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        access_key: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Head":
        """Create the component.

        Args:
            *children: The children of the component.
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
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

class Link(BaseHTML):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        cross_origin: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        href: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        href_lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        integrity: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        media: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        referrer_policy: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        rel: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        sizes: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        type: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        access_key: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Link":
        """Create the component.

        Args:
            *children: The children of the component.
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
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

class Meta(BaseHTML):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        char_set: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        content: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        http_equiv: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        name: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        access_key: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Meta":
        """Create the component.

        Args:
            *children: The children of the component.
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
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

class Title(Element):
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
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "Title":
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

class StyleEl(Element):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        media: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "StyleEl":
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

base = Base.create
head = Head.create
link = Link.create
meta = Meta.create
title = Title.create
style = StyleEl.create
