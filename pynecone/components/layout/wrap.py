"""Container to stack elements with spacing."""

from pynecone.components.component import Component
from pynecone.components.libs.chakra import ChakraComponent
from pynecone.var import Var


class Wrap(ChakraComponent):
    """Layout component used to add space between elements and wrap automatically if there isn't enough space."""

    tag = "Wrap"

    # How to align the items.
    align: Var[str]

    # The flex direction of the wrap.
    direction: Var[str]

    # How to justify the items.
    justify: Var[str]

    # Whether to wrap children in `pc.wrap_item`.
    should_wrap_children: Var[bool]

    # The spacing between the items.
    spacing: Var[str]

    # The horizontal spacing between the items.
    spacing_x: Var[str]

    # The vertical spacing between the items.
    spacing_y: Var[str]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Return a wrap component.

        Args:
            children: The children of the component.
            props: The properties of the component.

        Returns:
            The wrap component.
        """
        if not children:
            children = []
            items = props.pop("items", [])
            for item in items:
                children.append(WrapItem.create(*item))

        return super().create(*children, **props)


class WrapItem(ChakraComponent):
    """Item of the Wrap component."""

    tag = "WrapItem"
