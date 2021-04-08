import random

times = int(input('How many quick picks?'))
for i in range(times):
    numbers = [random.randint(1, 45) for _ in range(6)]
    print(numbers)

    """"
    I try the best :(     
    """