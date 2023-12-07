if __name__ == "__main__":
    # Part 1
    res1 = 1
    T1 = [35, 93, 73, 66]
    D1 = [212, 2060, 1201, 1044]
    for i, time in enumerate(T1):
        win = 0
        for speed in range(time):
            win += 1 if speed * (time - speed) > D1[i] else 0
        res1 *= win
    print(f"Result1:{res1}")

    # Part 2
    T2 = 35937366
    D2 = 212206012011044
    res2 = 0
    for speed in range(T2):
        if speed * (T2 - speed) > D2:
            res2 += 1

    print(f"Result2:{res2}")
