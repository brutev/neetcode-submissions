def remove_fourth_character(word: str) -> str:
    word1 = word[0:3]
    word2 = word[4:]
    result = word1 + word2

    return result


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
