alps=list(map(chr,range(97,123)))
alpC=list(map(chr,range(65,91)))
def enc(str):
    res=''
    for i in str:
        if i.isalpha():
            if i.isupper():
                res+=alpC[(alpC.index(i)+3)%26]
            else:
                res+=alps[(alps.index(i)+3)%26]
        else:
            res+=i
    return res
def dec(str):
    res=''
    for i in str:
        if i.isalpha():
            if i.isupper():
                res+=alpC[(alpC.index(i)-3)%26]
            else:
                res+=alps[(alps.index(i)-3)%26]
        else:
            res+=i
    return res
