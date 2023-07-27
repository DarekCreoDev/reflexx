"""The page decorator and associated variables and functions."""

from __future__ import annotations

from typing import List, Optional, Union

from reflex.event import EventHandler

DECORATED_PAGES = []


def page(
    route: Optional[str] = None,
    title: Optional[str] = None,
    image: Optional[str] = None,
    description: Optional[str] = None,
    meta: Optional[str] = None,
    on_load: Optional[Union[EventHandler, List[EventHandler]]] = None,
):
    """Decorate a function as a page.

    rx.App() will automatically call add_page() for any method decorated with page
    when App.compile is called.

    All defaults are None because they will use the one from add_page().

    Note: the decorated functions still need to be imported.

    Args:
        route: The route to reach the page.
        title: The title of the page.
        image: The favicon of the page.
        description: The description of the page.
        meta: Additionnal meta to add to the page.
        on_load: The event handler(s) called when the page load.

    Returns:
        The decorated function.
    """
    ...

    def decorator(render_fn):
        kwargs = {}
        if route:
            kwargs["route"] = route
        if title:
            kwargs["title"] = title
        if image:
            kwargs["image"] = image
        if description:
            kwargs["description"] = description
        if meta:
            kwargs["meta"] = meta
        if on_load:
            kwargs["on_load"] = on_load

        DECORATED_PAGES.append((render_fn, kwargs))

        return render_fn

    return decorator
