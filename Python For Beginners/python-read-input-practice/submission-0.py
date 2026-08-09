def add_two_numbers() -> int:
    test2 = 0
    test = input()
    two_numbers = test.split(",")

    two_numbers1 = [int(x) for x in two_numbers]
    for i in two_numbers1:
        test2 += i

    return test2



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
