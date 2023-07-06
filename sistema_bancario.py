menu = """

[A] Depositar
[B] Sacar
[C] Extrato
[D] Sair

=>"""

Saldo = 0
Limite = 500
Extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "A":
        valor = float(input("Informe o valor que deseja depositar: "))
        
        if valor > 0:
            Saldo += valor
            Extrato += f"deposito: R$ {valor:.2f}\n"


    elif opcao == "B":
       valor =  float(input("qual valor deseja sacar? "))
       valor_muito_acima_saldo = valor > Saldo
       valor_muito_acima_limite = valor > Limite
       Limite_saques_atingido = numero_saques >= LIMITE_SAQUES

       if valor_muito_acima_saldo:
           print("Saldo insuficiente")
        
       elif valor_muito_acima_limite:
           print("Valor Acima do Limite de saque")
       
       elif Limite_saques_atingido:
           print("Você atingiu o limite de saque")
        
       elif valor > 0:
            Saldo -= valor
            Extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

       else:
           print("Operação Falhou, informe valor valido")


    elif opcao == "C":
        
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not Extrato else Extrato)
        print(f"\nSaldo: R$ {Saldo:.2f}")
        print("==========================================")

    elif opcao == "D":
        break

    else:
        print("opção invalida, Por favor seleciona novamento a operação desejada")
        

    





    