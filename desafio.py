menu = " Menu ".center(20,"#")

menu+="""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> Digite a sua opção: """

saldo = 0.0
limite = 500
extrato = " Extrato da Conta ".center(30, "$") + "\n"
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    # depósito
    if opcao == "d":            
        valor = float(input("\nQual valor voce deseja DEPOSITAR? "))

        if (valor > 0):            
            print("Depósito realizado com sucesso")
            saldo += valor
            extrato += f"+ Depósito: R$ {valor:.2f}\n"
            print(f"Saldo atual {saldo}")
        else:
            print("Valor para depósito tem que ser maior que zero!!")

    # saque
    elif opcao == "s":        
        valor = float(input("\nQual valor voce deseja SACAR? "))

        if (valor > 500) or (saldo < valor) or (numero_saques >= 3):
            if (valor > 500):
                print(f"Valor solicitado R$ {valor} acima do permitido.")
            
            if (saldo < valor):
                print("Saldo insuficiente.")

            if (numero_saques >= 3):
                print("Quantidade máxima diária de saques atingida.")
            
        
        else:
            print("Saque realizado com sucesso")
            saldo -= valor
            numero_saques = numero_saques + 1
            extrato += f"- Saque: R$ {valor:.2f}\n"
            print(f"Saldo atual {saldo}")

    # extrato
    elif opcao == "e":
        print(f"{extrato} \n Saldo Atual: {saldo:.2f}\n")

    # sair do sistema
    elif opcao == "q":
        break

    # opção inválida
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")