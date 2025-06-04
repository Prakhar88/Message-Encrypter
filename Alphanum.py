alps=list(map(chr,range(97,123)))
alpC=list(map(chr,range(65,91)))
def enc(text):
    L = []
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                L.append(str(alpC.index(text[i]) + 1))
                L.append('-')
            else:
                L.append(str(alps.index(text[i]) + 1))
                L.append('-')
        else:
            if L and L[-1] == '-':
                L.pop()
            L.append(text[i])
    if L and L[-1] == '-':
        L.pop()
    return ''.join(L)
def dec(encoded):
    res = ''
    temp = ''
    i = 0
    while i < len(encoded):
        if encoded[i].isdigit():
            temp += encoded[i]
        elif encoded[i] == '-':
            if temp:
                num = int(temp)
                res += alps[num - 1] 
                temp = ''
        else:
            if temp:
                num = int(temp)
                res += alps[num - 1]
                temp = ''
            res += encoded[i]
        i += 1
    if temp:
        res += alps[int(temp) - 1]
    return res