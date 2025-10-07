#!/usr/bin/env python3

import os
import sys
import random
from shutil import rmtree


START_CLUE = 2
LAST_CLUE = 13
CLUE_SPACE = 100000
FIRST_CLUE = 12345


def zero_pad(clue):
    l = len(str(clue))
    m = len(str(CLUE_SPACE)) - 1
    if l < m:
        return "0" * (m - l) + str(clue)
    else:
        return str(clue)


def gen_clue_list(first, last, space, secret):
    R = random.Random()
    R.seed(secret)
    clue_indexes = []
    for i in range(first, last + 1):
        clue_indexes.append(R.randint(1, space))
    clue_indexes[0] = FIRST_CLUE
    return clue_indexes


if __name__ == "__main__":

    # Install dependencies
    try:
        print("Installing dependencies (this may take a while)...\n\n")
        import time
        time.sleep(1)
        import subprocess
        subprocess.run(["sudo", "apt", "install", "-y", "wamerican", "man-db"], check=True)
        subprocess.run(["sudo", "unminimize"], check=True)
    except:
        pass
    print("Done!")

    try:
        print("Found existing scavenger hunt - updating clues...")
        try:
            rmtree("clues")
        except:
            pass
        with open(".secret_number", "r") as f:
            secret_number = int(f.read())

    except:

        if len(sys.argv) != 2:
            sys.exit("Need a secret number - run like python generate_clues.py NUMBER")
        secret_number = int(sys.argv[1])

    try:
        val = open("conf", "r").read().strip()
        words = open(val, "r").read().strip()
    except FileNotFoundError:
        sys.exit("Unable to locate dictionary file. Please contact the instructors for support.")

    try:
        os.stat("clues")
    except FileNotFoundError:
        os.mkdir("clues")

    clue_indexes = gen_clue_list(START_CLUE, LAST_CLUE, CLUE_SPACE, secret_number)

    template_names = os.listdir(".clue-templates")
    template_names.sort()
    template_data = []

    for t in template_names:
        if t == "NO PEEKING":
            continue
        data = open(".clue-templates/" + t, "r").read()
        template_data.append(data)

    print("Hiding clues (this may take a couple minutes)...")
    for i in range(0, CLUE_SPACE):
        if i % 5000 == 0:
            print(f"{i // 1000}% done...")
        dir_name = "clues/" + "0" * (len(str(CLUE_SPACE)) - 1 - len(str(i))) + str(i)
        os.mkdir(dir_name)
        file_name = open(dir_name + "/clue", "w")
        if i not in clue_indexes:
            file_name.write("Nothing to see here.\n")
        else:

            template_index = clue_indexes.index(i)

            if template_index < len(template_data):
                # All templates are self-contained, no formatting needed
                file_name.write(template_data[template_index])
            else:
                file_name.write("Clue: \n")

    with open(".secret_number", "w") as f:
        f.write(str(secret_number))

    print("Done hiding clues.")
