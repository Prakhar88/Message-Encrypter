alps=list(map(chr,range(97,123)))
alpC=list(map(chr,range(65,91)))
def txt_only(txt):
    res=''
    for i in txt:
        if i.isalpha():
            res+=i
    return res
def back_to_normal(org,enc):
    n,m=0,0
    res=''
    while True:
        if org[n].isalpha():
            res+=enc[m]
            m+=1
        else:
            res+=org[n]
        n+=1
        if n>=len(org):
            break
    return res
def enc(text,n):
    str=txt_only(text)
    res=""
    for i in str:
        if i.isalpha()==True:
            if i.isupper()==True:
                x=((alpC.index(i)-n)%26)
                res+=alpC[x]
            else:
                x=((alps.index(i)-n)%26)
                res+=alps[x]
        else:
            res+=i
    res=back_to_normal(text,res)
    return res
def dec(text,n):
    str=txt_only(text)
    res=""
    for i in str:
        if i.isalpha()==True:
            if i.isupper()==True:
                x=((alpC.index(i)-n)%26)
                res+=alpC[x]
            else:
                x=((alps.index(i)-n)%26)
                res+=alps[x]
        else:
            res+=i
    res=back_to_normal(text,res)
    return res
