class Solution:

    def encode(self, strs: List[str]) -> str:
        return " ".join(strs)

    def decode(self, s: str) -> List[str]:
        if not s:
            return [""]
        return s.split(" ")