import unittest
from util import text_node_to_html_node as convert
from util import split_nodes_delimiter as spliter
from textnode import TextNode, TextType


convert_tests = [
    {
        "node": TextNode("raw text test", TextType.TEXT),
        "expected": "raw text test",
    },
    {
        "node": TextNode("bold text test", TextType.BOLD),
        "expected": "<b>bold text test</b>",
    },
    {
        "node": TextNode("italic text test", TextType.ITALIC),
        "expected": "<i>italic text test</i>",
    },
    {
        "node": TextNode("x = [1,2,3]", TextType.CODE),
        "expected": "<code>x = [1,2,3]</code>",
    },
    {
        "node": TextNode("Click me!", TextType.LINK, "https://www.google.com"),
        "expected": '<a href="https://www.google.com">Click me!</a>',
    },
    {
        "node": TextNode(
            "Click me!",
            TextType.IMAGE,
            "https://www.boot.dev/img/bootdev-logo-full-small.webp",
        ),
        "expected": '<img src="https://www.boot.dev/img/bootdev-logo-full-small.webp" alt="Click me!"></img>',
    },
]

convert_errors = [
    {
        "node": TextNode("error", None),
        "error": ValueError,
    },
    {
        "node": TextNode("error", ""),
        "error": ValueError,
    },
    {
        "node": TextNode("error", 1),
        "error": ValueError,
    },
]

spliter_tests = [
    {
        "nodes": [
            TextNode("This is text with a `code block` word", TextType.TEXT),
        ],
        "args": ("`", TextType.CODE),
        "out": [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ],
    },
    {
        "nodes": [
            TextNode("multiple **bold** words **test** thingy", TextType.TEXT),
        ],
        "args": ("**", TextType.BOLD),
        "out": [
            TextNode("multiple ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" words ", TextType.TEXT),
            TextNode("test", TextType.BOLD),
            TextNode(" thingy", TextType.TEXT),
        ],
    },
    {
        "nodes": [
            TextNode("*italic word* at the start", TextType.TEXT),
        ],
        "args": ("*", TextType.ITALIC),
        "out": [
            TextNode("italic word", TextType.ITALIC),
            TextNode(" at the start", TextType.TEXT),
        ],
    },
    {
        "nodes": [
            TextNode("This ends with a **bold word**", TextType.TEXT),
        ],
        "args": ("**", TextType.BOLD),
        "out": [
            TextNode("This ends with a ", TextType.TEXT),
            TextNode("bold word", TextType.BOLD),
        ],
    },
]


class TestMain(unittest.TestCase):
    def test_convert(self):
        for test in convert_errors:
            self.assertRaises(test["error"], convert, test["node"])

        for test in convert_tests:
            self.assertEqual(convert(test["node"]).to_html(), test["expected"])

    def test_spliter(self):
        for test in spliter_tests:
            self.assertEqual(spliter(test["nodes"], *test["args"]), test["out"])


if __name__ == "__main__":
    unittest.main()
