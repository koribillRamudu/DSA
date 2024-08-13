def reverseWord(self, str: str) -> str:
    #your code here
    # return str[::-1]
    s=""
    for i in range(len(str)-1,-1,-1):
        s=s+str[i]
    return s