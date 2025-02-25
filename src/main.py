import os
import shutil
import re
from block import markdown_to_blocks as blockalizer
from htmlutil import markdown_to_html_node as mdToNode

INPUTFILE = "content/index.md"
INPUT = "content"
TEMPLATE = "template.html"
STATIC = "static"
OUT = "public"


def main():
    print("Build a Static Site Generator")

    copyAllFiles(STATIC, OUT)
    # generate_page(INPUTFILE, TEMPLATE, OUT)
    generate_pages_recursive(INPUT, TEMPLATE, OUT)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    if os.path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, dest_dir_path)
        return

    content = os.listdir(dir_path_content)
    # print(f"DIR: {dir_path_content}\n{content}")
    for thing in content:
        src = os.path.join(dir_path_content, thing)
        dest = dest_dir_path

        # create the sub-dir in output location
        if not os.path.isfile(src):
            dest = os.path.join(dest_dir_path, thing)
            if not os.path.exists(dest):
                os.mkdir(dest)

        # print(f"\nFROM: {src}\nTO: {dest}")
        generate_pages_recursive(src, template_path, dest)


def generate_page(from_path, template_path, dest_path):
    print(
        f"Generating page from '{from_path}' to '{dest_path}' using '{template_path}'"
    )

    templateHTML = getFileText(template_path)
    # print(templ)
    markdown = getFileText(from_path)
    # print(markdown)
    title = extract_title(markdown)
    # print(title)
    htmlContent = mdToNode(markdown).to_html()
    # print(html)
    htmlFileName = getHTMLFileName(from_path)
    # print(htmlName)
    newContent = templateHTML.replace("{{ Title }}", title)
    newContent = newContent.replace("{{ Content }}", htmlContent)
    # print(newContent)
    isGood = writeOut(dest_path, htmlFileName, newContent)
    print(f"It did good stuff: {isGood}")


def getHTMLFileName(filePath: str):
    fileName = os.path.split(filePath)[1]
    parts = fileName.split(".")
    parts[len(parts) - 1] = "html"
    htmlName = ".".join(parts)

    return htmlName


def writeOut(dir, fileName: str, htmlContent: str) -> str:
    file = os.path.join(dir, fileName)
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
