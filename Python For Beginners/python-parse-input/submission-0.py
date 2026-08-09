from typing import List

def read_integers() -> List[int]:
    int_list = input()
    list_int = int_list.split(",")
    return [int(x) for x in list_int]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
