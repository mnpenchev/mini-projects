import random

guess = [[11, 22, 33, 44, 50], [1, 12]]


def lottery():
    EuroMillionsNumbers = []
    for i in range(0, 5):
        number = random.randint(1, 50)
        while number in EuroMillionsNumbers:
            number = random.randint(1, 50)
        EuroMillionsNumbers.append(number)
        EuroMillionsNumbers.sort()

    luckyStar = []
    for j in range(0, 2):
        number1 = random.randint(1, 12)
        while number1 in luckyStar:
            number1 = random.randint(1, 12)
        luckyStar.append(number1)
        luckyStar.sort()

    result = [EuroMillionsNumbers, luckyStar]
    return result


count = 0
while True:
    if guess == lottery():
        print("YOU HAVE WON THE LOTTERY !!! ", count, lottery())
        break
    else:
        count += 1
        print(count, lottery())
