import os
import shutil


def main():
    print("Build a Static Site Generator")
    copyAllFiles("static", "public")


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
