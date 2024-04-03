def ierakstit(teksts):
    fails = open("teksts.txt", "w", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()
    return
# ierakstit("Gundars")

def pierakstit(teksts):
    fails = open("teksts.txt", "a", encoding="utf-8")
    fails.write(teksts+"\n")
    fails.close()
    return
# pierakstit(" i love cats")

def nolasitvisu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    return teksts

# print(nolasitvisu())

def dabutrindas():
    fails = open("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()
    
    for i in range(len(rindas)):
        rindas[i] = rindas[i].strip()
    
    return rindas

#saraksts = dabutrindas()
#print(saraksts)

#ierakstit("FAKE cat, https://th.bing.com/th/id/OIP.YoF9RZTUoChn60ZjBfptewHaE8?rs=1&pid=ImgDetMain")
#pierakstit("REAL cat, https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Domestic_cat_cropped.jpg/235px-Domestic_cat_cropped.jpg")

print(dabutrindas)