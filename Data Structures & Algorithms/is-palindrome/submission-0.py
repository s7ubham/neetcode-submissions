class Solution:
    def isPalindrome(self, ss: str) -> bool:
        s=[]
        for i in ss:
            if i.isalnum():
                s.append(i)
        n=len(s)
        print(s)
        for i in range(n//2):
            if s[i].lower()!=s[n-i-1].lower():
                return False
        return True
        