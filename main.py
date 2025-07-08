"""
Termo inteligente de agua
Planteamiento del problema:
Vamos a crear una clase TermoInteligente que simula un termo que:
- Tiene una temperatura actual del agua que debe ser privada (__temperatura).
- Solo permite establecer temperaturas entre 30 y 100 grados Celsius.
- Tiene una propiedad temperatura para consultar el valor actual.
- Tiene un setter temperatura que valida que la nueva temperatura esté en el rango permitido.
- Tiene un método calentar(grados) que aumente la temperatura, sin pasar de 100°C.
- Tiene un método enfriar(grados) que reduzca la temperatura, sin bajar de 30°C.
"""
from termo import TermoInteligente

def main():
    termo1 = TermoInteligente(20)
    print(f"La temperatura del termo actual es: {termo1.temperatura}°C \n")

    termo1.calentar(30)
    print(f"La temperatura del termo caliente es: {termo1.temperatura}°C \n")

    termo1.enfriar(25)
    print(f"La temperatura del termo frio es: {termo1.temperatura}°C\n")

    termo1.calentar(120)
    print(f"La temperatura del termo en su rango es: {termo1.temperatura}°C\n")

    termo1.enfriar(75)
    print(f"La temperatura del termo en su rango es: {termo1.temperatura}°C\n")


if __name__ == "__main__":
    main()