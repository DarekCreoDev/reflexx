"""Stub file for reflex/components/radix/themes/components/textfield.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Dict, Literal
from reflex.components import el
from reflex.components.component import Component
from reflex.components.forms.debounce import DebounceInput
from reflex.constants import EventTriggers
from reflex.vars import Var
from ..base import (
    CommonMarginProps,
    LiteralAccentColor,
    LiteralRadius,
    LiteralSize,
    RadixThemesComponent,
)

LiteralTextFieldSize = Literal["1", "2", "3"]
LiteralTextFieldVariant = Literal["classic", "surface", "soft"]

class TextFieldRoot(el.Div, CommonMarginProps, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color: Optional[str] = None,
        color_scheme: Optional[str] = None,
        size: Optional[
            Union[Var[Literal["1", "2", "3"]], Literal["1", "2", "3"]]
        ] = None,
        variant: Optional[
            Union[
                Var[Literal["classic", "surface", "soft"]],
                Literal["classic", "surface", "soft"],
            ]
        ] = None,
        radius: Optional[
            Union[
                Var[Literal["none", "small", "medium", "large", "full"]],
                Literal["none", "small", "medium", "large", "full"],
            ]
        ] = None,
        access_key: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        auto_capitalize: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        dir: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        draggable: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        enter_key_hint: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        hidden: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        input_mode: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        item_prop: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        lang: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        role: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        slot: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        spell_check: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        tab_index: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        title: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        translate: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        m: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mx: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        my: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mt: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mr: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mb: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        ml: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
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
    ) -> "TextFieldRoot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            color: map to CSS default color property.
            color_scheme: map to radix color property.
            size: Text field size "1" - "3"
            variant: Variant of text field: "classic" | "surface" | "soft"
            radius: Override theme radius for text field: "none" | "small" | "medium" | "large" | "full"
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
            translate: Specifies whether the content of an element should be translated or not.
            m: Margin: "0" - "9"
            mx: Margin horizontal: "0" - "9"
            my: Margin vertical: "0" - "9"
            mt: Margin top: "0" - "9"
            mr: Margin right: "0" - "9"
            mb: Margin bottom: "0" - "9"
            ml: Margin left: "0" - "9"
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

class TextFieldInput(el.Input, TextFieldRoot):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        accept: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        alt: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        auto_complete: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        auto_focus: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        capture: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        checked: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        dirname: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        disabled: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        form_action: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form_enc_type: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form_method: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form_no_validate: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form_target: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        height: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        list: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        max: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        max_length: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        min_length: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        min: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        multiple: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        name: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        pattern: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        placeholder: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        read_only: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        required: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        size: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        src: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        step: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        type: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        use_map: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        value: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        width: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        variant: Optional[
            Union[
                Var[Literal["classic", "surface", "soft"]],
                Literal["classic", "surface", "soft"],
            ]
        ] = None,
        color: Optional[
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
        access_key: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        auto_capitalize: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        dir: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        draggable: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        enter_key_hint: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        hidden: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        input_mode: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        item_prop: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        lang: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        role: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        slot: Optional[Union[Var[Union[str, int, bool]], Union[str, int, bool]]] = None,
        spell_check: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        tab_index: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        title: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        translate: Optional[
            Union[Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        m: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mx: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        my: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mt: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mr: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        mb: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
        ] = None,
        ml: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
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
        on_change: Optional[
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
        on_key_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_key_up: Optional[
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
    ) -> "TextFieldInput":
        """Create an Input component.

        Args:
            *children: The children of the component.
            accept: Accepted types of files when the input is file type
            alt: Alternate text for input type="image"
            auto_complete: Whether the input should have autocomplete enabled
            auto_focus: Automatically focuses the input when the page loads
            capture: Captures media from the user (camera or microphone)
            checked: Indicates whether the input is checked (for checkboxes and radio buttons)
            dirname: Name part of the input to submit in 'dir' and 'name' pair when form is submitted
            disabled: Disables the input
            form: Associates the input with a form (by id)
            form_action: URL to send the form data to (for type="submit" buttons)
            form_enc_type: How the form data should be encoded when submitting to the server (for type="submit" buttons)
            form_method: HTTP method to use for sending form data (for type="submit" buttons)
            form_no_validate: Bypasses form validation when submitting (for type="submit" buttons)
            form_target: Specifies where to display the response after submitting the form (for type="submit" buttons)
            height: The height of the input (only for type="image")
            list: References a datalist for suggested options
            max: Specifies the maximum value for the input
            max_length: Specifies the maximum number of characters allowed in the input
            min_length: Specifies the minimum number of characters required in the input
            min: Specifies the minimum value for the input
            multiple: Indicates whether multiple values can be entered in an input of the type email or file
            name: Name of the input, used when sending form data
            pattern: Regex pattern the input's value must match to be valid
            placeholder: Placeholder text in the input
            read_only: Indicates whether the input is read-only
            required: Indicates that the input is required
            size: Text field size "1" - "3"
            src: URL for image inputs
            step: Specifies the legal number intervals for an input
            type: Specifies the type of input
            use_map: Name of the image map used with the input
            value: Value of the input
            width: The width of the input (only for type="image")
            variant: Variant of text field: "classic" | "surface" | "soft"
            color: Override theme color for text field
            radius: Override theme radius for text field: "none" | "small" | "medium" | "large" | "full"
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
            translate: Specifies whether the content of an element should be translated or not.
            m: Margin: "0" - "9"
            mx: Margin horizontal: "0" - "9"
            my: Margin vertical: "0" - "9"
            mt: Margin top: "0" - "9"
            mr: Margin right: "0" - "9"
            mb: Margin bottom: "0" - "9"
            ml: Margin left: "0" - "9"
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
    def get_event_triggers(self) -> Dict[str, Any]: ...

class TextFieldSlot(RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        color: Optional[str] = None,
        color_scheme: Optional[str] = None,
        gap: Optional[
            Union[
                Var[Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]],
                Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
            ]
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
    ) -> "TextFieldSlot":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            color: map to CSS default color property.
            color_scheme: map to radix color property.
            gap: Override the gap spacing between slot and input: "1" - "9"
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
