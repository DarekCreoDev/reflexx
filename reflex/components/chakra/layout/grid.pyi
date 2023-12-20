"""Stub file for reflex/components/chakra/layout/grid.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import List
from reflex.components.libs.chakra import ChakraComponent
from reflex.vars import Var

class Grid(ChakraComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        auto_columns: Optional[Union[Var[str], str]] = None,
        auto_flow: Optional[Union[Var[str], str]] = None,
        auto_rows: Optional[Union[Var[str], str]] = None,
        column: Optional[Union[Var[str], str]] = None,
        row: Optional[Union[Var[str], str]] = None,
        template_columns: Optional[Union[Var[str], str]] = None,
        template_rows: Optional[Union[Var[str], str]] = None,
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
    ) -> "Grid":
        """Create the component.

        Args:
            *children: The children of the component.
            auto_columns: Shorthand prop for gridAutoColumns to provide automatic column sizing based on content.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-columns)_
            auto_flow: Shorthand prop for gridAutoFlow to specify exactly how  auto-placed items get flowed into the grid.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-flow)_
            auto_rows: Shorthand prop for gridAutoRows.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-rows)_
            column: Shorthand prop for gridColumn.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column)_
            row: Shorthand prop for gridRow.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row)_
            template_columns: Shorthand prop for gridTemplateColumns.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-columns)_
            template_rows: Shorthand prop for gridTemplateRows.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-rows)_
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class GridItem(ChakraComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        area: Optional[Union[Var[str], str]] = None,
        col_end: Optional[Union[Var[str], str]] = None,
        col_start: Optional[Union[Var[int], int]] = None,
        col_span: Optional[Union[Var[int], int]] = None,
        row_end: Optional[Union[Var[str], str]] = None,
        row_start: Optional[Union[Var[int], int]] = None,
        row_span: Optional[Union[Var[int], int]] = None,
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
    ) -> "GridItem":
        """Create the component.

        Args:
            *children: The children of the component.
            area: Shorthand prop for gridArea  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-area)_
            col_end: Shorthand prop for gridColumnEnd  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-end)_
            col_start: The column number the grid item should start.
            col_span: The number of columns the grid item should span.
            row_end: Shorthand prop for gridRowEnd  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-end)_
            row_start: The row number the grid item should start.
            row_span: The number of rows the grid item should span.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...

class ResponsiveGrid(ChakraComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        auto_columns: Optional[Union[Var[str], str]] = None,
        auto_flow: Optional[Union[Var[str], str]] = None,
        auto_rows: Optional[Union[Var[str], str]] = None,
        column: Optional[Union[Var[str], str]] = None,
        row: Optional[Union[Var[str], str]] = None,
        columns: Optional[Union[Var[List[int]], List[int]]] = None,
        min_child_width: Optional[Union[Var[str], str]] = None,
        spacing: Optional[Union[Var[str], str]] = None,
        spacing_x: Optional[Union[Var[str], str]] = None,
        spacing_y: Optional[Union[Var[str], str]] = None,
        template_areas: Optional[Union[Var[str], str]] = None,
        template_columns: Optional[Union[Var[str], str]] = None,
        template_rows: Optional[Union[Var[str], str]] = None,
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
    ) -> "ResponsiveGrid":
        """Create the component.

        Args:
            *children: The children of the component.
            auto_columns: Shorthand prop for gridAutoColumns to provide automatic column sizing based on content.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-columns)_
            auto_flow: Shorthand prop for gridAutoFlow to specify exactly how  auto-placed items get flowed into the grid.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-flow)_
            auto_rows: Shorthand prop for gridAutoRows.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-rows)_
            column: Shorthand prop for gridColumn.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column)_
            row: Shorthand prop for gridRow.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row)_
            columns: A list that defines the number of columns for each breakpoint.
            min_child_width: The width at which child elements will break into columns. Pass a number for pixel values or a string for any other valid CSS length.
            spacing: The gap between the grid items
            spacing_x: The column gap between the grid items
            spacing_y: The row gap between the grid items
            template_areas: Shorthand prop for gridTemplateAreas  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas)_
            template_columns: Shorthand prop for gridTemplateColumns.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-columns)_
            template_rows: Shorthand prop for gridTemplateRows.  Learn more _[here](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-rows)_
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
