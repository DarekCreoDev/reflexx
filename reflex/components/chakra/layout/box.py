"""A box component that can contain other components."""


from reflex.components.chakra.layout.base import ChakraLayoutComponent
from reflex.components.tags import Tag
from reflex.vars import Var


class Box(ChakraLayoutComponent):
    """A generic container component that can contain other components."""

    tag = "Box"

    # The type element to render. You can specify an image, video, or any other HTML element such as iframe.
    element: Var[str]

    # The source of the content.
    src: Var[str]

    # The alt text of the content.
    alt: Var[str]

    def _render(self) -> Tag:
        return (
            super()
            ._render()
            .add_props(
                **{
                    "as": self.element,
                }
            )
        )
