class personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza= fuerza
        self.inteligencia= inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(self.nombre)
        print("-fuerza:", self. fuerza)
        print("-inteligencia", self. inteligencia)
        print("-defensa:", self. defensa)
        print("-vida:", self. vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    def esta_vivo(self):
        return self.vida > 0
    def morir(self):
         self.vida < 0
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("vida de", enemigo.nombre, "es", enemigo.vida)
        if daño <= 0:
            enemigo.vida  = 0
        else:
            print("vida de", enemigo.nombre, "es", enemigo. vida)
    

            
#variable de constructor pasivo de la clase
mi_personaje = personaje("Dante", 40, 3,70, 100)
mi_personaje.imprimir_atributos()
mi_enemigo = personaje("Vergil", 70, 30,70,100)
mi_personaje.atacar(mi_enemigo)
mi_enemigo.imprimir_atributos()

#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
# mi_personaje.subir_nivel(10,1,5)
# print("--------------")
# mi_personaje.imprimir_atributos()
# mi_personaje.nombre = "chemafighther"
# mi_personaje. fuerza = 30
# mi_personaje.inteligencia = 12
# mi_personaje.defensa = 28
# mi_personaje.vida = 3

# print("el nombre del personaje es", mi_personaje. nombre)
# print("La fuerza de personaje  es", mi_personaje. fuerza)
# print("el inteligencia del personaje es", mi_personaje. inteligencia)
# print("el defensa del personaje es", mi_personaje. defensa)
# print("el vida del personaje es", mi_personaje. vida)
