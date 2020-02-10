def f(a, b): #gorcoxutyn katrox funkcya
    return (a + b) % 256

def encoding(): #kodavorman funkcya
    k = j = 0
    l = 100 #kodavorman dzax mas
    r = 200 #kodavorman aj mas
    n = 3 #takteri qanak@ sksuma 0 ic mijev 3
    for k in range(1,n+1): #cikl vori mej katarvum e funkcyan ev popoxvum en aj ev dzax maser@
        j = r
        r = l
        l = j ^ f(r, k)
    j = l
    l = r
    r = j
    print("L = ",l,", R = ", r) #tpel aj ev dzax mas@

def decoding():
    k = j = 0
    l = 203 #kodavorman dzax mas
    r = 99 #kodavorman aj mas
    n = 3 #takteri qanak@ sksuma 3ic mijev 0
    for k in range(n, 0, -1): #hetadarc cikl vori mej katarvum e funkcyan ev popoxvum en aj ev dzax maser@
        j = r
        r = l
        l = j ^ f(r, k)
        print(k)
    j = l
    l = r
    r = j
    print("L = ",l,", R = ", r) #tpel aj ev dzax mas@

i = int(input("1 for enc or 2 for dec: ")) #menu vortex @ntrvuma kodavorum kam apakodavorum

if i == 1:
    encoding()
elif i == 2:
    decoding()
else:
    print("Error") #skxali depqum tpuma error
