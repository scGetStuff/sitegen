import unittest
from htmlnode import HTMLNode

css1 = {
    "class": "stuff",
}
# TODO: this breaks when real nodes are done
children = ["h1", "ul"]
value = "This is an HTML node"


class TestHTMLNode(unittest.TestCase):

    # need to check for any error caused by any properties being None
    # all properties are accesed by __repr__()
    def test_None(self):
        node = HTMLNode(None, None, None, None)
        isBroken = False
        try:
            s = str(node)
        except Exception:
            isBroken = True
        self.assertFalse(isBroken, "something being 'None' broke stuff")

    def test_props_to_html(self):
        node = HTMLNode("div", value, children, css1)
        expected = ' class="stuff"'
        self.assertEqual(node.props_to_html(), expected)

    def test_to_html(self):
        node = HTMLNode("div", value, children, css1)
        self.assertRaises(NotImplementedError, node.to_html)

    def test_repr(self):
        node = HTMLNode("div", value, children, css1)
        expected = f'HTMLNode: <div class="stuff">'
        s = str(node)
        self.assertEqual(s.find(expected), 0)
        self.assertEqual(s.find("children:2") > -1, True)
        self.assertEqual(s.find(value) > -1, True)


if __name__ == "__main__":
    unittest.main()
