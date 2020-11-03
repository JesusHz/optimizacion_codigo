entrada = open("codigo3.txt","r")

lineas = entrada.readlines()

dictValues = dict()

constantFoldedList = []
variables = []
auxVariables = []
auxVariables2 = []
auxVariables3 = []

print("Codigo de 4 direcciones")
print("-----------------------------")

for j in lineas:
    j = j.strip("\n")
    op,arg1,arg2,res = j.split()
    print(op,arg1,arg2,res)
    


#Evaluar codigo de 4 direcciones
for i in lineas:
    i = i.strip("\n")
    op,arg1,arg2,res = i.split()
    bandera = 0
    if (op in ["+","-","*","/"]):
        for x in range(0,len(constantFoldedList)):
            for y in range(0,len(variables)):
                if(constantFoldedList[x][3] in variables[y]):
                    constantFoldedList[x] = [op,arg1,arg2,res]
                    auxVariables.append(constantFoldedList[x])
                    break
        if (arg1.isdigit() and arg2.isdigit()):                     #CASO1: + 1 4 a
            result = eval(arg1+op+arg2)
            dictValues[res] = result
            #print("=",result,"NULL",res)
            constantFoldedList.append(["=",result,"NULL",res])
        elif (arg1.isdigit()):                                       #CASO2: + 1 x a
            if (arg2 in dictValues):
                result = eval(arg1 + op + str(dictValues[arg2]))
                dictValues[res] = result
                #print("=",result,"NULL",res)
                constantFoldedList.append(["=",result,"NULL",res])
            else:
                #print(op,arg1,arg2,res)
                constantFoldedList.append([op,arg1,arg2,res])
        elif (arg2.isdigit()):                                      #CASO3: - x 1 a
            if (arg1 in dictValues):
                result = eval(str(dictValues[arg1]) + op + arg2)
                dictValues[res] = result
                #print("=",result,"NULL",res)
                constantFoldedList.append(["=",result,"NULL",res])
            else:
                #print(op,arg1,arg2,res)
                constantFoldedList.append([op,arg1,arg2,res])
        else:                                                       #CASO4: - a b x
            flag1 = 0
            flag2 = 0
            arg1Res = arg1
            if (arg1 in dictValues):
                arg1Res = str(dictValues[arg1])
                flag1 = 1
            arg2Res = arg2
            if (arg2 in dictValues):
                arg2Res = str(dictValues[arg2])
                flag2 = 1
            if (flag1 == 1 and flag2 == 1):
                result = eval(arg1Res + op + arg2Res)
                dictValues[res] = result
                #print("=",result,"NULL",res) 
                constantFoldedList.append(["=",result,"NULL",res])
            else:
                #print(op,arg1Res,arg2Res,res)
                constantFoldedList.append([op,arg1,arg2,res])
    elif (op == "="):
        if (arg1.isdigit()):
            dictValues[res] = arg1
            #print("=", arg1,"NULL",res)
            constantFoldedList.append(["=",arg1,"NULL",res])
        else:
            if (arg1 in dictValues):
                result = eval(str(dictValues[arg1]))
                dictValues[res] = result
                #print("=",dictValues[arg1],"NULL",res)
                constantFoldedList.append(["=",dictValues[arg1],"NULL",res])
            else:
                #print("=",arg1,"NULL",res)
                constantFoldedList.append(["=",arg1,"NULL",res])
    elif (res[:5] == "print"):
        if (arg1.isdigit()):
            dictValues[res] = arg1
            #print("=", arg1,"NULL",res)
            constantFoldedList.append(["NULL",arg1,"NULL",res])
        else:
            if (arg1 in dictValues):
                result = eval(str(dictValues[arg1]))
                dictValues[res] = result
                #print("NULL",dictValues[arg1],"NULL",res)
                constantFoldedList.append(["NULL",dictValues[arg1],"NULL",res])
            else:
                constantFoldedList.append(["NULL",arg1,"NULL",res])
    elif (op in ["==","!="]):
        if (arg1.isdigit() and arg2.isdigit()):
            result = eval(arg1 + op + arg2)
            dictValues[res] = result
            if (op == "=="):
                result = " != "
            if (op == "!="):
                result = " == "
            constantFoldedList.append([result,arg1,arg2,res])
        elif (arg1.isdigit()):
            if (arg2 in dictValues):
                variables.append([arg2])
                if (op == "=="):
                    result = " != "
                if (op == "!="):
                    result = " == "
                constantFoldedList.append([result,arg1,arg2,res])
            else:
                constantFoldedList.append([result,arg1,arg2,res])
        elif (arg2.isdigit()):
            if (arg1 in dictValues):
                variables.append([arg1])
                
                if (op == "=="):
                    result = " != "
                if (op == "!="):
                    result = " == "
                #print(result,arg1,arg2,res)
                constantFoldedList.append([result,arg1,arg2,res])
            else:
                #print(op,arg1,arg2,res)
                constantFoldedList.append([op,arg1,arg2,res])
        else:
            ban1 = 0
            ban2 = 0
            variables.append([arg1])
            variables.append([arg2])
            arg1Res = arg1
            if (arg1 in dictValues):
                #arg1Res = str(dictValues[arg1])
                ban1 = 1
            arg2Res = arg2
            if (arg2 in dictValues):
                #arg2Res = str(dictValues[arg2])
                ban2 = 1
            if (ban1 == 1 and ban2 == 1):
                if (op == "=="):
                    result = " != "
                if (op == "!="):
                    result = " == "
                #print(result,arg1,arg2,res)
                constantFoldedList.append([result,arg1,arg2,res])
            else:
                #print(result,arg1,arg2,res)
                constantFoldedList.append([result,arg1,arg2,res])
    elif (op in [">","<","<=",">="]):
        if (arg1.isdigit() and arg2.isdigit()):
            result = eval(arg1 + op + arg2)
            dictValues[res] = result
            if (op == "<"):
                result = ">= "
            if (op == ">"):
                result = "<= "
            if (op == ">="):
                result = " <= "
            if (op == "<="):
                result = " >= "
            #print(result,arg1,arg2,res)
            constantFoldedList.append([result,arg1,arg2,res])
        elif (arg1.isdigit()):
            if (arg2 in dictValues):
                variables.append([arg2])
          
                if (op == "<"):
                    result = ">= "
                if (op == ">"):
                    result = "<= "
                if (op == ">="):
                    result = " <= "
                if (op == "<="):
                    result = " >= "
                #print(result,arg1,arg2,res)
                constantFoldedList.append([result,arg1,arg2,res])
            else:
                #print(op,arg1,arg2,res)
                constantFoldedList.append([op,arg1,arg2,res])
        elif (arg2.isdigit()):
            if (arg1 in dictValues):
                variables.append([arg1])
              
                if (op == "<"):
                    result = ">= "
                if (op == ">"):
                    result = "<= "
                if (op == ">="):
                    result = " <= "
                if (op == "<="):
                    result = " >= "
                #print(result,arg1,arg2,res)
                constantFoldedList.append([result,arg1,arg2,res])
            else:
                #print(op,arg1,arg2,res)
                constantFoldedList.append([op,arg1,arg2,res])
        else:
            ban1 = 0
            ban2 = 0
            arg1Res = arg1
            variables.append([arg1])
            variables.append([arg2])
            if (arg1 in dictValues):
                #arg1Res = str(dictValues[arg1])
                ban1 = 1
            arg2Res = arg2
            if (arg2 in dictValues):
                #arg2Res = str(dictValues[arg2])
                ban2 = 1
            if (ban1 == 1 and ban2 == 1):
                if (op == "<"):
                    result = ">= "
                if (op == ">"):
                    result = "<= "
                if (op == ">="):
                    result = " <= "
                if (op == "<="):
                    result = " >= "
                #print(result,arg1,arg2,res)
                constantFoldedList.append([result,arg1,arg2,res])
            else:
                #print(result,arg1,arg2,res)
                constantFoldedList.append([result,arg1,arg2,res])
    else:
        #print(op,arg1,arg2,res)
        constantFoldedList.append([op,arg1,arg2,res])

for x in auxVariables:
	if x not in auxVariables3:
		auxVariables3.append(x)
	else:
		if x not in auxVariables2:
			auxVariables2.append(x)



print("\n")
print("Codigo Intermedio Reducido")
print("------------------------------")

conBloque = 0
print("Bloque " + str(conBloque) + ":")
conBloque +=1

for i in constantFoldedList:
    string = i[3]

    if (i[0] in ["> ","< "," == "," != "]):
        for x in range (0,len(constantFoldedList)):
            if (constantFoldedList[x] == i):
                aux = constantFoldedList[x][0]
                if (aux == "> "):
                    constantFoldedList[x][0] = "<= "
                elif (aux== "< "):
                    constantFoldedList[x][0] = ">= "
                elif (aux== "== "):
                    constantFoldedList[x][0] = "!= "
                elif (aux== "!= "):
                    constantFoldedList[x][0] = "== "
                x += 1
                #print(constantFoldedList[x])

    if (i[0] == "="):
        print(i[3],i[0],i[1])
    elif (i[0] in ["+","-","*","/"]):
        print(i[3],"=",i[1],i[0],i[2])
    elif (string[:4] == "goto"):            
        if (i[0] != "NULL" and i[1] != "NULL" and i[2] != "NULL"):
            print("Bloque " + str(conBloque) + ":")
            conBloque +=1
            print("if",i[1],i[0],i[2],string)
            print("Bloque " + str(conBloque) + ":")
            conBloque +=1
        else:
            print(string)
            print("Bloque " + str(conBloque) + ":")
            conBloque +=1
    elif (string[:3] in ["met"]):
        print("Bloque " + str(conBloque) + ":")
        conBloque +=1
        if (i[1] == "NULL" and i[2] == "NULL"):
            print(string,"( ",")")
        elif (i[1] != "NULL" and i[2] == "NULL"):
            print(string,"(",i[1],")")
        elif (i[1] == "NULL" and i[2] != "NULL"):
            print(string,"(",i[2],")")
        elif (i[1] != "NULL" and i[2] != "NULL"):
            print(string,"(",i[1],",",i[2],")")
        print("Bloque " + str(conBloque) + ":")
        conBloque +=1
    elif (string[:5] in ["print"]):
        print(string,"(",i[1],")")

print("\n")
print("Eliminacion de Codigo Muerto")
print("-----------------------------------")
contador = 0
print("Bloque " + str(contador) + ":")
contador +=1

repe = []

for i in constantFoldedList:
    string = i[3]

    anterior = ""
    siguiente = ""

    aux = -1

    if (i[0] in [">= ","<= "," == ", " != "," <= "," >= "]):
        for x in range (0,len(constantFoldedList)):
            if (constantFoldedList[x] == i):
                x += 1
                aux = x
                #print(constantFoldedList[x])

    if (i[0] in [">=","<=",">= ","<= "," == "," != "," >= "," <= "]):
        for x in range (0,len(constantFoldedList)):
            if (constantFoldedList[x]== i):
                anterior = constantFoldedList[x][3]
                y = x + 1
                siguiente = constantFoldedList[y][3]
                constantFoldedList[x][3] = siguiente
                constantFoldedList[y][3] = anterior
                string = siguiente
                if (aux != -1):
                    constantFoldedList[aux][3] = ""
                    #print(constantFoldedList[aux])
                if ((constantFoldedList[x][1] or constantFoldedList[x][2]) == repe[0][3]):
                    print(repe[0][3],"=",repe[0][1],repe[0][0],repe[0][2])
    if (i[0] == "="):
        for x in auxVariables2:
            if(i == x):
                print(i[3],i[0],i[1])
    elif (i[0] in ["+","-","*","/"]):
        for x in auxVariables2:
            if(x[3] in ["i","x","j"] and i[3] in ["i","x","j"]):
                #print(i[3],"=",i[1],i[0],i[2])
                repe.append(i)
                break
    elif (string[:4] == "goto"):
        if (i[0] != "NULL" and i[1] != "NULL" and i[2] != "NULL"):
            print("Bloque " + str(contador) + ":")
            contador +=1
            print("if",i[1],i[0],i[2],string)
            print("Bloque " + str(contador) + ":")
            contador +=1
        else:
            print(string)
            print("Bloque " + str(contador) + ":")
            contador +=1
    elif (string[:3] in ["met"]):
        print("Bloque " + str(contador) + ":")
        contador +=1
        if (i[1] == "NULL" and i[2] == "NULL"):
            print(string,"( ",")")
        elif (i[1] != "NULL" and i[2] == "NULL"):
            print(string,"(",i[1],")")
        elif (i[1] == "NULL" and i[2] != "NULL"):
            print(string,"(",i[2],")")
        elif (i[1] != "NULL" and i[2] != "NULL"):
            print(string,"(",i[1],",",i[2],")")
        print("Bloque " + str(contador) + ":")
        contador +=1
    elif (string[:5] in ["print"]):
        print(string,"(",i[1],")")