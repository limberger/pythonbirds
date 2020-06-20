"""
Você deve crirar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direćão

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direćão terá a responsabilidae4 de controlar a direćão. Ela oferece os seguintes atributos:
1) Valor de direcao com valores possíveis: Norte, Sul, Leste, Oeste.
2) Método girar à direita
3) Método girar à esquerda
    N
O       L
    S

    Exemplo:
    >>> #testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    >>> #Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> #teste carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
"""

class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade > 2:
            self.velocidade -= 2
        else:
            self.velocidade = 0


class Direcao:
    direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']
    def __init__(self, direcao=0 ):
        self.direcao = direcao
        self.valor = Direcao.direcoes[self.direcao]

    def valor(self):
        return Direcao.direcoes[self.direcao]

    def girar_a_direita(self):
        if self.direcao < len(Direcao.direcoes) - 1:
            self.direcao += 1
        else:
            self.direcao = 0
        self.valor = Direcao.direcoes[self.direcao]

    def girar_a_esquerda(self):
        if self.direcao > 0:
            self.direcao -= 1
        else:
            self.direcao = len(Direcao.direcoes)-1
        self.valor = Direcao.direcoes[self.direcao]



class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def calcular_direcao(self):
        return self.direcao.valor