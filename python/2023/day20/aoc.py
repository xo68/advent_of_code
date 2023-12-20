if __name__ == "__main__":
    res1, res2 = 0, 0
    LOW, HIGH = 1, 2

    # Read the inputs
    evt = {}
    lines = open("input.txt").read().strip().split("\n")
    for line in lines:
        if "broadcaster" in line:
            name, targets = line.split(" -> ")
            targets = targets.split(", ")
            evt[name] = ["0", False, targets, {}]
        else:
            t = line[0]
            name, targets = line[1:].split(" -> ")
            targets = targets.split(", ")
            evt[name] = [t, False, targets, {}]

    # Add Conjunction module inputs
    # Default is low pulse for each input
    for e1 in evt:
        if evt[e1][0] == "&":
            for e2 in evt:
                if e1 in evt[e2][2]:
                    evt[e1][3][e2] = LOW

    LP, HP = 0, 0
    for _ in range(1000):
        LP += 1
        signal = LOW
        next = [("broadcaster", LOW, evt["broadcaster"][2])]
        while next:
            dst = next[:]
            next = []

            for i, d in enumerate(dst):
                src = dst[i][0]
                sig = dst[i][1]
                if sig == LOW:
                    LP += len(dst[i][2])
                else:
                    HP += len(dst[i][2])

                for name in dst[i][2]:
                    if name not in evt.keys():
                        continue
                    signal = sig

                    # 0: Type; 1: On/Off; 2: list of destinations
                    # Flip / Flop -> High pulse, nothing happen
                    if evt[name][0] == "%":
                        if signal == LOW:
                            if evt[name][1] is False:
                                evt[name][1] = True
                                signal = HIGH
                                # From , signal, targets
                            else:
                                evt[name][1] = False
                                signal = LOW
                            next.append((name, signal, evt[name][2]))

                    # Conjunction
                    if evt[name][0] == "&":
                        # Store the current signal
                        if signal == LOW:
                            evt[name][3][src] = LOW
                        else:
                            evt[name][3][src] = HIGH

                        pulse = HIGH
                        for p in evt[name][3]:
                            if evt[name][3][p] == LOW:
                                pulse = LOW
                                break
                        if pulse == HIGH:
                            signal = LOW
                        else:
                            signal = HIGH

                        next.append((name, signal, evt[name][2]))

    res1 = LP * HP
    print(f"Result1:{res1}")
    print(f"Result2:{res2}")
