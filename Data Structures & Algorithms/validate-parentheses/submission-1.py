class Solution:
    def isValid(self, s: str) -> bool:
        stackk = list()
        for i in s:
            if i in ["[","{","("]:
                stackk.append(i)
            else:
                if len(stackk)==0:
                    return False
                elif i == ")" and stackk[-1]!="(":
                    return False
                elif i == "]" and stackk[-1]!="[":
                    return False
                elif i == "}" and stackk[-1]!="{":
                    return False
                stackk=stackk[:len(stackk)-1]
        if len(stackk)==0:
            return True
        else:
            return False



        