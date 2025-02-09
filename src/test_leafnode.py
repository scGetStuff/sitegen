import unittest
from leafnode import LeafNode

to_html_tests = [
    {
        "args": ("p", "This is a paragraph of text."),
        "expected": "<p>This is a paragraph of text.</p>",
    },
    {
        "args": ("a", "Click me!", {"href": "https://www.google.com"}),
        "expected": '<a href="https://www.google.com">Click me!</a>',
    },
    {
        "args": (None, "raw text test"),
        "expected": "raw text test",
    },
]

to_html_errors = [
    {
        "args": ("p", None),
        "expected": ValueError,
    }
]


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        for test in to_html_errors:
            node = LeafNode(*test["args"])
            self.assertRaises(test["expected"], node.to_html)

        for test in to_html_tests:
            node = LeafNode(*test["args"])
            self.assertEqual(node.to_html(), test["expected"])


if __name__ == "__main__":
    unittest.main()
