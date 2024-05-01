class Deposito:
    def __init__(self, saldo, extrato):
        self.saldo = saldo
        self.extrato = extrato

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito de R$ {valor:.2f} realizado com sucesso!\n"
            print("Depósito efetuado!")
        else:
            print("O valor digitado é inválido.")

class Saque:
    def __init__(self, saldo, extrato, limite, numero_saques, limite_saques):
        self.saldo = saldo
        self.extrato = extrato
        self.limite = limite
        self.numero_saques = numero_saques
        self.limite_saques = limite_saques

    def sacar(self, valor):
        excedeu_saldo = valor > self.saldo
        excedeu_limite = valor > self.limite
        excedeu_saques = self.numero_saques >= self.limite_saques

        if excedeu_saldo:
            print("Saldo insuficiente!")
        elif excedeu_limite:
            print("Limite de saque superior ao permitido.")
        elif excedeu_saques:
            print("Número de saques esgotado.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque de R$ {valor:.2f} realizado.\n"
            self.numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

class Extrato:
    def __init__(self, saldo, extrato):
        self.saldo = saldo
        self.extrato = extrato

    def exibir_extrato(self, agencia, numero_conta):
        print("-" * 10, "EXTRATO", "-" * 10)
        print(f"Agência: {agencia}\tConta: {numero_conta}")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print("-" * 30)
        print(f"O saldo atual é de R$ {self.saldo:.2f}")
        print(":" * 30)

class Usuario:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente números): ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            print("Já existe um usuário com esse CPF!")
            return

        nome = input("Informe seu nome completo: ")
        data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/UF): ")

        self.usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "CPF": cpf, "endereco": endereco})
        print("Usuário criado com sucesso!")

    def filtrar_usuario(self, cpf):
        usuarios_filtrados = [usuario for usuario in self.usuarios if usuario["CPF"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

class Conta:
    def __init__(self, contas, usuarios, agencia):
        self.contas = contas
        self.usuarios = usuarios
        self.agencia = agencia

    def criar_conta(self):
        cpf = input("Informe o CPF (somente números): ")
        usuario = Usuario(self.usuarios).filtrar_usuario(cpf)

        if usuario:
            numero_conta = len(self.contas) + 1
            self.contas.append({"agencia": self.agencia, "numero_conta": numero_conta, "usuario": usuario})
            print("Conta criada com sucesso!")
        else:
            print("Usuário não encontrado. Por favor, cadastre-se primeiro.")

class Banco:
    def __init__(self):
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.usuarios = []
        self.contas = []
        self.LIMITE_SAQUES = 3
        self.AGENCIA = "0001"

    def menu(self):
        menu = """\n
        _______ MENU _______

        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nu]\tCadastrar Usuário
        [nc]\tCriar Conta
        [q]\tSair
        ==>"""
        return input(menu)

    def main(self):
        while True:
            opcao = self.menu()

            if opcao == "d":
                valor = float(input("Informe o valor do depósito: "))
                deposito = Deposito(self.saldo, self.extrato)
                deposito.depositar(valor)
                self.saldo = deposito.saldo
                self.extrato = deposito.extrato

            elif opcao == "s":
                valor = float(input("Digite o valor para saque: "))
                saque = Saque(self.saldo, self.extrato, self.limite, self.numero_saques, self.LIMITE_SAQUES)
                saque.sacar(valor)
                self.saldo = saque.saldo
                self.extrato = saque.extrato

            elif opcao == "e":
                extrato = Extrato(self.saldo, self.extrato)
                extrato.exibir_extrato(self.AGENCIA, len(self.contas) + 1)

            elif opcao == "nu":
                Usuario(self.usuarios).criar_usuario()

            elif opcao == "nc":
                Conta(self.contas, self.usuarios, self.AGENCIA).criar_conta()

            elif opcao == "q":
                print("Acesso encerrado!")
                break

# Instanciando e executando o programa
banco = Banco()
banco.main()


