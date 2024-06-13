"""Element classes."""
from __future__ import annotations

from reflex.utils import lazy_loader

_MAPPING = {
    "forms": [
        "button",
        "fieldset",
        "form",
        "input",
        "label",
        "legend",
        "meter",
        "optgroup",
        "option",
        "output",
        "progress",
        "select",
        "textarea",
    ],
    "inline": [
        "a",
        "abbr",
        "b",
        "bdi",
        "bdo",
        "br",
        "cite",
        "code",
        "data",
        "dfn",
        "em",
        "i",
        "kbd",
        "mark",
        "q",
        "rp",
        "rt",
        "ruby",
        "s",
        "samp",
        "small",
        "span",
        "strong",
        "sub",
        "sup",
        "time",
        "u",
        "wbr",
    ],
    "media": [
        "area",
        "audio",
        "img",
        "image",
        "map",
        "track",
        "video",
        "embed",
        "iframe",
        "object",
        "picture",
        "portal",
        "source",
        "svg",
        "defs",
        "lineargradient",
        "stop",
        "path",
    ],
    "metadata": [
        "base",
        "head",
        "link",
        "meta",
        "title",
    ],
    "other": ["details", "dialog", "summary", "slot", "template", "math", "html"],
    "scripts": ["canvas", "noscript", "script"],
    "sectioning": [
        "address",
        "article",
        "aside",
        "body",
        "header",
        "footer",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "main",
        "nav",
        "section",
    ],
    "tables": [
        "caption",
        "col",
        "colgroup",
        "table",
        "td",
        "tfoot",
        "th",
        "thead",
        "tr",
        "tbody",
    ],
    "typography": [
        "blockquote",
        "dd",
        "div",
        "dl",
        "dt",
        "figcaption",
        "hr",
        "ol",
        "li",
        "p",
        "pre",
        "ul",
        "ins",
        "del_",
        "Del",
    ],
}


EXCLUDE = ["del_", "Del", "image"]
for _, v in _MAPPING.items():
    v.extend([mod.capitalize() for mod in v if mod not in EXCLUDE])

_SUBMOD_ATTRS: dict[str, list[str]] = _MAPPING

__getattr__, __dir__, __all__ = lazy_loader.attach(
    __name__,
    submod_attrs=_SUBMOD_ATTRS,
)
