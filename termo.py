class TermoInteligente:

    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nueva_temperatura):
        if 30 <= nueva_temperatura <= 100:
            self.__temperatura = nueva_temperatura
        else:
            print("El rango de temperatura No esta permitido")

    def calentar(self, grado):
        if grado > 0:
            nueva_temperatura = self.__temperatura + grado
            self.__temperatura = min(nueva_temperatura, 100)
        else:
            print(f"Los grado para calentar son invalido")


    def enfriar(self, grado):
        if grado > 0 :
            nueva_temperatura = self.__temperatura - grado
            self.__temperatura = max(nueva_temperatura, 30)
        else:
            print("Los grados para enfriar son invalido")



