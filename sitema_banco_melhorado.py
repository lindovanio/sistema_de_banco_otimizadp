def menu():
    print("=============== MENU ===============")
    print("C - Criar conta")
    print("LC - Listar contas")
    print("D - Depositar")
    print("N - novo cliente")
    print("S - Sacar")
    print("L - Listar clientes")
    print("E - Extrato")
    print("Q - Sair")
    print("=====================================")


def depositar(saldo, extrato):
    try:
        valor = float(input("Digite o valor do deposito: R$:").replace(",", "."))
    except ValueError:
        print("Valor inválido. Tente novamente.")
        return saldo  # Retorna saldo sem alteração

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        mensagem = f"Depósito de R$ {valor:.2f} realizado com sucesso!"
        tamanho = len(mensagem)
        print(tamanho)
    else:
        print("Valor inválido para depósito.")
    return saldo


def sacar(saldo, extrato, limite, saques_realizados, limite_saque):
    try:
        valor = float(input("Digite o valor do saque: R$:").replace(",", "."))
    except ValueError:
        print("Valor inválido. Digite um valor numérico.")
        return saldo  # Retorna saldo sem alteração

    if saques_realizados >= limite_saque:
        print("Limite de saques diários atingido. Tente novamente amanhã.")

    elif valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite:
        print(f"Valor do saque excede o limite de R$ {limite:.2f}.")
    elif valor <= 0:
        print("Valor de saque deve ser positivo.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_realizados += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    return saldo, saques_realizados


def extrato_func(saldo, extrato):
    print("=============== EXTRATO ===============")
    if not extrato:
        print("Nenhuma transação realizada.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=======================================")


def formatar_cpf(cpf):

    cpf = "".join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def novo_usuario(cpf, nome, idade, novos_usuarios):
    print("=============== NOVO USUÁRIO ===============")
    while True:
        nome = input("Digite o nome do cliente: ").strip()
        if not nome:
            print("Nome inválido. Nao pode ser vazio.")
            continue

        elif nome.isdigit():
            print("Nome inválido. Digite apenas letras.")
            continue

        else:
            print(f"nome:{nome.title()} foi cadastrado.")
            break
    print("===========================================")
    print(" Observação: O CPF deve conter apenas números e ter 11 dígitos.")
    print("===========================================")

    while True:
        cpf = input("Digite o CPF do cliente: ")

        if novos_usuarios:
            usuario_existente = filtrar_usuarios(cpf, novos_usuarios)
            if usuario_existente:
                print(
                    f"CPF {formatar_cpf(cpf)} já cadastrado para o usuário {usuario_existente['nome']}."
                )
                continue

        elif not cpf.isdigit():
            print("CPF inválido. Digite apenas números.")
            continue
        elif len(cpf) != 11:
            print("CPF inválido. Deve conter 11 dígitos numéricos.")
            continue
        break

    print(f"CPF: {formatar_cpf(cpf)} foi cadastrado.")
    while True:
        idade = input("Digite a idade do cliente: ")

        if not idade.isdigit():
            print("Idade inválida. Digite apenas números.")
            continue
        idade = int(idade)
        if idade <= 0:
            print("Idade inválida. Deve ser um número positivo.")
            continue
        elif idade < 18:
            print(
                "Idade inválida. O cliente deve ser maior de idade (18 anos ou mais)."
            )
            continue
        break

    novos_usuarios.append({"nome": nome, "cpf": cpf, "idade": idade})

    print(f"Usuário {nome} adicionado com sucesso!")

    print("===========================================")


def listar_usuarios(novos_usuarios):
    print("=============== USUÁRIOS CADASTRADOS ===============")
    if not novos_usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in novos_usuarios:
            print(
                f"Nome: {usuario['nome']}, CPF: {formatar_cpf(usuario['cpf'])}, Idade: {usuario['idade']} anos"
            )
    print("=====================================================")


def criar_conta(agencia, numero_conta, novos_usuarios):
    print("=============== CRIAR CONTA ===============")
    cpf = input("Digite o CPF do cliente: ").strip()
    usuario = filtrar_usuarios(cpf, novos_usuarios)
    if not usuario:
        print("CPF não encontrado. Por favor, crie um novo usuário.")
        print("===========================================")
        return None
    else:
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario,
        }
        print(
            f"Conta criada com sucesso para {usuario['nome']}, agencia: {agencia}, numero_conta: {numero_conta} CPF: {formatar_cpf(usuario['cpf'])}, Idade: {usuario['idade']} anos."
        )
        print("===========================================")
        return conta


def listar_contas(contas):
    print("=============== CONTAS CADASTRADAS ===============")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(
                f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Nome: {conta['usuario']['nome']}, CPF: {formatar_cpf(conta['usuario']['cpf'])}, Idade: {conta['usuario']['idade']} anos"
            )


def filtrar_usuarios(cpf, novos_usuarios):
    cpf_formatado = formatar_cpf(cpf)
    for usuario in novos_usuarios:
        if formatar_cpf(usuario["cpf"]) == cpf_formatado:
            return usuario
    return None


def main():
    agencia = "0001"
    saldo = 0
    limite = 500.00
    extrato = []
    saques_realizados = 0  # Contador de saques realizados
    limite_saque = 3  # Limite de saques por dia
    novos_usuarios = []  # Lista para armazenar novos usuários
    numero_conta = 0  # Contador de contas criadas
    cpf = ""
    nome = ""
    idade = ""
    contas = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip().upper()
        if opcao not in ["D", "S", "E", "Q", "C", "N", "L", "LC"]:
            print("Opção inválida. Escolha D, S, E, N, C, L, LC ou Q.")
            continue
        elif opcao == "D":
            saldo = depositar(saldo, extrato)
        elif opcao == "S":
            saldo, saques_realizados = sacar(
                saldo, extrato, limite, saques_realizados, limite_saque
            )

        elif opcao == "C":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, novos_usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "LC":
            listar_contas(contas)
        elif opcao == "E":
            extrato_func(saldo, extrato)
        elif opcao == "N":
            novo_usuario(cpf, nome, idade, novos_usuarios)
        elif opcao == "L":
            listar_usuarios(novos_usuarios)
        elif opcao == "Q":
            print("Saindo do sistema. Obrigado!")
            break


main()
