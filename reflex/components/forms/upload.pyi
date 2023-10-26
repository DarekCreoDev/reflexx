"""Stub file for reflex/components/forms/upload.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Literal, overload, Dict, Optional, Union, List
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Dict, List, Optional, Union
from reflex.components.component import Component
from reflex.components.forms.input import Input
from reflex.components.layout.box import Box
from reflex.constants import EventTriggers
from reflex.event import EventChain
from reflex.vars import BaseVar, Var

files_state: str
upload_file: BaseVar
selected_files: BaseVar
clear_selected_files: BaseVar

class Upload(Component):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        accept: Optional[
            Union[Var[Optional[Dict[str, List]]], Optional[Dict[str, List]]]
        ] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        max_files: Optional[Union[Var[int], int]] = None,
        max_size: Optional[Union[Var[int], int]] = None,
        min_size: Optional[Union[Var[int], int]] = None,
        multiple: Optional[Union[Var[bool], bool]] = None,
        no_click: Optional[Union[Var[bool], bool]] = None,
        no_drag: Optional[Union[Var[bool], bool]] = None,
        no_keyboard: Optional[Union[Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, str]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_drop: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, List, function, BaseVar]
        ] = None,
        **props
    ) -> "Upload":
        """Create an upload component.

        Args:
            *children: The children of the component.
            accept: The list of accepted file types. This should be a dictionary of MIME types as keys and array of file formats as  values.  supported MIME types: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
            disabled: Whether the dropzone is disabled.
            max_files: The maximum number of files that can be uploaded.
            max_size: The maximum file size (bytes) that can be uploaded.
            min_size: The minimum file size (bytes) that can be uploaded.
            multiple: Whether to allow multiple files to be uploaded.
            no_click: Whether to disable click to upload.
            no_drag: Whether to disable drag and drop.
            no_keyboard: Whether to disable using the space/enter keys to upload.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The properties of the component.

        Returns:
            The upload component.
        """
        ...
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
