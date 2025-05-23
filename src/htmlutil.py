# had to change the file name, html is a built-in
from block import BlockTypes
from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode
from block import markdown_to_blocks as blockalizer
from block import block_to_block_type as getBlockType
from text import text_to_textnodes
from text import text_node_to_html_node


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = blockalizer(markdown)
    root = ParentNode("div", [])

    for block in blocks:
        type = getBlockType(block)
        node = convertBlock(block, type)
        root.children.append(node)

    return root


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


def parseInline(text: str):
    leafs = []
    textNodes = text_to_textnodes(text)
    # print(textNodes)

    for node in textNodes:
        leafs.append(text_node_to_html_node(node))

    return leafs


def makeHeading(block: str) -> ParentNode:
    parts = block.split(" ", 1)
    x = len(parts[0])
    text = parts[1] if len(parts) > 1 else ""
    leafs = parseInline(text)
    node = ParentNode(f"h{x}", leafs)

    return node


def makeParagraph(block: str) -> LeafNode:
    leafs = parseInline(block)
    node = ParentNode("p", leafs)

    return node


def makeCode(block: str) -> ParentNode:
    text = block[3:-3]
    code = LeafNode("code", text)
    pre = ParentNode("pre", [code])

    return pre


def makeQuote(block: str) -> ParentNode:
    block = block.replace("\n", "")
    block = block.replace(">", "")
    block = block.strip()
    # print(block)

    leafs = parseInline(block)
    blockQuote = ParentNode("blockquote", leafs)

    return blockQuote


def makeUL(block: str) -> ParentNode:
    lines = block.split("\n")
    ul = ParentNode("ul", [])

    for line in lines:
        leafs = parseInline(line[2:])
        li = ParentNode("li", leafs)
        ul.children.append(li)

    return ul


def makeOL(block: str) -> ParentNode:
    lines = block.split("\n")
    ol = ParentNode("ol", [])

    for line in lines:
        # could be arbitrary number of digits starting line
        parts = line.split(" ", 1)
        words = parts[1] if len(parts) > 1 else ""
        leafs = parseInline(words)
        li = ParentNode("li", leafs)
        ol.children.append(li)

    return ol


def main():
    print("\nyou are not supposed to run this module\n")

    # s = "> test"
    # out = markdown_to_html_node(s)
    # print(out.to_html())


if __name__ == "__main__":
    main()
