import unittest
from text import text_node_to_html_node as convert
from text import split_nodes_delimiter as spliter
from text import extract_markdown_images as parseImages
from text import extract_markdown_links as parseLinks
from text import split_nodes_image as splitImage
from text import split_nodes_link as splitLink
from text import text_to_textnodes as toTextNodes
from textnode import TextNode, TextType


convert_tests = [
    {
        "node": TextNode("", TextType.TEXT),
        "expected": "",
    },
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
            TextNode("", TextType.TEXT),
        ],
        "args": ("`", TextType.CODE),
        "expected": [],
    },
    {
        "nodes": [
            TextNode("nothing", TextType.TEXT),
        ],
        "args": ("`", TextType.CODE),
        "expected": [
            TextNode("nothing", TextType.TEXT),
        ],
    },
    {
        "nodes": [
            TextNode("This is text with a `code block` word", TextType.TEXT),
        ],
        "args": ("`", TextType.CODE),
        "expected": [
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
        "expected": [
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
        "expected": [
            TextNode("italic word", TextType.ITALIC),
            TextNode(" at the start", TextType.TEXT),
        ],
    },
    {
        "nodes": [
            TextNode("italic _word_ using underscore", TextType.TEXT),
        ],
        "args": ("_", TextType.ITALIC),
        "expected": [
            TextNode("italic ", TextType.TEXT),
            TextNode("word", TextType.ITALIC),
            TextNode(" using underscore", TextType.TEXT),
        ],
    },
    {
        "nodes": [
            TextNode("This ends with a **bold word**", TextType.TEXT),
        ],
        "args": ("**", TextType.BOLD),
        "expected": [
            TextNode("This ends with a ", TextType.TEXT),
            TextNode("bold word", TextType.BOLD),
        ],
    },
]

parseImages_tests = [
    {
        "text": "This is text with no images",
        "expected": [],
    },
    {
        "text": "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        "expected": [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ],
    },
    {
        "text": "![?/\\.,&%$#@(i](https://i.imgur.com/aKaOqIh.gif)",
        "expected": [
            ("?/\\.,&%$#@(i", "https://i.imgur.com/aKaOqIh.gif"),
        ],
    },
]

parseLinks_tests = [
    {
        "text": "This is text with no links",
        "expected": [],
    },
    {
        "text": "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        "expected": [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ],
    },
    {
        "text": "[?/\\.,&%$#@d)](https://www.boot.dev)",
        "expected": [
            ("?/\\.,&%$#@d)", "https://www.boot.dev"),
        ],
    },
]

splitImages_tests = [
    {
        "nodes": [
            TextNode("", TextType.TEXT),
        ],
        "expected": [],
    },
    {
        "nodes": [
            TextNode("not an image", TextType.TEXT),
        ],
        "expected": [
            TextNode("not an image", TextType.TEXT),
        ],
    },
    {
        "nodes": [
            TextNode("![rick roll](https://i.imgur.com/aKaOqIh.gif)", TextType.TEXT)
        ],
        "expected": [
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
        ],
    },
    {
        "nodes": [
            TextNode(
                "leading text ![rick roll](https://i.imgur.com/aKaOqIh.gif)",
                TextType.TEXT,
            )
        ],
        "expected": [
            TextNode("leading text ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
        ],
    },
    {
        "nodes": [
            TextNode(
                "![rick roll](https://i.imgur.com/aKaOqIh.gif) trailing text",
                TextType.TEXT,
            )
        ],
        "expected": [
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" trailing text", TextType.TEXT),
        ],
    },
    {
        "nodes": [
            TextNode(
                "leading text ![rick roll](https://i.imgur.com/aKaOqIh.gif) multiple images ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) trailing text",
                TextType.TEXT,
            )
        ],
        "expected": [
            TextNode("leading text ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" multiple images ", TextType.TEXT),
            TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" trailing text", TextType.TEXT),
        ],
    },
]

splitLinks_tests = [
    {
        "nodes": [
            TextNode("", TextType.TEXT),
        ],
        "expected": [],
    },
    {
        "nodes": [
            TextNode("not an link", TextType.TEXT),
        ],
        "expected": [
            TextNode("not an link", TextType.TEXT),
        ],
    },
    {
        "nodes": [TextNode("[to boot dev](https://www.boot.dev)", TextType.TEXT)],
        "expected": [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ],
    },
    {
        "nodes": [
            TextNode("leading text [to boot dev](https://www.boot.dev)", TextType.TEXT)
        ],
        "expected": [
            TextNode("leading text ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        ],
    },
    {
        "nodes": [
            TextNode("[to boot dev](https://www.boot.dev) trailing text", TextType.TEXT)
        ],
        "expected": [
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" trailing text", TextType.TEXT),
        ],
    },
    {
        "nodes": [
            TextNode(
                "leading text [to boot dev](https://www.boot.dev) multiple links [to youtube](https://www.youtube.com/@bootdotdev) trailing text",
                TextType.TEXT,
            )
        ],
        "expected": [
            TextNode("leading text ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" multiple links ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
            TextNode(" trailing text", TextType.TEXT),
        ],
    },
]

toTextNodes_tests = [
    {
        "text": "",
        "expected": [],
    },
    {
        "text": "stuff",
        "expected": [
            TextNode("stuff", TextType.TEXT),
        ],
    },
    {
        "text": "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
        "expected": [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
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
            self.assertEqual(spliter(test["nodes"], *test["args"]), test["expected"])

    def test_parseImages(self):
        for test in parseImages_tests:
            self.assertEqual(parseImages(test["text"]), test["expected"])

    def test_parseLinks(self):
        for test in parseLinks_tests:
            self.assertEqual(parseLinks(test["text"]), test["expected"])

    def test_splitImages(self):
        for test in splitImages_tests:
            self.assertEqual(splitImage(test["nodes"]), test["expected"])

    def test_splitLinks(self):
        for test in splitLinks_tests:
            self.assertEqual(splitLink(test["nodes"]), test["expected"])

    def test_to_textnodes(self):
        for test in toTextNodes_tests:
            self.assertEqual(toTextNodes(test["text"]), test["expected"])


if __name__ == "__main__":
    unittest.main()
