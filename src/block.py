from enum import Enum
import re


class BlockTypes(Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split("\n\n")
    # print(f"\n{blocks}\n")
    blocks = map(lambda block: block.strip(), blocks)
    blocks = filter(lambda block: len(block) > 0, blocks)
    blocks = list(blocks)
    return blocks


# these checks start to become validation of the markdown; not doing it
# TODO: the instructions for OL say the numbers have to be in order
# TODO: quote, ul, ol, should match pattern each line in the block
def block_to_block_type(block: str) -> str:

    blockPatterns: dict[str, str] = {
        # heading can't be empty, it would be valid markdown and pass unit test
        # but the app strips blocks, so `# ` becomes `#` wich is a paragraph
        BlockTypes.HEAD.value: r"^#{1,6} (?=[\S])",
        # code was matching the entire string, I do not want that
        # BlockTypes.CODE: r"^```[\s\S]*?```$",
        # BlockTypes.CODE.value: r"^```(?=[\s\S]*?```$)",
        BlockTypes.CODE.value: r"`{3}([\S\s]*)\n`{3}",
        BlockTypes.QUOTE.value: r"^>",
        BlockTypes.UL.value: r"^[\*\-] +(?=[\S])",
        BlockTypes.OL.value: r"^\d*\. +(?=[\S])",
    }

    for pattern in blockPatterns.items():
        matches = re.findall(pattern[1], block, re.MULTILINE)
        if len(matches) > 0:
            # print(f"\n{matches}")
            return pattern[0]

    return "paragraph"


def main():
    print("you are not supposed to run this module")


if __name__ == "__main__":
    main()
