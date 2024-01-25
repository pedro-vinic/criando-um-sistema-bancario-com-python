def menu():
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

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito R$ {valor:.2f} com sucesso!"
        print("Depósito efeutado!")    
    else:
        print("O valor digitado é inválido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite,numero_saques,limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Saldo insuficiente!")
            
    elif excedeu_limite:
        print("Limite de sanque superior ao permitido.")

    elif excedeu_saques:
        print("Número de saques esgotado.")

    elif valor > 0:
        saldo -= valor
        extrato += f"\nSaque de R$ {valor:.2f} realizado.\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato
        
def exibir_extrato(saldo, /, *, extrato, agencia, conta):
    print("-" * 10, "EXTRATO", "-" * 10)
    print(f"Agência = {agencia}\t Conta: {conta}")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("-" * 30)
    print(f"O saldo atual é de R$ {saldo:.2f}")
    print(":" * 30)

def criar_usuario(usuarios):
    cpf = input("Informa o CPF (somente o número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe um usuário com esse CPF!")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data de nascimento": data_nascimento, "CPF": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informa o CPF (somente o número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrato.")
        return criar_usuario(usuarios)
    
    

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []    

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)          

        elif opcao == "s":
            valor = float(input("Digite o valor para saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )            

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato, agencia=AGENCIA, conta=numero_conta)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "q":
            print("Acesso encerrado!")
            break

main()

