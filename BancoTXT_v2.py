# Author: Lucas Pereira Torres de Araujo
# Lista 10 (Sub-rotinas) - FUP's Class - 2016.1
# BancoTXT v2.0

import os


def check_file():
    if not os.path.isfile('contas.txt'):
        print "\n>>> Aviso de seguranca:"
        print "O arquivo contas.txt nao existe. Vamos criar um agora!"
        file('contas.txt', 'w').close()


def carregar_contas():
    # Abrir as listas
    arquivo = open('contas.txt', 'r')
    for linha in arquivo.readlines():
        keys = linha.split()
        dic = {}
        dic['nome_conta'] = keys[0]
        dic['saldo_conta'] = float(keys[1])
        contas.append(dic)
    # Fechar
    arquivo.close()


def salvar_contas():
    # Salvar listas
    arquivo = open('contas.txt', 'w')
    for j in xrange(len(contas)):
        dic = contas[j]
        key_conta = dic['nome_conta']
        key_valor = dic['saldo_conta']
        word = str(key_conta) + " " + str(key_valor) + "\n"
        arquivo.write(word)
    arquivo.close()


def menu():
    print "\n### Menu ###"
    print "0 - Sair"
    print "1 - Criar uma nova conta"
    print "2 - Remover uma conta"
    print "3 - Credito"
    print "4 - Debito"
    print "5 - Transferencia"
    print "6 - Consultar saldo\n"


def verificar_conta(parametro, flag=1):
    for verificar in contas:
        if verificar['nome_conta'] == parametro:
            flag = 0

    return flag


def index_conta(parametro, flag_index=-1, flag_delete=0):
    for verificar in contas:
        flag_index += 1
        if verificar['nome_conta'] == parametro:
            flag_delete = 1
            break

    return (flag_index, flag_delete)


def criar_conta(conta, saldo):
    dados_conta = {}
    dados_conta['nome_conta'] = conta

    flag = verificar_conta(conta)

    if flag == 0:
        print "\nO numero da conta ja existe. Tente novamente."
    else:
        dados_conta['saldo_conta'] = saldo
        contas.append(dados_conta)
        print "\nOperacao efetuada com sucesso."


def remover_conta(conta):
    index, delete = index_conta(conta)
    if delete == 1:
        del contas[index]
        print "\nOperacao efetuada com sucesso."
    else:
        print "\nO numero da conta nao existe. Tente novamente."


def operacao_credito(conta, valor):
    flag = verificar_conta(conta)
    if flag == 1:
        print "\nO numero da conta nao foi encontrado. Tente novamente."
    else:
        if valor < 0:
            print "\nValores negativos nao sao aceitos. Tente novamente."
        else:
            index, delete = index_conta(conta)
            contas[index]['saldo_conta'] += valor
            print "\nOperacao efetuada com sucesso."


def operacao_debito(conta, valor):
    flag = verificar_conta(conta)
    if flag == 1:
        print "\nO numero da conta nao foi encontrado. Tente novamente."
    else:
        if valor < 0:
            print "\nValores negativos nao sao aceitos. Tente novamente."
        else:
            index, delete = index_conta(conta)
            contas[index]['saldo_conta'] -= valor
            print "\nOperacao efetuada com sucesso."


def operacao_transferencia(saida, destino, valor):
    if saida == destino:
        print "\nNao eh possivel transferir dinheiro para a mesma conta."
    elif valor < 0:
        print "\nNao eh possivel transferir um valor negativo."
    else:
        flag_out = verificar_conta(saida)
        flag_in = verificar_conta(destino)
        if flag_in == 1 and flag_out == 1:
            print "\nO numero das duas contas nao foi encontrado. Tente novamente."
        elif flag_in == 0 and flag_out == 1:
            print "\nO numero da sua conta nao foi encontrado. Tente novamente."
        elif flag_in == 1 and flag_out == 0:
            print "\nO numero da conta destino nao foi encontrado. Tente novamente."
        else:
            index_out, delete = index_conta(saida)
            index_in, delete = index_conta(destino)

            if contas[index_out]['saldo_conta'] < valor:
                print "\nNao eh possivel transferir um valor maior que o seu saldo."
            else:
                contas[index_out]['saldo_conta'] -= valor
                contas[index_in]['saldo_conta'] += valor
                print "\nOperacao efetuada com sucesso."


def consultar_saldo(conta):
    flag = verificar_conta(conta)

    if flag == 1:
        print "\nO numero da conta nao foi encontrado. Tente novamente."
    else:
        index, delete = index_conta(conta)
        saldo = contas[index]['saldo_conta']

        if saldo >= 0:
            status = "Positivo"
        else:
            status = "Negativo"

        print "\nO saldo eh: R$ %.2f (%s)" % (saldo, status)


def sair(run=0):
    print "\nSistema encerrado."
    return run


run = 1

print ">>> Bem-vindo ao sistema BancoTXT <<<"

while run == 1:

    contas = []

    # Check File 'contas.txt'
    check_file()

    # Carrega as contas existentes
    carregar_contas()

    # Mostrar o menu
    menu()
    # Seleciona a opcao desejada
    op = raw_input("Seleciona a operacao que deseja realizar:\n>>> ")

    # Sair
    if op == "0":
        run = sair()

    # Criar nova conta
    elif op == "1":
        nconta = raw_input("Digite o numero da nova conta:\n>>> ")
        nsaldo = float(input("Digite o saldo da nova conta:\n>>> "))
        criar_conta(nconta, nsaldo)

    # Remover conta existente
    elif op == "2":
        conta = raw_input("Digite o numero da conta para remover:\n>>> ")
        remover_conta(conta)

    # Credito em conta
    elif op == "3":
        conta = raw_input("Digite o numero da conta:\n>>> ")
        valor_credito = float(input("Digite o valor do credito:\n>>> R$ "))
        operacao_credito(conta, valor_credito)

    # Debito em conta
    elif op == "4":
        conta = raw_input("Digite o numero da conta:\n>>> ")
        valor_debito = float(input("Digite o valor do debito:\n>>> R$ "))
        operacao_debito(conta, valor_debito)

    # Transferencia
    elif op == "5":
        conta1 = raw_input("Digite o numero da sua conta:\n>>> ")
        conta2 = raw_input("Digite o numero da conta destino:\n>>> ")
        valor_transfer = float(
            input("Digite o valor da transferencia:\n>>> R$ "))
        operacao_transferencia(conta1, conta2, valor_transfer)

    # Consulta de saldo
    elif op == "6":
        conta = raw_input(
            "Digite o numero da conta para consultar o saldo:\n>>> ")
        consultar_saldo(conta)

    else:
        print "\nOperacao invalida."

    # Salva os dados das contas
    salvar_contas()
