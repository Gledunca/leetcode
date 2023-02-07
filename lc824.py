class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = ""
        words = sentence.split(" ")
        i = 1
        for word in words:
            if word[0] in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
                word += "ma"
            else:
                word = word[1:] + word[0]
                word += "ma"
            word += "a"*i
            i += 1
            res += (word+" ")
        return res[:-1]
            