import unittest
from leafnode import LeafNode

to_html_tests = [
    {
        "node": LeafNode("p", "This is a paragraph of text."),
        "expected": "<p>This is a paragraph of text.</p>",
    },
    {
        "node": LeafNode("a", "Click me!", {"href": "https://www.google.com"}),
        "expected": '<a href="https://www.google.com">Click me!</a>',
    },
    {
        "node": LeafNode(None, "raw text test"),
        "expected": "raw text test",
    },
]

to_html_errors = [
    {
        "node": LeafNode("p", None),
        "expected": ValueError,
    }
]


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        for test in to_html_errors:
            self.assertRaises(test["expected"], test["node"].to_html)

        for test in to_html_tests:
            self.assertEqual(test["node"].to_html(), test["expected"])


if __name__ == "__main__":
    unittest.main()
