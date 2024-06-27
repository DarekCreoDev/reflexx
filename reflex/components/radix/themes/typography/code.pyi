"""Stub file for reflex/components/radix/themes/typography/code.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from reflex.components.core.breakpoints import Responsive
from reflex.components.el import elements
from reflex.vars import Var
from ..base import LiteralAccentColor, LiteralVariant, RadixThemesComponent
from .base import LiteralTextSize, LiteralTextWeight

class Code(elements.Code, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        variant: Optional[
            Union[
                reflex.vars.Var[
                    Literal["classic", "solid", "soft", "surface", "outline", "ghost"]
                ],
                Literal["classic", "solid", "soft", "surface", "outline", "ghost"],
            ]
        ] = None,
        size: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                        ],
                    ]
                ],
                Union[
                    Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    reflex.components.core.breakpoints.Breakpoints[
                        str, Literal["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                    ],
                ],
            ]
        ] = None,
        weight: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["light", "regular", "medium", "bold"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str, Literal["light", "regular", "medium", "bold"]
                        ],
                    ]
                ],
                Union[
                    Literal["light", "regular", "medium", "bold"],
                    reflex.components.core.breakpoints.Breakpoints[
                        str, Literal["light", "regular", "medium", "bold"]
                    ],
                ],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                reflex.vars.Var[
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
        high_contrast: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        access_key: Optional[
<<<<<<< HEAD
<<<<<<< HEAD
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
=======
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        auto_capitalize: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        dir: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        draggable: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        enter_key_hint: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        hidden: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        input_mode: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        item_prop: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        lang: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        role: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        slot: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        spell_check: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        tab_index: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        title: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
>>>>>>> 2027a2f0 (order type annotations in pyi_generator (#3585))
=======
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        auto_capitalize: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        dir: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        draggable: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        enter_key_hint: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        hidden: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        input_mode: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        item_prop: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        lang: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        role: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        slot: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        spell_check: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        tab_index: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        title: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
>>>>>>> 2027a2f0 (order type annotations in pyi_generator (#3585))
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
    ) -> "Code":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            variant: The visual variant to apply: "solid" | "soft" | "outline" | "ghost"
            size: Text size: "1" - "9"
            weight: Thickness of text: "light" | "regular" | "medium" | "bold"
            color_scheme: Overrides the accent color inherited from the Theme.
            high_contrast: Whether to render the text with higher contrast color
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
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

code = Code.create
