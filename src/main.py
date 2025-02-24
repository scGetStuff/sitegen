import os
import shutil
import re
from block import markdown_to_blocks as blockalizer
from htmlutil import markdown_to_html_node as mdToNode

INPUTFILE = "content/index.md"
TEMPLATE = "template.html"
STATIC = "static"
OUT = "public"


def main():
    print("Build a Static Site Generator")

    copyAllFiles(STATIC, OUT)
    generate_page(STATIC, TEMPLATE, OUT)


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'"
    )

    templ = getFileText(TEMPLATE)
    # print(templ)
    markdown = getFileText(INPUTFILE)
    # print(markdown)
    title = extract_title(markdown)
    # print(title)
    htmlContent = mdToNode(markdown).to_html()
    # print(html)
    htmlName = getOutName(INPUTFILE)
    # print(htmlName)
    newContent = templ.replace("{{ Title }}", title)
    newContent = templ.replace("{{ Content }}", htmlContent)
    # print(newContent)
    isGood = writeOut(htmlName, newContent)
    print(f"It did good stuff: {isGood}")


def getOutName(filePath: str):
    fileName = os.path.split(filePath)[1]
    parts = fileName.split(".")
    parts[len(parts) - 1] = "html"
    htmlName = ".".join(parts)

    return htmlName


def writeOut(fileName: str, htmlContent: str) -> str:
    file = os.path.join(OUT, fileName)
    # print(file)
    count = 0

    with open(file, "w") as f:
        count = f.write(htmlContent)

    return count == len(htmlContent)


def getFileText(file: str) -> str:
    text = ""
    with open(file) as f:
        text = f.read()

    return text


def extract_title(markdown: str) -> str:
    blocks = blockalizer(markdown)
    if len(blocks) < 1:
        raise Exception("missing header")
    firstLine = blocks[0]

    pattern = r"^# (?=[\S])"
    matches = re.findall(pattern, firstLine)
    # print(f"\nMATCHES: {len(matches)}")
    if len(matches) < 1:
        raise Exception("missing header")

    return firstLine[2:]


def copyAllFiles(fromDir: str, toDir: str):

    if os.path.exists(toDir):
        shutil.rmtree(toDir)

    copyThing(fromDir, toDir)


def copyThing(fromThing: str, toThing: str):

    if os.path.isfile(fromThing):
        shutil.copy(fromThing, toThing)
        # print(f"FILE: {fromThing}")
        return

    os.mkdir(toThing)
    content = os.listdir(fromThing)
    # print(f"DIR: {fromThing}\n{content}")

    for thing in content:
        src = os.path.join(fromThing, thing)
        dest = os.path.join(toThing, thing)
        # print(f"\nFROM: {src}\nTO: {dest}")
        copyThing(src, dest)


if __name__ == "__main__":
    main()
