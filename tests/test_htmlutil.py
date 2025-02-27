import unittest
from htmlutil import markdown_to_html_node as mdToNode


mdToNode_tests = [
    {
        "markdown": "",
        "html": "<div></div>",
    },
    {
        "markdown": "#### test",
        "html": "<div><h4>test</h4></div>",
    },
    {
        "markdown": "a paragraph of text\nline2",
        "html": "<div><p>a paragraph of text\nline2</p></div>",
    },
    {
        "markdown": "```\ncode1()\ncode2()\ncode3()\n```",
        "html": "<div><pre><code>\ncode1()\ncode2()\ncode3()\n</code></pre></div>",
    },
    {
        "markdown": "> one\n> two\n> three",
        "html": "<div><blockquote>one two three</blockquote></div>",
    },
    {
        "markdown": (
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item"
        ),
        "html": "<div><ul><li>This is the first list item in a list block</li><li>This is a list item</li><li>This is another list item</li></ul></div>",
    },
    {
        "markdown": "1. one\n" "2. two\n" "3. three",
        "html": "<div><ol><li>one</li><li>two</li><li>three</li></ol></div>",
    },
]


class TestMain(unittest.TestCase):
    def test_mdToNode(self):
        for test in mdToNode_tests:
            node = mdToNode(test["markdown"])
            self.assertEqual(node.to_html(), test["html"])


if __name__ == "__main__":
    unittest.main()
