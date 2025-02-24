import unittest
from parentnode import ParentNode
from leafnode import LeafNode

# TODO: each class I've been improving the data driven test setup
# need to go back and refactor all

# TODO: nesting ParentNode objects


to_html_tests = [
    {
        "node": ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ),
        "expected": "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
    },
    {
        "node": ParentNode(
            "div",
            [
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
            ],
        ),
        "expected": "<div>Normal text<p><b>Bold text</b>Normal text</p></div>",
    },
    {
        "node": ParentNode(
            "div",
            [
                LeafNode(None, "div1"),
                ParentNode(
                    "div",
                    [
                        LeafNode(None, "div2"),
                        ParentNode(
                            "div",
                            [
                                LeafNode(None, "div3"),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        "expected": "<div>div1<div>div2<div>div3</div></div></div>",
    },
]

to_html_errors = [
    {
        "node": ParentNode(None, None),
        "expected": ValueError,
    },
    {
        "node": ParentNode("p", None),
        "expected": ValueError,
    },
]


class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        for test in to_html_errors:
            self.assertRaises(test["expected"], test["node"].to_html)

        for test in to_html_tests:
            self.assertEqual(test["node"].to_html(), test["expected"])


if __name__ == "__main__":
    unittest.main()
