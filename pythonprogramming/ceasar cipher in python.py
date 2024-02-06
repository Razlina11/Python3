def ceasar(text,key):
    result=""
    for char in text:
        if char.isalpha():
            shift=key % 26
            if char.islower():
                base=ord('a')
            else:
                base=ord('A')
            shifted=chr((ord(char)-base+shift) % 26 + base)
            result+=shifted
        else:
            result+=char
    return result

key=3
et=ceasar("abcd",key)
print(et)
