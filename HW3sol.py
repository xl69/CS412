#Stub submission file for CS412 Homework 3.

def get_sequences(file, minsup):
    #Load file:
    f = open(file, "r")
    items = []
    sequences = []
    while(True):
        str = f.readline()
        if str == '': break
        item, sequence = str.split(',')
        sequence = sequence[2:]
        sequence, _ = sequence.split('>')
        sequences.append(sequence)
    #Find frequent patterns:
    fre = {}
    take = {}
    for sequence in sequences:
        take = dict.fromkeys(take, True)
        for char in sequence:
            if char not in fre:
                take[char] = False
                fre[char] = 1
            elif take[char] == True:
                take[char] = False
                fre[char] = fre.get(char) + 1
    for char in list(fre):
        if fre[char] < minsup:
            del fre[char]
    newfre = {}
    keys = fre.keys()
    for key1 in keys:
        for key2 in keys:
            char = ''
            char += key1 + key2
            newfre[char] = 0
    keys = newfre.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                newfre[key] = newfre.setdefault(key, 0) + 1
    for char in list(newfre):
        if newfre[char] < minsup:
            del newfre[char]
    key1s = fre.keys()
    key2s = newfre.keys()
    fre3 = {}
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre3[char] = 0
    keys = fre3.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre3[key] = fre3.setdefault(key, 0) + 1
    for char in list(fre3):
        if fre3[char] < minsup:
            del fre3[char]
    key1s = fre.keys()
    key2s = fre3.keys()
    fre4 = {}
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre4[char] = 0
    key1s = newfre.keys()
    for key1 in key1s:
        for key2 in key1s:
            char = ''
            char += key1 + key2
            fre4[char] = 0
    keys = fre4.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre4[key] = fre4.setdefault(key, 0) + 1
    for char in list(fre4):
        if fre4[char] < minsup:
            del fre4[char]
    key1s = fre.keys()
    key2s = fre4.keys()
    fre5 = {}
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre5[char] = 0
    key1s = newfre.keys()
    key2s = fre3.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre5[char] = 0
    keys = fre5.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre5[key] = fre5.setdefault(key, 0) + 1
    for char in list(fre5):
        if fre5[char] < minsup:
            del fre5[char]
    fre6 = {}
    key1s = fre.keys()
    key2s = fre5.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre6[char] = 0
    key1s = newfre.keys()
    key2s = fre4.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre6[char] = 0
    key1s = fre3.keys()
    key2s = fre3.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre6[char] = 0
    keys = fre6.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre6[key] = fre6.setdefault(key, 0) + 1
    for char in list(fre6):
        if fre6[char] < minsup:
            del fre6[char]
    fre7 = {}

    key1s = fre.keys()
    key2s = fre6.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre7[char] = 0
            
    key1s = newfre.keys()
    key2s = fre5.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre7[char] = 0
            
    key1s = fre3.keys()
    key2s = fre4.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre7[char] = 0
    keys = fre7.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre7[key] = fre7.setdefault(key, 0) + 1
    for char in list(fre7):
        if fre7[char] < minsup:
            del fre7[char]
    fre8 = {}

    key1s = fre.keys()
    key2s = fre7.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre8[char] = 0
            
    key1s = newfre.keys()
    key2s = fre6.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre8[char] = 0
            
    key1s = fre3.keys()
    key2s = fre5.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre8[char] = 0

    key1s = fre4.keys()
    key2s = fre4.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre8[char] = 0

    keys = fre8.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre8[key] = fre8.setdefault(key, 0) + 1
    for char in list(fre8):
        if fre8[char] < minsup:
            del fre8[char]
    fre9 = {}

    key1s = fre.keys()
    key2s = fre8.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre9[char] = 0
            
    key1s = newfre.keys()
    key2s = fre7.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre9[char] = 0
            
    key1s = fre3.keys()
    key2s = fre6.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre9[char] = 0

    key1s = fre4.keys()
    key2s = fre5.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre9[char] = 0

    keys = fre9.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre9[key] = fre9.setdefault(key, 0) + 1
    for char in list(fre9):
        if fre9[char] < minsup:
            del fre9[char]
    fre10 = {}

    key1s = fre.keys()
    key2s = fre9.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre10[char] = 0
            
    key1s = newfre.keys()
    key2s = fre8.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre10[char] = 0
            
    key1s = fre3.keys()
    key2s = fre7.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre10[char] = 0

    key1s = fre4.keys()
    key2s = fre6.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre10[char] = 0
            
    key1s = fre5.keys()
    key2s = fre5.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre10[char] = 0

    keys = fre10.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre10[key] = fre10.setdefault(key, 0) + 1
    for char in list(fre10):
        if fre10[char] < minsup:
            del fre10[char]
    
    fre11 = {}

    key1s = fre.keys()
    key2s = fre10.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre11[char] = 0
            
    key1s = newfre.keys()
    key2s = fre9.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre11[char] = 0
            
    key1s = fre3.keys()
    key2s = fre8.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre11[char] = 0

    key1s = fre4.keys()
    key2s = fre7.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre11[char] = 0
            
    key1s = fre5.keys()
    key2s = fre6.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre11[char] = 0

    keys = fre11.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre11[key] = fre11.setdefault(key, 0) + 1
    for char in list(fre11):
        if fre11[char] < minsup:
            del fre11[char]
            
    fre12 = {}

    key1s = fre.keys()
    key2s = fre11.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre12[char] = 0
            
    key1s = newfre.keys()
    key2s = fre10.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre12[char] = 0
            
    key1s = fre3.keys()
    key2s = fre9.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre12[char] = 0

    key1s = fre4.keys()
    key2s = fre8.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre12[char] = 0
            
    key1s = fre5.keys()
    key2s = fre7.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre12[char] = 0

    key1s = fre6.keys()
    key2s = fre6.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre12[char] = 0

    keys = fre12.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre12[key] = fre12.setdefault(key, 0) + 1
    for char in list(fre12):
        if fre12[char] < minsup:
            del fre12[char]
            
    fre13 = {}

    key1s = fre.keys()
    key2s = fre12.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre13[char] = 0
            
    key1s = newfre.keys()
    key2s = fre11.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre13[char] = 0
            
    key1s = fre3.keys()
    key2s = fre10.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre13[char] = 0

    key1s = fre4.keys()
    key2s = fre9.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre13[char] = 0
            
    key1s = fre5.keys()
    key2s = fre8.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre13[char] = 0

    key1s = fre6.keys()
    key2s = fre7.keys()
    for key1 in key1s:
        for key2 in key2s:
            char = ''
            char += key1 + key2
            fre13[char] = 0

    keys = fre13.keys()
    for key in keys:
        for sequence in sequences:
            if key in sequence:
                fre13[key] = fre13.setdefault(key, 0) + 1
    for char in list(fre13):
        if fre13[char] < minsup:
            del fre13[char]
    fre.update(newfre);
    fre.update(fre3);
    fre.update(fre4);
    fre.update(fre5);
    fre.update(fre6);
    fre.update(fre7);
    fre.update(fre8);
    fre.update(fre9);
    fre.update(fre10);
    fre.update(fre11);
    fre.update(fre12);
    fre.update(fre13);
    #Fill in this dictionary so that the keys are frequent patterns and the values are the absolute support.
    
    return fre

