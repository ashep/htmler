"""HTMLer Tests
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import pytest, random, string, htmler
from os import linesep
from random import randint as random_int
from typing import Union, List, Type, Tuple
from inspect import isclass


def random_str(length: int = 8):
    """Generate a random string of fixed length
    """
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def _get_elements_classes(subcls_only: Union[Type, Tuple[Type, ...]] = None,
                          except_subcls: Union[Type, Tuple[Type, ...]] = None) -> List[Type[htmler.Element]]:
    r = []
    for n in dir(htmler):
        cls = getattr(htmler, n)

        if not isclass(cls) or issubclass(cls, (htmler.TagLessElement, htmler.Html)):
            continue

        if issubclass(cls, htmler.Element) and not (except_subcls and issubclass(cls, except_subcls)):
            if subcls_only:
                if issubclass(cls, subcls_only):
                    r.append(cls)
            else:
                r.append(cls)

    return r


class TestElements:
    """Test Elements
    """

    @staticmethod
    def _test_render(cls: Type[htmler.Element], rendered_children: str = '', *children, **attrs):
        """Helper method
        """
        em = cls(*children, **attrs)

        attrs_str = htmler.html_attrs_str(attrs)

        # Element with no tags
        if isinstance(em, htmler.TagLessElement):
            assert em.render(False) == rendered_children

        # Element with no closing tags
        elif isinstance(em, htmler.SingleTagElement):
            assert em.render(False) == f'<{em.name}{attrs_str}>'

        # Element with opening and closing tags pair
        else:
            assert em.render(False) == f'<{em.name}{attrs_str}>{rendered_children}</{em.name}>'

    def test_not_abc(self):
        with pytest.raises(TypeError):
            htmler.Node().render()

    def test_empty(self):
        """Test of rendering of an empty elements
        """
        for cls in _get_elements_classes():
            self._test_render(cls)

    def test_str(self):
        """Test __str__() method
        """
        for cls in _get_elements_classes(htmler.BlockElement):
            em = cls()
            if isinstance(em, htmler.SingleTagElement):
                assert str(em) == f'<{em.name}>{linesep}'
            else:
                if len(em):
                    assert str(em) == f'<{em.name}>{linesep}</{em.name}>{linesep}'
                else:
                    assert str(em) == f'<{em.name}></{em.name}>{linesep}'

        for cls in _get_elements_classes(htmler.InlineElement):
            em = cls()
            if isinstance(em, htmler.SingleTagElement):
                assert str(em) == f'<{em.name}>'
            else:
                assert str(em) == f'<{em.name}></{em.name}>'

    def test_append_child(self):
        for parent_cls in _get_elements_classes(except_subcls=htmler.SingleTagElement):
            for child_cls in _get_elements_classes(htmler.SingleTagElement):
                child = child_cls()
                self._test_render(parent_cls, f'<{child.name}>', child)

            for child_cls in _get_elements_classes(except_subcls=htmler.SingleTagElement):
                child = child_cls()
                self._test_render(parent_cls, f'<{child.name}></{child.name}>', child)

        em_1 = htmler.Element()
        em_2 = htmler.Element()
        assert len(em_1) == 0

        em_1.append_child(em_2)
        assert len(em_1) == 1

    def test_append_child_exception(self):
        """Test of impossibility of adding children to SingleTagElement
        """
        for parent_cls in _get_elements_classes(htmler.SingleTagElement):
            for child_cls in _get_elements_classes():
                with pytest.raises(ValueError):
                    child = child_cls()
                    self._test_render(parent_cls, f'<{child.name}></{child.name}>', child)

        for invalid_child in 1, [], ():
            with pytest.raises(TypeError):
                htmler.Element(invalid_child)

    def test_wrap(self):
        """Test of wrapping an element with another one
        """
        for child_cls in _get_elements_classes():
            for wrapper_cls in _get_elements_classes(except_subcls=(htmler.SingleTagElement, htmler.Html)):
                child = child_cls()
                wrapper = child.wrap(wrapper_cls())
                assert wrapper.render(False) == f'<{wrapper.name}>{child.render(False)}</{wrapper.name}>'

    def test_text(self):
        """Test of adding text to elements
        """
        s = random_str()
        for cls in _get_elements_classes(except_subcls=htmler.SingleTagElement):
            self._test_render(cls, s, htmler.Text(s))
            self._test_render(cls, s, s)

        # Pass not str as first argument
        n = random_int(0, 65535)
        assert htmler.Text(n).render() == str(n)

    def test_text_append_child(self):
        with pytest.raises(ValueError):
            htmler.Text().append_child(htmler.Text())

    def test_comment(self):
        """Test of adding comments to elements
        """
        s = random_str()

        for cls in _get_elements_classes(except_subcls=htmler.SingleTagElement):
            self._test_render(cls, f'<!-- {s} -->', htmler.Comment(s))

    def test_attrs(self):
        """Test of attributes handling
        """
        for cls in _get_elements_classes():
            s1 = random_str()
            s2 = random_str()

            # Ordinary attributes
            self._test_render(cls, attr=s1, attr_abc=s2)

            # Single attributes
            self._test_render(cls, allowfullscreen=True, checked=True, hidden=True, selected=True, required=True)

            # Replaceable attributes
            self._test_render(cls, label_for=s1, css=s2)

            # Get attributes
            em = cls(attr1=s1, attr2=s2)
            assert em.attrs == {'attr1': s1, 'attr2': s2}
            assert em.get_attr('attr1') == s1
            assert em.get_attr('attr2') == s2

            # Set attributes
            em.set_attr('attr3', s1)
            em.set_attr('attr4', s2)
            assert em.attrs == {'attr1': s1, 'attr2': s2, 'attr3': s1, 'attr4': s2}
            assert em.get_attr('attr3') == s1
            assert em.get_attr('attr4') == s2

            # Init 'data-*' attrs via constructor
            assert cls(data={'attr1': s1, 'attr2': s2}).attrs == {'data-attr1': s1, 'data-attr2': s2}

    def test_append_text(self):
        """Test of append_text() method
        """
        for cls in _get_elements_classes(except_subcls=htmler.SingleTagElement):
            s = random_str()
            em = cls()
            em.append_text(s)
            assert em.render(False) == f'<{em.name}>{s}</{em.name}>'

    def test_append_comment(self):
        """Test of append_comment() method
        """
        for cls in _get_elements_classes(htmler.BlockElement, htmler.SingleTagElement):
            s = random_str()
            em = cls()
            em.append_comment(s)
            assert em.render(False) == f'<{em.name}><!-- {s} --></{em.name}>'

    def test_get_element_by_id(self):
        for parent_cls in _get_elements_classes(except_subcls=htmler.SingleTagElement):
            parent_em = parent_cls()
            parent_em.append_text(random_str())
            parent_em.append_comment(random_str())
            for child_cls in _get_elements_classes(except_subcls=htmler.SingleTagElement):
                child_2_id = random_str()
                child_2_em = child_cls(id=child_2_id)
                parent_em.append_child(child_cls(id=random_str())).append_child(child_2_em)
                assert parent_em.get_element_by_id(child_2_id) == child_2_em

    def test_css(self):
        """Test of the *_css() methods
        """
        for cls in _get_elements_classes():
            css_1 = random_str()
            css_2 = random_str()
            css_3 = random_str()

            em = cls(css=f'{css_1} {css_2}')
            assert em.has_css(css_1) is True
            assert em.has_css(css_2) is True
            assert em.has_css(css_3) is False

            em.add_css(css_3)
            assert em.has_css(css_3) is True

            em.remove_css(css_1)
            assert em.has_css(css_1) is False

            em.toggle_css(css_1)
            assert em.has_css(css_1) is True

    def test_tagless(self):
        """Test of rendering of the TagLessElement
        """
        for cls in _get_elements_classes():
            child = cls()
            assert htmler.TagLessElement(child).render() == child.render()

    def test_render_children_indent(self):
        """Test of rendering children of block elements with indentation
        """
        for cls in _get_elements_classes(htmler.BlockElement, htmler.SingleTagElement):
            s = random_str()
            em = cls(s)
            assert em.render() == f'<{em.name}>{linesep}{(htmler.INDENT_WIDTH * " ")}{s}{linesep}</{em.name}>{linesep}'
