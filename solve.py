for i in range(10):
    with open (f"problems/november_contest/magical_wheat/testcases/in{i}.txt", "r") as file:
        a, c = map(int, file.readline().split())
        wheats = []
        for j in range(a):
            wheats.append(file.readline().count('M'))
        wheats.sort()
        wheats.reverse()

        total = 0
        count = 0
        for w in wheats:
            total += w
            count += 1
            if total >= c:
                break
        if total < c:
            count = -1

        with open (f"problems/november_contest/magical_wheat/testcases/out{i}.txt", "w") as output:
            output.write(f"{count}\n")