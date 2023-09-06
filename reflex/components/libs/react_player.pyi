"""Stub file for react_player.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import overload, Optional, Union
from reflex.components.component import Component
from reflex.components.component import NoSSRComponent
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class ReactPlayerComponent(NoSSRComponent):
    @overload
    @classmethod
    def create(cls, *children, url: Optional[Union[Var[str], str]] = None, playing: Optional[Union[Var[str], str]] = None, loop: Optional[Union[Var[bool], bool]] = None, controls: Optional[Union[Var[bool], bool]] = None, light: Optional[Union[Var[bool], bool]] = None, volume: Optional[Union[Var[float], float]] = None, muted: Optional[Union[Var[bool], bool]] = None, width: Optional[Union[Var[str], str]] = None, height: Optional[Union[Var[str], str]] = None, on_mouse_leave: Union[EventHandler, EventSpec] = None, on_focus: Union[EventHandler, EventSpec] = None, on_click: Union[EventHandler, EventSpec] = None, on_mouse_move: Union[EventHandler, EventSpec] = None, on_double_click: Union[EventHandler, EventSpec] = None, on_blur: Union[EventHandler, EventSpec] = None, on_scroll: Union[EventHandler, EventSpec] = None, on_mouse_down: Union[EventHandler, EventSpec] = None, on_mouse_over: Union[EventHandler, EventSpec] = None, on_mouse_enter: Union[EventHandler, EventSpec] = None, on_unmount: Union[EventHandler, EventSpec] = None, on_mouse_out: Union[EventHandler, EventSpec] = None, on_context_menu: Union[EventHandler, EventSpec] = None, on_mount: Union[EventHandler, EventSpec] = None, on_mouse_up: Union[EventHandler, EventSpec] = None, **props) -> "ReactPlayerComponent": ...  # type: ignore
