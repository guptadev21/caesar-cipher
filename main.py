def encrypt(phrase, keyword):
    key = ""
    lent = len(phrase)

    key += keyword

    x = 0

    res = ""

    for i in range (lent - len(key)):
        key += phrase[x]
        x+=1

    # print(key)
    for i in range (lent):
        temp = (ord(phrase[i])-65) + (ord(key[i])-65)
        if (temp > 26):
            temp = temp%26
        res += chr(temp+65)

    return res

def decrypt(msg, keyword):
    phr = "" + keyword
    lent = len(msg)
    for i in range (lent):
        temp = (ord(msg[i])-65) - (ord(phr[i])-65)
        if (temp < 0):
            temp += 26
        phr += chr(temp+65)

    return phr

choice = input("Enter your choice 'en'(encryption) or 'de'(decryption): ")
phrase = input("Enter your phrase here: ")
phrase = phrase.upper()
keyword = input("Enter your keyword: ")
keyword = keyword.upper()

if (choice == "en"):
    res = encrypt(phrase, keyword)
    print("Your encrypted message is: ", res)
elif (choice == "de"):
    res = ""
    de_res = decrypt(phrase, keyword)
    for i in range(len(keyword), len(de_res)):
        res += de_res[i]
    print("Your decrypted message is: ",res)