class LTestAlgo:
    """Recognizes for the language L = { 0 ^ n 1 ^ n | n >= 1} over the alphabet {0,1} """
    def check(self, word: str) -> bool:
        #check if word is empty
        if len(word) == 0:
            return False
        
        # check if the word contains only 0 and 1
        for char in word:
            if char not in ("0", "1"):
                return False
        
        # check if the word has the form 0^n 1^n
        seen_one = False
        count_0 = 0 
        count_1 = 0

        # check 
        for char in word:
            if char == "0":
                if seen_one:
                    return False
                count_0 += 1
            else:
                seen_one = True
                count_1 += 1
        if count_0 == count_1 and count_0 > 0:
            return True
        else:
            return False
        
# Tests
words = ["0011", "000111", "0101", "00011", "111000", "00110", "22212", ""]
l_test = LTestAlgo()
print("L-Test Algorithm")
for w in words:
    print(w, "->", l_test.check(w))