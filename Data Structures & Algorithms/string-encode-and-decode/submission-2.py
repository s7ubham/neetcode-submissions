class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=i
            s+="kuchbhi"
        return s
    def decode(self, s: str) -> List[str]:
        return list(map(str,s.split("kuchbhi")))[:-1]
