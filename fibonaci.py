def fiboanacci(number):         # 0,1,1,2,3,5,8,13,21,34.... the value of the next number is the sum of the last two numbers
    a,b = 0,1                   # we start with 0 and 1
    for i in range(number):     # for every number in range of numbers
        yield a                 # repeat a
        temp = a                # create new variable to store the value of a
        a = b                   # now we want a to get the value of b
        b = temp + b            # and b to get the value of the last tow numbers

for x in fiboanacci(10):        # now call the fibonacci function and print every number forom the range
    print(x)