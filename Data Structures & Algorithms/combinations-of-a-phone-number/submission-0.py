# int -> 3 or 4 chars mapping

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_groups = []
        for d in digits:
            adj = 1 if d in ['8', '9'] else 0
            start_letter = (ord(d) - ord('2')) * 3 + ord('a') + adj
            if d not in ['7', '9']:
                letter_groups.append([chr(start_letter), chr(start_letter + 1), chr(start_letter + 2)])
            else:
                letter_groups.append([chr(start_letter), chr(start_letter + 1), chr(start_letter + 2), chr(start_letter + 3)])

        idx = 0
        out = []
        for i in range(len(letter_groups)):
            curr_group = letter_groups[i]
            if i == 0:
                out.extend(curr_group)
            else:
                new_out = []
                for s in out:
                    for c in curr_group:
                        new_out.append(s + c)
                out = new_out

        return out
        