"""Stub file for image.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Set, Optional, Any, Union, overload
from reflex.components.component import Component
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class Image(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, align: Optional[Union[Var[str], str]] = None, fallback: Optional[Component] = None, fallback_src: Optional[Union[Var[str], str]] = None, fit: Optional[Union[Var[str], str]] = None, html_height: Optional[Union[Var[str], str]] = None, html_width: Optional[Union[Var[str], str]] = None, ignore_fallback: Optional[Union[Var[bool], bool]] = None, loading: Optional[Union[Var[str], str]] = None, src: Optional[Union[Var[Any], Any]] = None, alt: Optional[Union[Var[str], str]] = None, src_set: Optional[Union[Var[str], str]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_load: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_error: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Image":  # type: ignore
        """Create the component.

               Args:
                   *children: The children of the component.
                   align: How to align the image within its bounds. It maps to css `object-position` property.
                   fallback: Fallback Reflex component to show if image is loading or image fails.
                   fallback_src: Fallback image src to show if image is loading or image fails.
                   fit: How the image to fit within its bounds. It maps to css `object-fit` property.
                   html_height: The native HTML height attribute to the passed to the img.
                   html_width: The native HTML width attribute to the passed to the img.
                   ignore_fallback: If true, opt out of the fallbackSrc logic and use as img.
                   loading: "eager" | "lazy"
                   src: The path/url to the image or PIL image object.
                   alt: The alt text of the image.
                   src_set: Provide multiple sources for an image, allowing the browser
        to select the most appropriate source based on factors like
        screen resolution and device capabilities.
        Learn more _[here](https://developer.mozilla.org/en-US/docs/Learn/HTML/Multimedia_and_embedding/Responsive_images)_
                   **props: The props of the component.

               Returns:
                   The component.

               Raises:
                   TypeError: If an invalid child is passed.
        """
        ...
