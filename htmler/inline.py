"""HTMLer Inline Elements
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from .base import Element, SingleTagElement


class InlineElement(Element):
    """Base Inline Element
    """
    pass


class A(InlineElement):
    """A Element
    """
    pass


class Abbr(InlineElement):
    """ABBR Element
    """
    pass


class B(InlineElement):
    """B Element
    """
    pass


class Bdi(InlineElement):
    """BDI Element
    """
    pass


class Bdo(InlineElement):
    """BDO Element
    """
    pass


class Br(InlineElement, SingleTagElement):
    """BR Element
    """
    pass


class Button(InlineElement):
    """BUTTON Element
    """
    pass


class Cite(InlineElement):
    """CITE Element
    """
    pass


class Code(InlineElement):
    """CODE Element
    """
    pass


class Data(InlineElement):
    """DATA Element
    """
    pass


class Del(InlineElement):
    """DEL Element
    """
    pass


class Dfn(InlineElement):
    """DFN Element
    """
    pass


class Em(InlineElement):
    """EM Element
    """
    pass


class I(InlineElement):
    """I Element
    """
    pass


class Img(InlineElement, SingleTagElement):
    """IMG Element
    """
    pass


class Input(InlineElement, SingleTagElement):
    """INPUT Element
    """
    pass


class Ins(InlineElement, SingleTagElement):
    """INS Element
    """
    pass


class Kbd(InlineElement, SingleTagElement):
    """KBD Element
    """
    pass


class Label(InlineElement):
    """LABEL Element
    """
    pass


class Legend(InlineElement):
    """LEGEND Element
    """
    pass


class Meter(InlineElement):
    """METER Element
    """
    pass


class Mark(InlineElement):
    """MARK Element
    """
    pass


class Output(InlineElement):
    """OUTPUT Element
    """
    pass


class Progress(InlineElement):
    """PROGRESS Element
    """
    pass


class Q(InlineElement):
    """Q Element
    """
    pass


class Rp(InlineElement):
    """RP Element
    """
    pass


class Rt(InlineElement):
    """RT Element
    """
    pass


class Rtc(InlineElement):
    """RTC Element
    """
    pass


class S(InlineElement):
    """S Element
    """
    pass


class Small(InlineElement):
    """SMALL Element
    """
    pass


class Span(InlineElement):
    """SPAN Element
    """
    pass


class Strong(InlineElement):
    """STRONG Element
    """
    pass


class Sub(InlineElement):
    """SUB Element
    """
    pass


class Sup(InlineElement):
    """SUP Element
    """
    pass


class Time(InlineElement):
    """TIME Element
    """
    pass


class U(InlineElement):
    """U Element
    """
    pass


class Var(InlineElement):
    """VAR Element
    """
    pass


class Wbr(InlineElement):
    """WBR Element
    """
    pass
