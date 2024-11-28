from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        strs[1]
        return ' '.join(s.replace(" ", "#") for s in strs)
    def decode(self, s: str) -> List[str]:
        return [p.replace("#"," ") for p in s.split(" ")]
