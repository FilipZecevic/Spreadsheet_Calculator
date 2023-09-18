def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a*b
def equasion(stro):
    if stro[0]!="=":
        return stro
    elif stro[0]=="=":
        stro1=stro.replace("=","")
        try:
            rezultat = eval(stro1)
            nnflag = True
        except:
            nnflag = False
            return "NaN"
        if nnflag == True:
            rezultat_float = float(rezultat)
            return rezultat_float
    
