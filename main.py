import random
import decimal


def normalfib():
    num1 = 0
    num2 = 1
    num3 = 0
    z = 0
    while z < 1000:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        z += 1
        print("Number:\t" + str(num3))
        print("Ratio:\t" + str(num3 / num1))


def randomfib():
    num1 = 0
    num2 = 1
    num3 = 0
    P = []
    z = 0
    while z < 100000:
        if random.randint(0, 1) == 0:
            num3 = num2 + num1
            num1 = num2
            num2 = num3
        else:
            num3 = num2 - num1
            num1 = num2
            num2 = num3

        z += 1
        if num1 !=0:
            P.append(num3/num1)
            #print("Number:\t" + str(num3))
            #print("Ratio:\t" + str(num3 / num1))
            print(sum(P)/z)


randomfib()
