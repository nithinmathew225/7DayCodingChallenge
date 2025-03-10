def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    tempvowels = []
    indexarray = []
    newstring = ''
    index = 0
    for item in s:
        if item.lower() in vowels:
            tempvowels.append(item)
            indexarray.append(index)
        index += 1

    print(tempvowels)
    print(indexarray)

    arraylength = len(indexarray)

    for item in s:
        if item.lower() in vowels:
            arraylength -= 1
            newstring = newstring + tempvowels[arraylength]
        else:
            newstring = newstring + item

    print(newstring)




reverseVowels("IceCreAm")