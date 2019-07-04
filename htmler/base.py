"""HTMLer Base Classes
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import List, Generator, Union, Optional
from os import environ
from abc import ABC, abstractmethod
from copy import copy

INDENT_WIDTH = environ.get('HTMLER_INDENT_WIDTH', 4)

_NODE_SINGLE_ATTRS = ('allowfullscreen', 'async', 'checked', 'hidden', 'selected', 'required')
_NODE_REPLACE_ATTRS = {
    'css': 'class',
    'label_for': 'for',
}


def escape_html(s):
    """Escape an HTML string
    """
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def html_attrs_str(attrs: dict) -> str:
    """Format dictionary as an attributes string
    """
    r = ''
    for k, v in attrs.items():
        k = k.strip().replace('_', '-')
        if k in _NODE_REPLACE_ATTRS:
            k = _NODE_REPLACE_ATTRS[k]

        if v is not None:
            if k in _NODE_SINGLE_ATTRS:
                if v:
                    r += f' {k}'
            else:
                r += f' {k}="{escape_html(str(v).strip())}"'

    return r


class Node(ABC):
    """Base node
    """

    @property
    def name(self):
        """Get node's name
        """
        return self._name

    @property
    def children(self):
        """Get node's children

        :rtype: Generator[Node]
        """
        return (c for c in self._children)

    def __init__(self, *args):
        """Init
        """
        self._name = self.__class__.__name__.lower()
        self._children = []  # type: List[Node]

        for child in args:
            self.append_child(child)

    def append_child(self, child):
        """Append a child node

        :type Node: child
        :rtype Node
        """
        if not isinstance(child, Node):
            raise TypeError(f'{type(child)} cannot be child of {type(self)}')

        self._children.append(child)

        return child

    def wrap(self, wrapper):
        """Wrap the node with another one

        :rtype: Node
        """
        wrapper.append_child(self)

        return wrapper

    @abstractmethod
    def render(self, indent: bool = True) -> str:
        """Render the node
        """
        pass  # pragma: no cover

    def __str__(self) -> str:
        """___str___()
        """
        return self.render()

    def __iter__(self):
        """__iter__()
        """
        return self.children

    def __len__(self) -> int:
        """__len__()
        """
        return len(self._children)

    def __bool__(self) -> bool:
        """__bool__()
        """
        return True


class Text(Node):
    """Text Node
    """

    def __init__(self, content: str = '', escape: bool = False):
        """Init
        """
        super().__init__()

        if not isinstance(content, str):
            content = str(content)

        self._content = escape_html(content) if escape else content

    def append_child(self, child: Node):
        """Append a child node
        """
        raise ValueError(f"'{self._name}' element cannot contain children")

    def render(self, indent: bool = True) -> str:
        """Render the node
        """
        return self._content


class Comment(Text):
    """Comment Node
    """

    def render(self, indent: bool = True) -> str:
        """Render the node
        """
        return f'<!-- {self._content} -->'


class Element(Node):
    """Base HTML element
    """

    @property
    def id(self) -> Optional[str]:
        """Get element's ID
        """
        return self.get_attr('id')

    @property
    def attrs(self) -> dict:
        """Get node's attributes/values
        """
        return copy(self._attrs)

    def __init__(self, *args, **kwargs):
        """Init
        """
        super().__init__(*args)

        self._attrs = {}
        self._children_by_id = {}

        if 'data' in kwargs and isinstance(kwargs['data'], dict):
            for k, v in kwargs['data'].items():
                self.set_attr('data-' + k, v)
            del kwargs['data']

        for k, v in kwargs.items():
            self.set_attr(k, v)

    def set_attr(self, attr: str, value: str):
        """Set attribute
        """
        self._attrs[attr.replace('_', '-')] = value

        return self

    def get_attr(self, attr, default=None) -> str:
        """Get attribute's value
        """
        return self._attrs[attr] if attr in self._attrs else default

    def append_child(self, child: Union[Node, str]):
        """Append a child node
        """
        if isinstance(child, str):
            child = Text(child)

        if isinstance(child, Element) and child.id:
            self._children_by_id[child.id] = child

        return super().append_child(child)

    def append_text(self, text: str) -> Text:
        """Append a text node
        """
        return self.append_child(Text(text))

    def append_comment(self, comment: str) -> Comment:
        """Append a comment node
        """
        return self.append_child(Comment(comment))

    def get_element_by_id(self, em_id: str):
        """Get descendant element

        :rtype: Optional[Element]
        """
        if em_id in self._children_by_id:
            return self._children_by_id[em_id]

        for child in self:
            if not isinstance(child, Element):
                continue

            descendant = child.get_element_by_id(em_id)
            if descendant:
                return descendant

    def has_css(self, css_class: str) -> bool:
        """Check if the element has a CSS class
        """
        return css_class in self.get_attr('css', '')

    def add_css(self, css_class: str):
        """Add a CSS class to the element
        """
        return self.set_attr('css', (self.get_attr('css', '') + ' ' + css_class).strip())

    def remove_css(self, css_class: str):
        """Remove a CSS class from the element
        """
        return self.set_attr('css', (self.get_attr('css', '').replace(css_class, '')).strip())

    def toggle_css(self, css_class: str):
        """Toggle a CSS class of the element
        """
        return self.remove_css(css_class) if self.has_css(css_class) else self.add_css(css_class)

    def _render_open_tag(self, indent: bool = True) -> str:
        """Render opening tag
        """
        return f'<{self._name}{html_attrs_str(self._attrs)}>'

    def _render_children(self, indent: bool) -> str:
        """Render child nodes
        """
        return ''.join(child.render(indent) for child in self)

    def _render_close_tag(self, indent: bool = True) -> str:
        """Render closing tag
        """
        return f'</{self._name}>'

    def render(self, indent: bool = True) -> str:
        """Render the node
        """
        r = self._render_open_tag(indent)
        r += self._render_children(indent)
        r += self._render_close_tag(indent)

        return r


class SingleTagElement(Element):
    """Element without closing tag
    """

    def append_child(self, child: Node):
        """Append a child node
        """
        raise ValueError(f"'{self._name}' element cannot contain children")

    def render(self, indent: bool = True) -> str:
        """Render the element
        """
        return self._render_open_tag(indent)


class TagLessElement(Element):
    """Element With No Tags
    """

    def _render_open_tag(self, indent: bool = True) -> str:
        """Render opening tag
        """
        return ''

    def _render_close_tag(self, indent: bool = True) -> str:
        """Render closing tag
        """
        return ''
