def alimento():
    f=open("Alimentos.txt","rt")
    f.seek(3)
    line= f.readlines()
    f.close()
    print(f)




if __name__=="__main__":
    alimento()