def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u']
    tempvowels = []
    indexarray = []
    liststring = list(s)
    index = 0
    for item in s:
        if item.lower() in vowels:
            tempvowels.append(item)
            indexarray.append(index)
        index += 1


    arraylength = len(indexarray)

    for item in indexarray:
        arraylength -= 1
        liststring[item] = tempvowels[arraylength]

        

    print(''.join(liststring))




reverseVowels("IceCreAm")
