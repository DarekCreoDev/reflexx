"""Stub file for avatar.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import overload, Set, Optional, Union
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class Avatar(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, icon: Optional[Union[Var[str], str]] = None, icon_label: Optional[Union[Var[str], str]] = None, ignore_fallback: Optional[Union[Var[bool], bool]] = None, name: Optional[Union[Var[str], str]] = None, show_border: Optional[Union[Var[bool], bool]] = None, src: Optional[Union[Var[str], str]] = None, src_set: Optional[Union[Var[str], str]] = None, size: Optional[Union[Var[str], str]] = None, on_mouse_leave: Union[EventHandler, EventSpec] = None, on_focus: Union[EventHandler, EventSpec] = None, on_click: Union[EventHandler, EventSpec] = None, on_mouse_move: Union[EventHandler, EventSpec] = None, on_double_click: Union[EventHandler, EventSpec] = None, on_blur: Union[EventHandler, EventSpec] = None, on_scroll: Union[EventHandler, EventSpec] = None, on_mouse_down: Union[EventHandler, EventSpec] = None, on_mouse_over: Union[EventHandler, EventSpec] = None, on_mouse_enter: Union[EventHandler, EventSpec] = None, on_unmount: Union[EventHandler, EventSpec] = None, on_mouse_out: Union[EventHandler, EventSpec] = None, on_error: Union[EventHandler, EventSpec] = None, on_context_menu: Union[EventHandler, EventSpec] = None, on_mount: Union[EventHandler, EventSpec] = None, on_mouse_up: Union[EventHandler, EventSpec] = None, **props) -> "Avatar": ...  # type: ignore

class AvatarBadge(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, on_mouse_leave: Union[EventHandler, EventSpec] = None, on_focus: Union[EventHandler, EventSpec] = None, on_click: Union[EventHandler, EventSpec] = None, on_mouse_move: Union[EventHandler, EventSpec] = None, on_double_click: Union[EventHandler, EventSpec] = None, on_blur: Union[EventHandler, EventSpec] = None, on_scroll: Union[EventHandler, EventSpec] = None, on_mouse_down: Union[EventHandler, EventSpec] = None, on_mouse_over: Union[EventHandler, EventSpec] = None, on_mouse_enter: Union[EventHandler, EventSpec] = None, on_unmount: Union[EventHandler, EventSpec] = None, on_mouse_out: Union[EventHandler, EventSpec] = None, on_context_menu: Union[EventHandler, EventSpec] = None, on_mount: Union[EventHandler, EventSpec] = None, on_mouse_up: Union[EventHandler, EventSpec] = None, **props) -> "AvatarBadge": ...  # type: ignore

class AvatarGroup(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, max_: Optional[Union[Var[int], int]] = None, spacing: Optional[Union[Var[int], int]] = None, on_mouse_leave: Union[EventHandler, EventSpec] = None, on_focus: Union[EventHandler, EventSpec] = None, on_click: Union[EventHandler, EventSpec] = None, on_mouse_move: Union[EventHandler, EventSpec] = None, on_double_click: Union[EventHandler, EventSpec] = None, on_blur: Union[EventHandler, EventSpec] = None, on_scroll: Union[EventHandler, EventSpec] = None, on_mouse_down: Union[EventHandler, EventSpec] = None, on_mouse_over: Union[EventHandler, EventSpec] = None, on_mouse_enter: Union[EventHandler, EventSpec] = None, on_unmount: Union[EventHandler, EventSpec] = None, on_mouse_out: Union[EventHandler, EventSpec] = None, on_context_menu: Union[EventHandler, EventSpec] = None, on_mount: Union[EventHandler, EventSpec] = None, on_mouse_up: Union[EventHandler, EventSpec] = None, **props) -> "AvatarGroup": ...  # type: ignore
