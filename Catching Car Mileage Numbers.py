def zera(x):
    x=str(x)
    global dlugosc

    dlugosc=len(x)
    if dlugosc>1:
        for i in x[1:]:
            if i!='0':
                return False
        return  True
    else:
        return False


def same(x):
    x = str(x)
    for i in x[1:]:
        if i != x[0]:
            return False
    return True

def inc(x):
    x = str(x)
    for i in range(0,dlugosc-1):
        if (int(x[i])+1 != int(x[i+1])):#
            if (int(x[i]) - 9 != int(x[i + 1])):
                return False
    return True

def dec(x):
    x = str(x)
    for i in range(0,dlugosc-1):
        if (int(x[i]) != int(x[i+1])+1):#
            
            return False
    return True

def rev(x):
    x = str(x)
    if x==x[::-1]:
        return  True
    else:
        return False
#
# def is_interesting(number, awesome_phrases):
#


def is_interesting(number, awesome_phrases):
    licznik=2
    pomoc=0
    if number>97:
        while number<100:
            licznik-=1
            number+=1
        while licznik>=0:
            if(licznik==0):
                pomoc+=1
            if(zera(number))==True:
                print(1)
                return licznik+pomoc
            if (same(number)) == True:
                print(2)
                return licznik + pomoc
            if (inc(number)) == True:
                print(3)
                return licznik + pomoc
            if (dec(number)) == True:
                print(4)
                return licznik+pomoc
            if (rev(number)) == True:
                print(5)
                return licznik + pomoc

            number=str(number)
            #print(awesome_phrases[0])
            for i in awesome_phrases:
                if str(i) in number:
                    print("Wykryto takie same wartości",i,number)
                    return licznik + pomoc
            number=int(number)
            number+=1
            licznik-=1
            print("Numer wynosi teraz",number)
        return 0
    else:
        return 0




