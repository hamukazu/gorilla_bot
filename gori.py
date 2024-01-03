import random


def gori():
    s = ""
    sep = False
    beg = True
    while len(s) < 120:
        if beg:
            s += "ウ"
            s += ["ホ", "ホッ"][random.randrange(2)]
            beg = False
        if sep:
            s += "、"
            sep = False
            beg = True
        else:
            if random.randrange(10) == 0:
                sep = True
            else:
                s += ["ホ", "ホッ"][random.randrange(2)]
                if random.randrange(5) == 0:
                    beg = True
    return s


if __name__ == "__main__":
    print(gori())
