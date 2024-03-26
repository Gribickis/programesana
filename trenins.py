def rezultats(sk1, sk2):
    if sk1>0 and sk2>0:
        rez = sk1*sk2
    else:
        rez = sk1+sk2
    return rez


for skaitlis in range(1, 11, 2):
    for otrs in range(2, 11, 2):
        print("pirmais skaitlis:", skaitlis, "otrais skaitlis:", otrs, "rezultāts:", rezultats(skaitlis, otrs))
        
def zvaigznes (Skaits):
    for rindasnr in range(1, Skaits+1):
        print("*"*rindasnr)
zvaigznes(5)

def zvaigznes2 (Skaits):
    for rindasnr in range(1, Skaits+1):
        for zvaigzne in range(rindasnr):
            print("*", end="")
        print("")
zvaigznes2(5)


skaitlis1 = 3
skaitlis2 = 5

print("pirmais skaitlis:", skaitlis1, "otrais skaitlis:", skaitlis2, "rezultats:", rezultats(skaitlis1,skaitlis2))