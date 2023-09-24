class Persona:
    def __init__(self, nombre, estatura, peso):
        self.nombre=nombre
        self.estatura=estatura
        self.peso=peso
    
    def calcular(self):
        estatura= self.estatura /100
        imc = self.peso/(estatura**2)
        return imc
    
    def escala(self):
        imc = self.calcular()
        if imc < 18.5:
            return "Por debajo"
        elif imc < 24.9:
            return "Saludable"
        elif imc < 29.9:
            return "Sobrepeso"
        elif imc < 34.9:
            return "Obesidad I"
        elif imc < 39.9:
            return "Obesidad II"
        else:
            return "Obesidad severa"

def main():
    personas = [
        persona("Pedro Caceres", 188, 97),
        persona("Maria Pérez", 160, 47),
        persona("Julian Dominguez", 158, 58),
        persona("Jessica Fuentes", 170, 73)
    ]

    for persona in personas:
        nombre = persona.nombre
        imc = persona.calcular()
        escala = persona.escala()
    
        print(f"{nombre}: IMC = {round(imc,2)}, Por tanto está en = {escala}")

if __name__=="__main__":
    main()

