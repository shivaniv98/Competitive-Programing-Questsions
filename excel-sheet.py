''' Problem Statement :
    You are given a string STR represinting column titles in excel sheet.
    Find its corresponding colmn number.
    Example:
    input - 
        3
        AZ
        COD
        ZZZ
    output - 
        52
        2422
        18278
    '''
def titleToNumber(a):
    alphaMap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    val = 0
    for s in range(len(a)):
        val = val+(26**(len(a)-s-1)*(alphaMap.index(a[s])+1))
    return val
count=input()
for i in range(int(count)):
    a = input()
    print(titleToNumber(a))


