menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor para depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$ {valor:.2f} com sucesso!"
            print("Depósito efeutado!")
        
        else:
            print("O valor digitado é inválido.")
        

    elif opcao == "s":
        valor = float(input("Digite o valor para saque: "))

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
            print("Saque realizado com sucesso!")
            numero_saques += 1

    elif opcao == "e":
        print("-" * 10, "EXTRATO", "-" * 10)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"O saldo atual é de R$ {saldo:.2f}")
        print(":" * 30)

    elif opcao == "q":
        print("Acesso encerrado!")
        break

  

