"""Stub file for reflex/components/radix/themes/typography/link.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Literal
from reflex.components.component import Component, MemoizationLeaf
from reflex.components.core.breakpoints import Responsive
from reflex.components.core.colors import color
from reflex.components.core.cond import cond
from reflex.components.el.elements.inline import A
from reflex.components.next.link import NextLink
from reflex.utils.imports import ImportDict
from reflex.vars import Var
from ..base import LiteralAccentColor, RadixThemesComponent
from .base import LiteralTextSize, LiteralTextTrim, LiteralTextWeight

LiteralLinkUnderline = Literal["auto", "hover", "always", "none"]
next_link = NextLink.create()

class Link(RadixThemesComponent, A, MemoizationLeaf):
    def add_imports(self) -> ImportDict: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[reflex.vars.Var[bool], bool]] = None,
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
        trim: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["normal", "start", "end", "both"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str, Literal["normal", "start", "end", "both"]
                        ],
                    ]
                ],
                Union[
                    Literal["normal", "start", "end", "both"],
                    reflex.components.core.breakpoints.Breakpoints[
                        str, Literal["normal", "start", "end", "both"]
                    ],
                ],
            ]
        ] = None,
        underline: Optional[
            Union[
                reflex.vars.Var[Literal["auto", "hover", "always", "none"]],
                Literal["auto", "hover", "always", "none"],
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
        is_external: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        download: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        href: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        href_lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        media: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        ping: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        referrer_policy: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        rel: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        shape: Optional[
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
    ) -> "Link":
        """Create a Link component.

        Args:
            *children: The children of the component.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            size: Text size: "1" - "9"
            weight: Thickness of text: "light" | "regular" | "medium" | "bold"
            trim: Removes the leading trim space: "normal" | "start" | "end" | "both"
            underline: Sets the visibility of the underline affordance: "auto" | "hover" | "always" | "none"
            color_scheme: Overrides the accent color inherited from the Theme.
            high_contrast: Whether to render the text with higher contrast color
            is_external: If True, the link will open in a new tab
            download: Specifies that the target (the file specified in the href attribute) will be downloaded when a user clicks on the hyperlink.
            href: Specifies the URL of the page the link goes to
            href_lang: Specifies the language of the linked document
            media: Specifies what media/device the linked document is optimized for
            ping: Specifies which referrer is sent when fetching the resource
            referrer_policy: Specifies the relationship between the current document and the linked document
            rel: Specifies the relationship between the linked document and the current document
            shape: Specifies the shape of the area
            target: Specifies where to open the linked document
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

        Raises:
            ValueError: in case of missing children

        Returns:
            Component: The link component
        """
        ...

link = Link.create
