import random

EuroMillionsNumbers = []
luckyStar = []

for i in range(0, 5):
    number = random.randint(1, 50)
    while number in EuroMillionsNumbers:
        number = random.randint(1, 50)
    EuroMillionsNumbers.append(number)

for it in range(0, 2):
    number1 = random.randint(1, 13)
    while number1 in luckyStar:
        number1 = random.randint(1, 13)
    luckyStar.append(number1)

EuroMillionsNumbers.sort()
luckyStar.sort()

print("Today's EuroMillions numbers are: ")
print(EuroMillionsNumbers)
print("Lucky Stars numbers are: ")
print(luckyStar)
