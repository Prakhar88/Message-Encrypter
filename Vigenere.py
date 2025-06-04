alps=list(map(chr,range(97,123)))
alpC=list(map(chr,range(65,91))) 
def keyvalid(str):
    return str.isalpha()   
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
def enc(text,key):
    res=''
    txt=txt_only(text)
    if len(txt)==len(key):
        for i in range(len(txt)):
            if txt[i].isalpha():
                if txt[i].isupper():
                    c=alpC[(alpC.index(txt[i])+alpC.index(key[i].upper()))%26]
                else:
                    c=alps[(alps.index(txt[i])+alps.index(key[i].lower()))%26]
                res+=c
            else:
                res+=txt[i]
    else:
        a=len(txt)//len(key)
        key=a*key
        a=len(txt)-len(key)
        key+=key[0:a]
        for i in range(len(txt)):
            if txt[i].isalpha():
                if txt[i].isupper():    
                    c=alpC[(alpC.index(txt[i])+alpC.index(key[i].upper()))%26]
                else:
                    c=alps[(alps.index(txt[i])+alps.index(key[i].lower()))%26]
                res+=c
            else:
                res+=txt[i]
    res=back_to_normal(text,res)
    return res
def dec(text,key):
    txt=txt_only(text)
    res=''
    if len(txt)==len(key):
        for i in range(len(txt)):
            if txt[i].isalpha():
                if txt[i].isupper():    
                    c=alpC[(alpC.index(txt[i])-alpC.index(key[i].upper()))%26]
                else:
                    c=alps[(alps.index(txt[i])-alps.index(key[i].lower()))%26]
                res+=c
            else:
                res+=txt[i]
    else:
        a=len(txt)//len(key)
        key=a*key
        a=len(txt)-len(key)
        key+=key[0:a]
        for i in range(len(txt)):
            if txt[i].isalpha():
                if txt[i].isupper():    
                    c=alpC[(alpC.index(txt[i])-alpC.index(key[i].upper()))%26]
                else:
                    c=alps[(alps.index(txt[i])-alps.index(key[i].lower()))%26]
                res+=c
            else:
                res+=txt[i]
    res=back_to_normal(text,res)
    return res
