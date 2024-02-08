"""Image component from next/image."""

from typing import Any, Dict, Literal

from reflex.components.el import Img, Div
from reflex.vars import Var

from .base import NextComponent

from reflex.components.radix.themes.layout.box import Box


class Image(NextComponent):
    """Display an image."""

    tag = "Image"
    library = "next/image"
    is_default = True

    # This can be either an absolute external URL, or an internal path
    src: Var[Any]

    # Represents the rendered width in pixels, so it will affect how large the image appears.
    width: Var[int]

    # Represents the rendered height in pixels, so it will affect how large the image appears.
    height: Var[int]

    # Used to describe the image for screen readers and search engines.
    alt: Var[str]

    # A custom function used to resolve image URLs.
    loader: Var[Any]

    # A boolean that causes the image to fill the parent element, which is useful when the width and height are unknown. Default to True
    fill: Var[bool]

    # A string, similar to a media query, that provides information about how wide the image will be at different breakpoints.
    sizes: Var[str]

    # The quality of the optimized image, an integer between 1 and 100, where 100 is the best quality and therefore largest file size. Defaults to 75.
    quality: Var[int]

    # When true, the image will be considered high priority and preload. Lazy loading is automatically disabled for images using priority.
    priority: Var[bool]

    # A placeholder to use while the image is loading. Possible values are blur, empty, or data:image/.... Defaults to empty.
    placeholder: Var[str]

    # Allows passing CSS styles to the underlying image element.
    # style: Var[Any]

    # The loading behavior of the image. Defaults to lazy. Can hurt performance, recommended to use `priority` instead.
    loading: Var[Literal["lazy", "eager"]]

    # A Data URL to be used as a placeholder image before the src image successfully loads. Only takes effect when combined with placeholder="blur".
    blurDataURL: Var[str]

    def get_event_triggers(self) -> Dict[str, Any]:
        """The event triggers of the component.

        Returns:
            The dict describing the event triggers.
        """
        return {
            **super().get_event_triggers(),
            "on_load": lambda: [],
            "on_error": lambda: [],
        }

    @classmethod
    def create(
        cls,
        *children,
        **props,
    ):
        """Create an Image component from next/image.

        Args:
            *children: The children of the component.
            **props:The props of the component.

        Returns:
            _type_: _description_
        """
        if "width" not in props or "height" not in props:
            # props.pop("width", None)
            # props.pop("height", None)
            if "width" in props:
                props["width"] = f"{props['width']}px"
            if "height" in props:
                props["height"] = f"{props['height']}px"
                # return Box.create(
                #     Img.create(*children, **props),
                #     width=props.get("width", None),
                #     height=props.get("height", None),
                # )
                return Div.create(
                    Img.create(*children, **props),
                    style={
                        "width": props.get("width", None),
                        "height": props.get("height", None),
                        "border": props.get("border", None),
                    },
                )
            return Img.create(*children, **props)
        src = props.get("src", None)
        if src is not None and not isinstance(src, (Var)):
            props["src"] = Var.create(value=src, _var_is_string=True)

        return super().create(*children, **props)
