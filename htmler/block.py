"""HTMLer Block Elements
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from os import linesep
from .base import Element, SingleTagElement, INDENT_WIDTH


class BlockElement(Element):
    """Block element
    """

    def _render_open_tag(self, indent: bool = True) -> str:
        """Render opening tag
        """
        r = super()._render_open_tag(indent)

        return (r + linesep) if (indent and (len(self) or isinstance(self, SingleTagElement))) else r

    def _render_children(self, indent: bool) -> str:
        r = super()._render_children(indent)

        if indent:
            rn = ''
            for l in r.split(linesep):
                if l:
                    rn += (' ' * INDENT_WIDTH) + l + linesep
            r = rn

        return r

    def _render_close_tag(self, indent: bool = True) -> str:
        r = super()._render_close_tag(indent)

        return (r + linesep) if indent else r


class Address(BlockElement):
    """ADDRESS Element
    """
    pass


class Area(BlockElement, SingleTagElement):
    """AREA Element
    """
    pass


class Article(BlockElement):
    """ARTICLE Element
    """
    pass


class Aside(BlockElement):
    """ASIDE Element
    """
    pass


class Audio(BlockElement):
    """AUDIO Element
    """
    pass


class Base(BlockElement, SingleTagElement):
    """BASE Element
    """
    pass


class Body(BlockElement):
    """BODY Element
    """
    pass


class Blockquote(BlockElement):
    """BLOCKQUOTE Element
    """
    pass


class Canvas(BlockElement):
    """CANVAS Element
    """
    pass


class Caption(BlockElement):
    """CAPTION Element
    """
    pass


class Col(BlockElement, SingleTagElement):
    """COL Element
    """
    pass


class Colgroup(BlockElement):
    """COLGROUP Element
    """
    pass


class Datalist(BlockElement):
    """DATALIST Element
    """
    pass


class Dd(BlockElement):
    """DD Element
    """
    pass


class Details(BlockElement):
    """DETAILS Element
    """
    pass


class Dialog(BlockElement):
    """DIALOG Element
    """
    pass


class Div(BlockElement):
    """DIV Element
    """
    pass


class Dl(BlockElement):
    """DL Element
    """
    pass


class Dt(BlockElement):
    """DT Element
    """
    pass


class Embed(BlockElement, SingleTagElement):
    """EMBED Element
    """
    pass


class Fieldset(BlockElement):
    """FIELDSET Element
    """
    pass


class Figcaption(BlockElement):
    """FIGCAPTION Element
    """
    pass


class Figure(BlockElement):
    """FIGURE Element
    """
    pass


class Footer(BlockElement):
    """FOOTER Element
    """
    pass


class Form(BlockElement):
    """FORM Element
    """
    pass


class H1(BlockElement):
    """H1 Element
    """
    pass


class H2(BlockElement):
    """H2 Element
    """
    pass


class H3(BlockElement):
    """H3 Element
    """
    pass


class H4(BlockElement):
    """H4 Element
    """
    pass


class H5(BlockElement):
    """H5 Element
    """
    pass


class H6(BlockElement):
    """H6 Element
    """
    pass


class Head(BlockElement):
    """HEAD Element
    """
    pass


class Header(BlockElement):
    """HEADER Element
    """
    pass


class Hr(BlockElement):
    """HR Element
    """
    pass


class Html(BlockElement):
    """HTML Element
    """

    def _render_open_tag(self, indent: bool = True) -> str:
        return '<!DOCTYPE html>' + (linesep if indent else '') + super()._render_open_tag(indent)


class Iframe(BlockElement):
    """IFRAME Element
    """
    pass


class Li(BlockElement):
    """LI Element
    """
    pass


class Link(BlockElement, SingleTagElement):
    """LINK Element
    """
    pass


class Main(BlockElement, SingleTagElement):
    """MAIN Element
    """
    pass


class Map(BlockElement):
    """MAP Element
    """
    pass


class Menu(BlockElement):
    """MENU Element
    """
    pass


class Meta(BlockElement, SingleTagElement):
    """META Element
    """
    pass


class Nav(BlockElement):
    """NAV Element
    """
    pass


class Noscript(BlockElement):
    """NOSCRIPT Element
    """
    pass


class Object(BlockElement):
    """OBJECT Element
    """
    pass


class Ol(BlockElement):
    """OL Element
    """
    pass


class Optgroup(BlockElement):
    """OPTGROUP Element
    """
    pass


class Option(BlockElement):
    """OPTION Element
    """
    pass


class P(BlockElement):
    """P Element
    """
    pass


class Param(BlockElement, SingleTagElement):
    """PARAM Element
    """
    pass


class Pre(BlockElement):
    """PRE Element
    """
    pass


class Progress(BlockElement):
    """PROGRESS Element
    """
    pass


class Ruby(BlockElement):
    """RUBY Element
    """
    pass


class Samp(BlockElement):
    """SAMP Element
    """
    pass


class Script(BlockElement):
    """SCRIPT Element
    """
    pass


class Section(BlockElement):
    """SECTION Element
    """
    pass


class Select(BlockElement):
    """SELECT Element
    """
    pass


class Slot(BlockElement):
    """SLOT Element
    """
    pass


class Source(BlockElement, SingleTagElement):
    """SOURCE Element
    """
    pass


class Style(BlockElement):
    """STYLE Element
    """
    pass


class Summary(BlockElement):
    """SUMMARY Element
    """
    pass


class Table(BlockElement):
    """TABLE Element
    """
    pass


class Tbody(BlockElement):
    """TBODY Element
    """
    pass


class Td(BlockElement):
    """TD Element
    """
    pass


class Template(BlockElement):
    """TEMPLATE Element
    """
    pass


class Textarea(BlockElement):
    """TEXTAREA Element
    """
    pass


class Tfoot(BlockElement):
    """TFOOT Element
    """
    pass


class Th(BlockElement):
    """TH Element
    """
    pass


class Thead(BlockElement):
    """THEAD Element
    """
    pass


class Title(BlockElement):
    """TITLE Element
    """
    pass


class Tr(BlockElement):
    """TR Element
    """
    pass


class Track(BlockElement, SingleTagElement):
    """TRACK Element
    """
    pass


class Ul(BlockElement):
    """UL Element
    """
    pass


class Video(BlockElement):
    """VIDEO Element
    """
    pass
