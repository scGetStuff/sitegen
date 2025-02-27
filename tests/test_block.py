import unittest
from block import BlockTypes
from block import markdown_to_blocks as blockalizer
from block import block_to_block_type as getBlockType


blockalizer_tests = [
    {"markdown": "", "expected": []},
    {
        "markdown": (
            "# This is a heading\n"
            "\n"
            "   \n"
            "\n"
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n"
            "\n"
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item"
        ),
        "expected": [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            (
                "* This is the first list item in a list block\n"
                "* This is a list item\n"
                "* This is another list item"
            ),
        ],
    },
]

getBlockType_tests = [
    {
        "markdown": "# ",
        "expected": BlockTypes.PARA.value,
    },
    {
        "markdown": "# test",
        "expected": BlockTypes.HEAD.value,
    },
    {
        "markdown": "#### test",
        "expected": BlockTypes.HEAD.value,
    },
    {
        "markdown": "######## not head",
        "expected": BlockTypes.PARA.value,
    },
    {
        "markdown": "```\ncode()\n```",
        "expected": BlockTypes.CODE.value,
    },
    {
        "markdown": "```\ncode1()\ncode2()\ncode3()\n```",
        "expected": BlockTypes.CODE.value,
    },
    {
        "markdown": "```not code",
        "expected": BlockTypes.PARA.value,
    },
    {
        "markdown": "> one\n> two\n> three",
        "expected": BlockTypes.QUOTE.value,
    },
    {
        "markdown": ">",
        "expected": BlockTypes.QUOTE.value,
    },
    {
        "markdown": "* one\n- two",
        "expected": BlockTypes.UL.value,
    },
    {
        "markdown": "1. one\n2. two",
        "expected": BlockTypes.OL.value,
    },
]


class TestMain(unittest.TestCase):
    def test_blockalizer(self):
        for test in blockalizer_tests:
            self.assertEqual(blockalizer(test["markdown"]), test["expected"])

    def test_getBlockType(self):
        for test in getBlockType_tests:
            self.assertEqual(getBlockType(test["markdown"]), test["expected"])


if __name__ == "__main__":
    unittest.main()
