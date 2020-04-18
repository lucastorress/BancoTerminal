# Author: Lucas Pereira Torres de Araujo
# Lista 9 - FUP's Class - 2016.1
# BancoTXT

contas = []
run = 1
cont = 0
c = 0

print ">>> Bem vindo ao sistema BancoTXT <<<"

while run == 1:
    print "\n### Menu ###"
    print "0 - Sair"
    print "1 - Criar uma nova conta"
    print "2 - Remover uma conta"
    print "3 - Credito"
    print "4 - Debito"
    print "5 - Transferencia"
    print "6 - Consultar saldo\n"
    op = raw_input("Seleciona a operacao que deseja realizar:\n>>> ")

    if op == "0":
        print "\nSistema encerrado."
        run = 0

    elif op == "1":
        flag = 1
        dados_conta = {}
        dados_conta['nome_conta'] = raw_input(
            "Digite o numero da nova conta:\n>>> ")

        for verificar in contas:
            if verificar['nome_conta'] == dados_conta['nome_conta']:
                flag = 0

        if flag == 0:
            print "\nO numero da conta ja existe. Tente novamente."
        else:
            dados_conta['saldo_conta'] = float(
                input("Digite o saldo da nova conta:\n>>> "))
            contas.append(dados_conta)
            print "\nOperacao efetuada com sucesso."

    elif op == "2":
        flag_index = -1
        flag_delete = 0
        remover_conta = raw_input(
            "Digite o numero da conta para remover:\n>>> ")

        for verificar in contas:
            flag_index += 1
            if verificar['nome_conta'] == remover_conta:
                flag_delete = 1

        if flag_delete == 1:
            del contas[flag_index]
            print "\nOperacao efetuada com sucesso."
        else:
            print "\nO numero da conta nao existe. Tente novamente."

    elif op == "3":
        flag = 0
        conta_credito = raw_input("Digite o numero da conta:\n>>> ")

        for consulta in contas:
            if consulta['nome_conta'] == conta_credito:
                flag = 1
                valor_credito = float(
                    input("Digite o valor do credito:\n>>> R$ "))
                if valor_credito < 0:
                    print "\nValores negativos nao sao aceitos. Tente novamente."
                else:
                    consulta['saldo_conta'] += valor_credito
                    print "\nOperacao efetuada com sucesso."

        if flag == 0:
            print "\nO numero da conta nao foi encontrado. Tente novamente."

    elif op == "4":
        flag = 0
        conta_debito = raw_input("Digite o numero da conta:\n>>> ")

        for consulta in contas:
            if consulta['nome_conta'] == conta_debito:
                flag = 1
                valor_debito = float(
                    input("Digite o valor do credito:\n>>> R$ "))
                if valor_debito < 0:
                    print "\nValores negativos nao sao aceitos. Tente novamente."
                else:
                    consulta['saldo_conta'] -= valor_debito
                    print "\nOperacao efetuada com sucesso."
        if flag == 0:
            print "\nO numero da conta nao foi encontrado. Tente novamente."

    elif op == "5":
        flag_is = 0
        conta_transfer = raw_input("Digite o numero da sua conta:\n>>> ")

        # Procura a primeira conta
        for consulta in contas:
            if consulta['nome_conta'] == conta_transfer:
                flag_is = 1
                conta_destino = raw_input(
                    "Digite o numero da conta destino:\n>>> ")

                # Verifica se eh uma transferencia para a mesma conta
                if conta_destino != conta_transfer:
                    # Procura a segunda conta
                    for destino in contas:
                        if destino['nome_conta'] == conta_destino:
                            flag_is = 2
                            valor_transfer = float(
                                input("Digite o valor da transferencia:\n>>> R$ "))

                            # Verifica se o saldo eh suficiente
                            if valor_transfer > consulta['saldo_conta']:
                                print "\nNao eh possivel transferir um valor maior que o seu saldo."
                                break
                            # Verifica se o valor eh negativo
                            elif valor_transfer < 0:
                                print "\nNao eh possivel transferir um valor negativo."
                                break
                            else:
                                consulta['saldo_conta'] -= valor_transfer
                                destino['saldo_conta'] += valor_transfer
                                print "\nOperacao efetuada com sucesso."
                                break
                else:
                    flag_is = 3
                    break

        if flag_is == 0:
            print "\nA sua conta nao foi encontrada. Tente novamente."
        elif flag_is == 1:
            print "\nA conta de destino nao foi encontrada. Tente novamente."
        elif flag_is == 3:
            print "\nNao eh possivel transferir dinheiro para a mesma conta."

    elif op == "6":
        flag = 0
        consulta_conta = raw_input(
            "Digite o numero da conta para consultar o saldo:\n>>> ")

        for consulta in contas:
            if consulta['nome_conta'] == consulta_conta:
                flag = 1
                if consulta['saldo_conta'] >= 0:
                    status = "Positivo"
                else:
                    status = "Negativo"
                print "\nO saldo eh: R$ %.2f (%s)" % (consulta['saldo_conta'], status)

        if flag == 0:
            print "\nO numero da conta nao foi encontrado. Tente novamente."
    else:
        print "\nOperacao invalida."

    if cont % 2 == 0:
        backup = open('banco_backup.txt', 'a')
        c += 1
        linha = "Entrada %s (%s): %s" % (str(c), str(cont), str(contas))
        backup.write(linha+"\n")
        backup.close()

    cont += 1

bancotxt = open('bancotxt.txt', 'w')
linha = str(contas)
bancotxt.write(linha+"\n")

bancotxt.write("\n>>> Dados das contas <<<\n")
for conta in contas:
    dadostxt = "Numero da conta: {0}\nSaldo: {1}\n" .format(
        conta['nome_conta'], conta['saldo_conta'])
    bancotxt.write(dadostxt+"\n")
bancotxt.close()
