import random

numdict = []

def num5_generate():
    num5 = random.randint(0, 99999)
    number_str = str(num5).zfill(5)
    return number_str

def unique_num5():
    global numdict
    number5 = num5_generate()
    
    while number5 in numdict:
        number5 = num5_generate()
    
    numdict.append(number5)
    return number5
    
number5 = unique_num5()