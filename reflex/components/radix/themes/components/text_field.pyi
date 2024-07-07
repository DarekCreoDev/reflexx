"""Stub file for reflex/components/radix/themes/components/text_field.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Callable, Dict, Literal, Optional, Union, overload

from reflex.components.component import Component, ComponentNamespace
from reflex.components.core.breakpoints import Breakpoints
from reflex.components.el import elements
from reflex.event import EventHandler, EventSpec
from reflex.style import Style
from reflex.vars import BaseVar, Var

from ..base import RadixThemesComponent

LiteralTextFieldSize = Literal["1", "2", "3"]
LiteralTextFieldVariant = Literal["classic", "surface", "soft"]

class TextFieldRoot(elements.Div, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        size: Optional[
            Union[
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3"]], Literal["1", "2", "3"]
                    ]
                ],
                Literal["1", "2", "3"],
                Breakpoints[str, Literal["1", "2", "3"]],
            ]
        ] = None,
        variant: Optional[
            Union[
                Var[Literal["classic", "surface", "soft"]],
                Literal["classic", "surface", "soft"],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        radius: Optional[
            Union[
                Var[Literal["none", "small", "medium", "large", "full"]],
                Literal["none", "small", "medium", "large", "full"],
            ]
        ] = None,
        auto_complete: Optional[Union[Var[bool], bool]] = None,
        default_value: Optional[Union[Var[str], str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        max_length: Optional[Union[Var[int], int]] = None,
        min_length: Optional[Union[Var[int], int]] = None,
        name: Optional[Union[Var[str], str]] = None,
        placeholder: Optional[Union[Var[str], str]] = None,
        read_only: Optional[Union[Var[bool], bool]] = None,
        required: Optional[Union[Var[bool], bool]] = None,
        type: Optional[Union[Var[str], str]] = None,
        value: Optional[Union[Var[Union[float, int, str]], str, int, float]] = None,
        access_key: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        auto_capitalize: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        dir: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        draggable: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        enter_key_hint: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        hidden: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        input_mode: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        item_prop: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        lang: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        role: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        slot: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        spell_check: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        tab_index: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        title: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_change: Optional[
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
        on_key_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_key_up: Optional[
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
    ) -> "TextFieldRoot":
        """Create an Input component.

        Args:
            *children: The children of the component.
            size: Text field size "1" - "3"
            variant: Variant of text field: "classic" | "surface" | "soft"
            color_scheme: Override theme color for text field
            radius: Override theme radius for text field: "none" | "small" | "medium" | "large" | "full"
            auto_complete: Whether the input should have autocomplete enabled
            default_value: The value of the input when initially rendered.
            disabled: Disables the input
            max_length: Specifies the maximum number of characters allowed in the input
            min_length: Specifies the minimum number of characters required in the input
            name: Name of the input, used when sending form data
            placeholder: Placeholder text in the input
            read_only: Indicates whether the input is read-only
            required: Indicates that the input is required
            type: Specifies the type of input
            value: Value of the input
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
            **props: The properties of the component.

        Returns:
            The component.
        """
        ...

    @classmethod
    def create_root_deprecated(cls, *children, **props) -> Component: ...
    @classmethod
    def create_input_deprecated(cls, *children, **props) -> Component: ...

class TextFieldSlot(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color_scheme: Optional[
            Union[
                Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
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
    ) -> "TextFieldSlot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            color_scheme: Override theme color for text field slot
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

class TextField(ComponentNamespace):
    root = staticmethod(TextFieldRoot.create_root_deprecated)
    input = staticmethod(TextFieldRoot.create_input_deprecated)
    slot = staticmethod(TextFieldSlot.create)

    @staticmethod
    def __call__(
        *children,
        size: Optional[
            Union[
                Var[
                    Union[
                        Breakpoints[str, Literal["1", "2", "3"]], Literal["1", "2", "3"]
                    ]
                ],
                Literal["1", "2", "3"],
                Breakpoints[str, Literal["1", "2", "3"]],
            ]
        ] = None,
        variant: Optional[
            Union[
                Var[Literal["classic", "surface", "soft"]],
                Literal["classic", "surface", "soft"],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        radius: Optional[
            Union[
                Var[Literal["none", "small", "medium", "large", "full"]],
                Literal["none", "small", "medium", "large", "full"],
            ]
        ] = None,
        auto_complete: Optional[Union[Var[bool], bool]] = None,
        default_value: Optional[Union[Var[str], str]] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        max_length: Optional[Union[Var[int], int]] = None,
        min_length: Optional[Union[Var[int], int]] = None,
        name: Optional[Union[Var[str], str]] = None,
        placeholder: Optional[Union[Var[str], str]] = None,
        read_only: Optional[Union[Var[bool], bool]] = None,
        required: Optional[Union[Var[bool], bool]] = None,
        type: Optional[Union[Var[str], str]] = None,
        value: Optional[Union[Var[Union[float, int, str]], str, int, float]] = None,
        access_key: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        auto_capitalize: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        dir: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        draggable: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        enter_key_hint: Optional[
            Union[Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        hidden: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        input_mode: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        item_prop: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        lang: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        role: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        slot: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        spell_check: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        tab_index: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        title: Optional[Union[Var[Union[bool, int, str]], str, int, bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_change: Optional[
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
        on_key_down: Optional[
            Union[EventHandler, EventSpec, list, Callable, BaseVar]
        ] = None,
        on_key_up: Optional[
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
    ) -> "TextFieldRoot":
        """Create an Input component.

        Args:
            *children: The children of the component.
            size: Text field size "1" - "3"
            variant: Variant of text field: "classic" | "surface" | "soft"
            color_scheme: Override theme color for text field
            radius: Override theme radius for text field: "none" | "small" | "medium" | "large" | "full"
            auto_complete: Whether the input should have autocomplete enabled
            default_value: The value of the input when initially rendered.
            disabled: Disables the input
            max_length: Specifies the maximum number of characters allowed in the input
            min_length: Specifies the minimum number of characters required in the input
            name: Name of the input, used when sending form data
            placeholder: Placeholder text in the input
            read_only: Indicates whether the input is read-only
            required: Indicates that the input is required
            type: Specifies the type of input
            value: Value of the input
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
            **props: The properties of the component.

        Returns:
            The component.
        """
        ...

input = text_field = TextField()
