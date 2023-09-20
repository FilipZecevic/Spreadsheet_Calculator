import ast
dict1={"A1":1,"A2":2}
def equasion(stro):  
    if stro[0]!="=":
        print("if")
        return stro
    elif stro[0]=="=":
        print("elif")
        stro1=stro.replace("=","")
        try:
            x = range(26)
            y = range(100)
            for i in x:
                print("for")
                for j in y:
                    key1=i+ord('A')
                    key2=j
                    print(chr(key1), end='')
                    print(key2)

            rezultat = eval(stro1)
            nnflag = True
        except:
            print("expect")
            nnflag = False
            return "NaN"
        if nnflag == True:
            rezultat_float = float(rezultat)
            return rezultat_float
        
#if stro[0]!="=":
#    print(stro)
#elif stro[0]=="=":
#    stro1=stro.replace("=","")
#        for i in (0,26):
#            for j in (0,100):
#                key1=i+ord('A')
#                key2=j
#                kljuc=chr(key1)+key2
#                if stro1.find(kljuc):
#                    stro1=stro1.replace(kljuc,dict1[kljuc])
#                
#                
#    try:
#        x = range(26)
#        y = range(100)
#        for i in x:
#            for j in y:
#                key1=i+ord('A')
#                key2=j
#                print(chr(key1), end='')
#                print(key2)
#        rezultat = eval(stro1)
#        nnflag = True
#    except:
#        print("expect")
#        nnflag = False
#        print("NaN")
#    if nnflag == True:
#        rezultat_float = float(rezultat)
#        print(rezultat_float)
def duck(dict1):
    stro=str(input())
    if stro[0]!="=":
        print(stro)
    elif stro[0]=="=":
        stro1=stro.replace("=","")
        for i in range(0,26):
            for j in range(0,100):
                key1=i+ord('A')
                key2=j
                kljuc=chr(key1)+str(key2)
                if kljuc in stro1:
                    stro1=stro1.replace(kljuc,str(dict1[kljuc]))
        try:
            tree = ast.parse(stro1, mode='eval')
            rezultat = eval(compile(tree, filename='', mode='eval'))
            nnflag=True
        except:
            nnflag=False
            print("Error")
        if nnflag == True:
            rezultat_float = float(rezultat)
            print(rezultat_float)

        
 
