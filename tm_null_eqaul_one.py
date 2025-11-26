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


class TMNullEqualOne:
    

    def __init__(self):
       
        self.count_0 = 0
        self.count_1 = 0

    def check(self, word: str) -> bool:
       
        self.count_0 = 0
        self.count_1 = 0

        for char in word:
            if char == "0":
                self.count_0 += 1
            elif char == "1":
                self.count_1 += 1
            else:
                return False
        return self.count_0 == self.count_1


# Tests
word1 = "0011"     # -> True
word2 = "010101"   # -> True
word3 = "001111"   # -> False
word4 = "00211"    # -> False

words = [word1, word2, word3, word4]

tm = TMNullEqualOne()

print("Class")
for w in words:
    print(w, "->", tm.check(w))

print("-----------------------------------")

print("Function")
for w in words:
    print(w, "->", tm_null_equal_one(w))
