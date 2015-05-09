#Teste para extrair nmeros de strings

import re
with open("f2") as input:
    for line in input:
        cont = 1
        string = str("Frame {0:d}".format(cont))
        if string in line:
            newLine = ("Frame {0:d}".format(s+dif))
            
            s = int(re.search(r'\d+', line).group())
            print (s)
        else:
            print("Nao Rolou")