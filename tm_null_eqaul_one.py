def tm_null_equal_one(word: str) -> bool:
    count_0 = 0
    count_1 = 0
    for char in word:
        if char == "0":
            count_0 += 1
        elif char == "1":
            count_1 += 1
        else: 
            return False
    return count_0 == count_1

word1 = "0011"     # -> True
word2 = "010101"   # -> True
word3 = "001111"   # -> False
word4 = "00211"    # -> False 
words = ["0011", "010101", "001111", "00211"]
for w in words:
    print(w, "->", tm_null_equal_one(w))

