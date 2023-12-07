S = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


# THIS IS UGLY !!!!!!!!!! and to be rewritten !!!!!!!!!
def rank(hand, J=False):
    hand = list(hand)
    M = {}
    for c in hand:
        if c in M:
            M[c] += 1
        else:
            M[c] = 1
    if len(M) == 1:
        return 7
    elif len(M) == 2:
        for m in M.keys():
            if M.get(m) == 4:
                return 7 if J and "J" in M.keys() and m != "J" else 6
            if M.get(m) == 3:
                return 7 if J and "J" in M.keys() else 5
    elif len(M) == 3:
        if J and "J" in M.keys() and M.get("J") == 3:
            return 6
        if J and "J" in M.keys() and M.get("J") == 2:
            return 6
        for m in M.keys():
            if M.get(m) == 3:
                if J and "J" in M.keys() and M.get("J") and m != "J":
                    return 6
            if M.get(m) == 2:
                if J and "J" in M.keys() and M.get("J") and m != "J":
                    return 5
        for m in M.keys():
            if M.get(m) == 3:
                return 4
        for m in M.keys():
            if M.get(m) == 2:
                return 3
    elif len(M) == 4:
        if J and "J" in M.keys():
            return 4
        else:
            return 2
    return 2 if J and "J" in M.keys() else 1


def compare(hand1, hand2):
    for i in range(5):
        if S.get(hand1[i]) > S.get(hand2[i]):
            return True
        if S.get(hand1[i]) < S.get(hand2[i]):
            return False
    return False


if __name__ == "__main__":
    # Read inputs
    data, data2 = [], []
    lines = open("input.txt").read().split("\n")
    for i, line in enumerate(lines):
        if line:
            card, score = line.split(" ")
            data.append((rank(card), card, score))
            data2.append((rank(card, J=True), card, score))

    # Part 1
    print(S)
    tmp = data[:]
    i, res1 = 0, 0
    while tmp:
        i += 1
        cur = 0
        for c in range(len(tmp)):
            if tmp[cur][0] > tmp[c][0]:
                cur = c
            if tmp[cur][0] == tmp[c][0] and compare(tmp[cur][1], tmp[c][1]):
                cur = c
        res1 += i * int(tmp.pop(cur)[2])

    # Part 2
    S["J"] = 1
    print(S)
    tmp = data2[:]
    i, res2 = 0, 0
    while tmp:
        i += 1
        cur = 0
        for c in range(len(tmp)):
            if tmp[cur][0] > tmp[c][0]:
                cur = c
            elif tmp[cur][0] == tmp[c][0] and compare(tmp[cur][1], tmp[c][1]):
                cur = c
        res2 += i * int(tmp.pop(cur)[2])

    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
