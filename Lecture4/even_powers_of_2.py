from math import pow

n = int(input())

for i in range(n+1):
        num = pow(2, i)
        if i % 2 == 0:

            print(int(num))
            i = i + 2
        else:
            i = i + 1