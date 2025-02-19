# had to change the file name, html is a built-in
from block import BlockTypes
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode
from block import markdown_to_blocks as blockalizer
from block import block_to_block_type as getBlockType


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = blockalizer(markdown)
    root = ParentNode("div", [])

    for block in blocks:
        type = getBlockType(block)
        node = convertBlock(block, type)
        root.children.append(node)

    return root


# TODO: I did this wrong
# all of the blocks need to be parsed into textnodes, then htmlnodes
# paragraph is a lie, it is a block of text that needs to be parsed
def convertBlock(block: str, type: str) -> HTMLNode:
    match type:
        case BlockTypes.HEAD.value:
            return makeHeading(block)
        case BlockTypes.PARA.value:
            return makeParagraph(block)
        case BlockTypes.CODE.value:
            return makeCode(block)
        case BlockTypes.QUOTE.value:
            return makeQuote(block)
        case BlockTypes.UL.value:
            return makeUL(block)
        case BlockTypes.OL.value:
            return makeOL(block)
        case _:
            raise Exception("bad block type")


def makeHeading(block) -> LeafNode:
    parts = block.split(" ", 1)
    x = len(parts[0])
    words = parts[1] if len(parts) > 1 else ""
    node = LeafNode(f"h{x}", words)
    return node


def makeParagraph(block) -> LeafNode:
    node = LeafNode("p", block)
    return node


def makeCode(block) -> ParentNode:
    text = block[3:-3]
    code = LeafNode("code", text)
    pre = ParentNode("pre", [code])
    return pre


def makeQuote(block) -> ParentNode:
    lines = block.split("\n")

    blockQuote = ParentNode("blockquote", [])
    for line in lines:
        quote = LeafNode("p", line[1:])
        blockQuote.children.append(quote)

    return blockQuote


def makeUL(block) -> LeafNode:
    lines = block.split("\n")

    ul = ParentNode("ul", [])
    for line in lines:
        li = LeafNode("li", line[2:])
        ul.children.append(li)

    return ul


def makeOL(block) -> LeafNode:
    lines = block.split("\n")

    ol = ParentNode("ol", [])
    for line in lines:
        # could be arbitrary number of digits starting line
        parts = line.split(" ", 1)
        words = parts[1] if len(parts) > 1 else ""
        li = LeafNode("li", words)
        ol.children.append(li)

    return ol


def main():
    print("you are not supposed to run this module")

    s = "1. one\n" "2. two\n" "3. three"

    out = markdown_to_html_node(s)
    print(out.to_html())


if __name__ == "__main__":
    main()
