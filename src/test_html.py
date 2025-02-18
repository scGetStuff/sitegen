import unittest
from html import markdown_to_html_node as mdToNode


mdToNode_tests = [
    {
        "markdown": "",
        "html": "",
    },
    {
        "markdown": "# test",
        "html": "<h1>test</h1>",
    },
    # {
    #     "markdown": (
    #         "# This is a heading\n"
    #         "\n"
    #         "   \n"
    #         "\n"
    #         "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"
    #         "\n"
    #         "* This is the first list item in a list block\n"
    #         "* This is a list item\n"
    #         "* This is another list item"
    #     ),
    #     "html": [
    #         "# This is a heading",
    #         "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
    #         (
    #             "* This is the first list item in a list block\n"
    #             "* This is a list item\n"
    #             "* This is another list item"
    #         ),
    #     ],
    # },
]


class TestMain(unittest.TestCase):
    def test_mdToNode(self):
        for test in mdToNode_tests:
            self.assertEqual(mdToNode(test["markdown"]), test["html"])


if __name__ == "__main__":
    unittest.main()
