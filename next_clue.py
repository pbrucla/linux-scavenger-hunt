import os
import sys
import random
import hashlib
import generate_clues as gc
import subprocess as sp


def shell_out(comm):
    return sp.run(comm.split(), capture_output=True).stdout.decode()


def check_hint(clue, hint, dictionary):
    if clue == 3:
        count = len(os.listdir("/usr"))
        return int(hint) == count
    elif clue == 4:
        hostname = open("/etc/hostname", "r").read().strip()
        return hint == hostname
    elif clue == 5:
        return hint in ["i", "n", "-i", "-n"]
    elif clue == 6:
        return hint == os.getenv("PATH").split(":")[0]
    elif clue == 7:
        return hint == shell_out("which python").strip()
    elif clue == 8:
        return hint in ["accel"]
    elif clue == 9:
        val = shell_out(f"wc -l {dictionary}").split()[0]
        return hint == val
    elif clue == 10:
        return (
            hint == shell_out(f"grep -A 1 tactful {dictionary}").strip().split("\n")[1]
        )
    elif clue == 11:
        with open("README.md", "r") as f:
            return "cats are better than dogs" in "".join(f.readlines())
    elif clue == 12:
        if not hint.startswith("-"):
            return False
        if not ("k 5" in hint or "k5" in hint):
            return False
        if not "r" in hint:
            return False
        if not ("n" in hint or "g" in hint):
            return False
        return True


if __name__ == "__main__":

    if len(sys.argv) != 3:
        sys.exit("Need a clue number and hint")
    clue_number = int(sys.argv[1])
    hint = sys.argv[2]
    try:
        with open(".secret_number", "r") as f:
            secret_number = int("".join(f.readlines()))
    except:
        sys.exit("Generate the clues first!")

    clue_indexes = gc.gen_clue_list(
        gc.START_CLUE, gc.LAST_CLUE, gc.CLUE_SPACE, secret_number
    )
    dictionary = open("conf", "r").read().strip()

    if check_hint(clue_number, hint, dictionary):
        print(gc.zero_pad(clue_indexes[clue_number - gc.START_CLUE]))
    else:
        R = random.Random()
        if type(hint) == str:
            md5 = hashlib.md5(hint.encode())
            hint_number = int(md5.hexdigest(), 16)
        R.seed(secret_number + clue_number + hint_number)
        print(gc.zero_pad(R.randint(1, gc.CLUE_SPACE)))
