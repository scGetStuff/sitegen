import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

        node1 = TextNode(None, None, None)
        node2 = TextNode(None, None, None)
        self.assertEqual(node1, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        expected = "TextNode(This is a text node, bold, https://www.boot.dev)"
        self.assertEqual(str(node), expected)

        node = TextNode("This is a text node", TextType.BOLD)
        expected = "TextNode(This is a text node, bold, None)"
        self.assertEqual(str(node), expected)

    def test_ne(self):
        node1 = TextNode("node1", TextType.BOLD)
        node2 = TextNode("node2", TextType.BOLD)
        self.assertNotEqual(node1, node2)

        node1 = TextNode("node", TextType.BOLD)
        node2 = TextNode("node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

        node1 = TextNode("node", TextType.CODE, None)
        node2 = TextNode("node", TextType.CODE, "https://www.boot.dev")
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
