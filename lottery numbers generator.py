import random


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

    return EuroMillionsNumbers, luckyStar


print(lottery())
