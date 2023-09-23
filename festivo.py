festivo={
    "Enero":["1 - año nuevo", "6 - reyes magos"], 
    "Febrero":["No festivos"],
    "Marzo":["20 - dia de San Jose"]}


def main():
    mes=input("Ingrese un mes: ")
    print(festivo[mes])



if __name__=="__main__":
    main()