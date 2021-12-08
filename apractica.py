
x=[]
l=[]
s=0
y=[]
k=[]
with open("/Users/nicoletaroman/Desktop/Lista_clasei_11D.txt","r")as f:
    for i in f:
        x=i.split()
        l.append(x)
        if l[0][3]=='2':
            y.append(i.strip())
        if l[0][3]=='1':
            k.append(i.strip())
        l.clear()
        s+=int(x[2])
with open("/Users/nicoletaroman/Desktop/Media.txt","w")as m:
    m.write(f"Media clasei este = {s/30}")
with open("/Users/nicoletaroman/Desktop/gr1.txt","w")as gr1:
    for element1 in k:
        gr1.write(f"{element1[0:-1]}\n")
with open("/Users/nicoletaroman/Desktop/gr2.txt","w")as gr2:
    for element2 in y:
        gr2.write(f"{element2[0:-1]}\n")