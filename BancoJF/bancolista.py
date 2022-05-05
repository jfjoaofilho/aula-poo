
class BancoLista:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta):
        self.contas.append(conta)

    def procurar_conta(self,numero):
        achou = False
        for elemento in self.contas:
            if elemento.get_numero() == numero:
                achou = True
                return elemento
        if achou is False:
                return None

    def creditar(self,numero,valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print('Conta Inexistente!')

    def debitar(self,numero,valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print('Conta Inexistente!')

    def saldo(self, numero,saldo):
        conta = self.procurar_conta(numero)
        if conta:
            conta.get_saldo(saldo)
        else:
            print('Conta Inexistente!')


    def transferir(self, origem, destino, valor):
        conta = self.procurar_conta(origem)
        conta1 = self.procurar_conta(destino)

        if (conta == True and conta1 == True):
            conta.debitar(valor)
            conta1.creditar(valor)

