numbers = [3, 1, 4, 1, 5, 9, 2]
""""
numbers[0] #3
numbers[-1] #2
numbers[3] #1
numbers[:-1] # 314159
numbers[3:4] # [3] not so sure :(  Ok actually is 1
5 in numbers #5
7 in numbers #2
"3" in numbers  #1
numbers + [6, 5, 3] #[3,1,4,1,5,9,2,6,5,3]
"""
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])


def main():
    numbers[0] = 'ten'
    print(numbers)
    numbers[-1] = 1
    print(numbers[2:])
    if numbers.count(9) > 0:
        print('Yes there is a 9')


main()