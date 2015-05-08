#Teste para extrair números de strings

import re
with open("f2") as input:
    for line in input:
        cont = 1
        string = str("Frame 1")# {0:d}" .format(cont))
        #print("String =" + string.replace(" ",""))
        #print("Line = " + str(line.replace(" ","")))
        if string in line:
            s = int(re.search(r'\d+', line).group())
            print (s)
        else:
            print("Nao Rolou")