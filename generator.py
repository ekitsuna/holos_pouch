from random import randint
import random

for i in range(10):
    with open(f"problems/november_contest/magical_wheat/testcases/in{i}.txt", "w") as file:
        a = randint(1, 1000)
        c = randint(1, 10000)
        if i <= 4:
            a = randint(1, 100)
            c = randint(1, 1000)

        field_length = abs(a - c) + 1
        
        file.write(f"{a} {c}\n")

        for j in range(a):
            uwu_factor = randint(2, min(field_length // 2, 100))
            target = randint(0, field_length)

            for k in range(field_length):
                if randint(1, uwu_factor) == 1 or k == target:
                    file.write("M")
                else:
                    file.write("W")
            file.write("\n")
            