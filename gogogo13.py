if __name__ == '__main__':
    s = '###'
    isalnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False


    for c in s:
        if c.isalnum():
            kondisi = True
            
        if c.isalpha():
            kondisi = True

        if c.isdigit():
            kondisi = True

        if c.islower():
            kondisi = True

        if c.isupper():
            kondisi = True
    print(isalnum)
    print(isalpha)
    print(isdigit)
    print(isupper)
    print(islower)