#!/usr/bin/env python3

# Pig

# Filetype = .pigg
#FILE

from sys import exit

FILE = "Test.pigg"

def __init__():
    with open("STRINGSTOR.Vpigg", "w") as f:
        f.write("")
        f.close()
    with open("INTSTOR.Vpigg", "w") as f:
        f.write("")
        f.close()
    with open("build.bat", "w") as f:
        f.write("@echo off\n")
        f.write("color 0a\n")
        f.write("python pig.py\n")
        f.write("pause")
        f.close()

__init__()

def add(a, b):
    fin = int(a) + int(b)
    print(fin)

def multi(a, b):
    fin = int(a) * int(b)
    print(fin)

def divide(a, b):
    fin = int(a) / int(b)
    print(fin)

def subtract(a, b):
    fin = int(a) - int(b)
    print(fin)

def assignString(name, val):
    with open("STRINGSTOR.Vpigg", "a") as f:
        f.write(name + " " + val + "\n")
    f.close()

def assignIntegerPUB(name, val):
    with open("INTSTOR.Vpigg", "a") as f:
        f.write("public" + " " + name + " " + val + "\n")
    f.close()

def assignIntegerPRIV(name, val):
    with open("INTSTOR.Vpigg", "a") as f:
        f.write("private" + " " + name + " " + val + "\n")
    f.close()



def callString(name):
    with open("STRINGSTOR.Vpigg", "r") as f:
        for line in f.readlines():
            if name in line:
                fin = line.rstrip()
                finn = fin.replace(name, "")
                print(finn)
    f.close()


def callInteger(name):
    with open("INTSTOR.Vpigg", "r") as f:
        for line in f.readlines():
            if name in line:
                fin = line.rstrip()
                if "public" in fin:
                    finn = fin.replace(name, "")
                    fnn = finn.replace("public", "")
                    print(fnn)
                elif "private" in fin:
                    fn = fin.replace(name, "")
                    fni = fn.replace("private", "")
                    fnni = fni.replace(fni, "")
                else:
                    exit("ERROR: no method assigned")
                
    f.close()


with open(FILE, "r") as f:
    for line in f.readlines():
        # maths
        if "add" in line:
            fin = line.rstrip()
            finn = fin.replace("add", "")
            digitOne, _, digitwo = finn.partition(',')
            add(digitOne, digitwo)
        if "multi" in line:
            fin = line.rstrip()
            finn = fin.replace("multi", "")
            digitOne, _, digitwo = finn.partition(',')
            multi(digitOne, digitwo)
        if "divide" in line:
            fin = line.rstrip()
            finn = fin.replace("divide", "")
            digitOne, _, digitwo = finn.partition(',')
            divide(digitOne, digitwo)
        if "subtract" in line:
            fin = line.rstrip()
            finn = fin.replace("subtract", "")
            digitOne, _, digitwo = finn.partition(',')
            subtract(digitOne, digitwo)

        #Functions
        if "println" in line:
            fin = line.rstrip()
            if "'" not in line:
                exit("ERROR: cannot print int")
            finn = fin.replace("println", "")
            fn = finn.replace("(", "")
            fni = fn.replace(")", "")
            fnii = fni.replace("'", "")
            fnn, _, msg = fnii.partition(' ')
            print(fnn)

        #var assignment
        if "new string" in line:
            fin = line.rstrip()
            finn = fin.replace("new string", "")
            fnn = finn.replace(" = ", "")
            fni = fnn.replace("'", " ")
            fnii, _, val = fni.partition(' ')
            assignString(fnii, val)
        if "new integer" in line:
            fin = line.rstrip()
            finn = fin.replace("new integer", "")
            fnn = finn.replace(" = ", " ")
            if "public" in fnn:
                fni, _, val = fnn.partition(' ')
                assignIntegerPUB(fni, val)
            if "private" in fnn:
                fni, _, val = fnn.partition(' ')
                assignIntegerPRIV(fni, val)
        if "call string" in line:
            fin = line.rstrip()
            finn = fin.replace("call string", "")
            callString(finn)
        if "call integer" in line:
            fin = line.rstrip()
            finn = fin.replace("call integer", "")
            fnn = finn.replace("   ", "")
            callInteger(fnn)
        if "getmeoutahere" in line:
            exit()
    f.close()
