def lectura():
    f=open("matrizAsignacion.txt","rt")
    f.seek(3)
    line= f.readlines()
    f.close()
    for i in line:
        a=i.rstrip("\n").split(",")
        print(f"{a} => {int(a[0])+int(a[1])}")
    

def lectura2():
    f=open("matrizAsignacion.txt","rt")
    line=f.readline()
    f.seek(3)
    while line!="":
        print(line)
        opc=input("presione enter")
        line=f.readline()
    f.close()
    print("finalizó la lectura")


def lectura3():
    f=open("matrizAsignacion.txt","rt")
    line=f.read()
    f.close()
    print(line,len(line))
    print("----------------")
    a=line.split("\n")
    for i in a:
        b=i.split(",")
        print(b)
    

if __name__=="__main__":
    #lectura()
    lectura2()
    #lectura3()