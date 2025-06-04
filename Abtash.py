alps=list(map(chr,range(97,123)))
alpC=list(map(chr,range(65,91)))
def enc(str):
    res=''
    for char in str:
        if char.isalpha():
            if char.isupper():
                res+=alpC[25-alpC.index(char)]
            else:
                res+=alps[25-alps.index(char)]
        else:
            res+=char
    return res
def dec(str):
    return enc(str) 
'''
    it's literally just reversing the alphabets, so I don't think I need a brand new logic for this one.
'''