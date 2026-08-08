def first_n_characters(s: str, n: int) -> str:
    stest = s[:n]
    return stest

def last_n_characters(s: str, n: int) -> str:
    stester = s[-n:]
    return stester


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
