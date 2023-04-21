
def encrypt(string, encryptKey):
    resultString = ''
    for x in string:
        if x in encryptKey:
            resultString += encryptKey[x]
        else:
            resultString += x
    return resultString

def decrypt(string,encryptKey):
    resultString = ''
    for x in string:
        if x in encryptKey.values():
            for key,value in encryptKey.items():
                if value==x:
                    resultString += key
        else:
            resultString += x
    return resultString


strung = "informatyka"
klucz = {'a':'y', 'e':'i', 'i':'o' , 'o':'a' , 'y':'e'}
strung2 = "onfarmyteky"
print(encrypt(strung,klucz))
print(decrypt(strung2,klucz))