class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        out = []
        comb = []
        def create_comb_from_ith(i: int):
            if i >= len(digits):
                out.append("".join(comb))
                return
            
            curr_dig = digits[i]
            for letter in dig_map[curr_dig]:
                comb.append(letter)
                create_comb_from_ith(i + 1)
                comb.pop()
        
        create_comb_from_ith(0)
        return out
        