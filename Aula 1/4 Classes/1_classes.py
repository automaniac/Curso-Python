class Personagem:
    def curar(self):
        self.vida += 10


class Monstro(Personagem):
    def __init__(self, vida, ataque):
        self.vida = vida
        self.ataque = ataque
        print('monstro criado')

    def atacar(self):
        print('Ataque')

    def rugir(self):
        print("rawr")


class Heroi (Personagem):
    def __init__(self, vida, ataque):
        self.vida = vida
        self.ataque = ataque

    def atacar(self, monstro):
        monstro.vida -= self.ataque
         


monstro1 = Monstro(vida=900, ataque=80)
heroi = Heroi(vida=400, ataque=90)
print(heroi.vida)
heroi.curar()
print(heroi.vida)
