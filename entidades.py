class Pessoa:

    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self, comida=None):
        if self.falando:
            print(f'{self.nome} não pode comer pois esta falando')
        elif self.dormindo:
            print(f'{self.nome} não pode comer pois esta dormindo')
        elif self.comendo:
            print(f'{self.nome} Já esta comendo')
        else:
            self.comendo = True
            print(f'{self.nome} está comendo {comida}')

    def pararComer(self):
        if self.comendo:
            print(f'{self.nome} parou de comer')
            self.comendo = False
        else:
            print(f'{self.nome} não esta comendo')

    def falar(self):
        if self.comendo:
            print(f'{self.nome} não pode falar pois esta comendo')
        elif self.dormindo:
            print(f'{self.nome} não pode comer pois esta dormindo')
        elif self.falando:
            print(f'{self.nome} já esta falando')
        else:
            self.falando = True
            print(f'{self.nome} está falando')

    def pararFalar(self):
        if self.falando:
            print(f'{self.nome} parou de falar')
            self.falando = False
        else:
            print(f'{self.nome} não esta falando')

    def dormir(self):
        if self.comendo:
            print(f'{self.nome} não pode dormir pois esta comendo')
        elif self.falando:
            print(f'{self.nome} não pode dormir pois esta falando')
        elif self.dormindo:
            print(f'{self.nome} já esta dormindo')
        else:
            self.dormindo = True
            print(f'{self.nome} está dormindo')

    def pararDormir(self):
        if self.dormindo:
            print(f'{self.nome} acordou')
            self.dormindo = False
        else:
            print(f'{self.nome} não esta falando')

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}. Tenho de {self.idade} anos e peso {self.peso}kg")


class ContaBancaria:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = 0

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo += valor_deposito
        else:
            print("Valor de deposito incorreto")

    def sacar(self, valor_saque):
        if valor_saque > 0:
            if (self.saldo - valor_saque) > self.limite:
                print("Saldo insuficiente")
            else:
                self.saldo -= valor_saque
        else:
            print("Valor de depoisito incorreto")

    def ativarConta(self, limite):
        if not self.status:
            self.status = True
            self.limite = limite
            print("Conta ativada")
        else:
            "A conta já está ativa"

    def verificarSaldo(self):
        print(f'R${self.saldo:.2f}')


class Animal:

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'{self.nome} foi comer')

    def emitirSom(self):
        print(f"{self.nome} está emitindo som")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f'{self.nome} está miando')


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f"{self.nome} está latindo")


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f"{self.nome} está dizendo que tá atrasado")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirSom(self):
        print(f"{self.nome} está mugindo")
