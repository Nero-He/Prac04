def main():
    numbers = []
    for i in range(5):
        enter = int(input("Please enter 5 times of numbers: "))
        numbers.append(enter)
    print('The first number is', numbers[0])
    print('The last number is', numbers[4])
    print('The smallest number is', min(numbers))
    print('The largest number is', max(numbers))
    b = len(numbers)
    total = 0
    for i in numbers:
        total = total + i
        print('The average of the numbers is', total/b)
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    name = float(input('Please enter your username: '))
    if name in usernames:
        print("Access granted! Welcome Back! {}".format(name))
    else:
        print("Access denied!")


main()