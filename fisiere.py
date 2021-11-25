f=open('/Users/nicoletaroman/Desktop/ABC.txt','w')
c=str(input())
f.write(c)
f.close()
f=open('/Users/nicoletaroman/Desktop/ABC.txt','r')
cr=f.read()
#program cu vocale
vc=[]
for i in range(0,len(cr)):
    if cr[i]=='a' or cr[i]=='i' or cr[i]=='e' or cr[i]=='o' or cr[i]=='u' or cr[i]=='A' or cr[i]=='E' or cr[i]=='I' or cr[i]=='U' or cr[i]=='O':
        vc.append(cr[i])

f=open('/Users/nicoletaroman/Desktop/vocale.txt','w')
f.write(str(vc))
f.write('\n sunt ')
f.write(str(len(vc)))
f.write(' vocale')
f.close()