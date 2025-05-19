from time import sleep

def linha():
    print("-" * 30)

linha()
print("   CALCULADOR DE FINANÇAS  ")
linha()

transicoes = []
granaAtual = 2000

while True:
    print("BEM-VINDO AO SEU CATÁLOGO DE DESPESAS")
    linha()

    catalogo = int(input(
        "Opção:\n"
        "[1] - adicionar despesas\n"
        "[2] - adicionar receita\n"
        "[3] - ver histórico de transações\n"
        "[4] - ver resumo por categoria\n"
        "[5] - sair do banco\nEscolha: "
    ))
    linha()

    if catalogo == 1:
        valor = float(input("Digite o valor da despesa: R$ "))
        granaAtual -= valor  

        escolha = int(input("Deseja colocar uma descrição?\n[1] - sim\n[2] - não\nEscolha: "))
        if escolha == 1:
            descricao = input("Descreva: ")
        else:
            descricao = "Sem descrição"

        transicoes.append({
            "tipo": "despesa",
            "valor": valor,
            "descricao": descricao
        })

        print(f"Despesa adicionada com sucesso! Seu saldo atual é: R${granaAtual:.2f}")
        print("Voltando ao catálogo...")
        sleep(1.5)



    elif catalogo == 2:
        opcoes = int(input(
            "Adicione a receita correspondente:\n"
            "[1] - anual\n[2] - mensal\n[3] - semanal\nEscolha: "
        ))

        valor = float(input("Digite o valor da receita: R$ "))

        if opcoes == 1:
            frequencia = "anual"
            valor_mensal = valor / 12
        elif opcoes == 2:
            frequencia = "mensal"
            valor_mensal = valor
        elif opcoes == 3:
            frequencia = "semanal"
            valor_mensal = valor * 4.3
        else:
            print("Opção inválida.")
            continue

        descricao = input("Deseja descrever essa receita? Se não quiser, deixe em branco: ")

        transicoes.append({
            "tipo": "receita",
            "valor original": valor,
            "valor mensal": round(valor_mensal, 2),
            "descricao": descricao if descricao else "Sem descrição",
            "frequencia": frequencia
        })

        granaAtual += valor_mensal 

        print(f"Receita {frequencia} adicionada com sucesso.")
        print(f"Valor mensal equivalente: R${valor_mensal:.2f}")
        print(f"Saldo atual: R${granaAtual:.2f}")
        print("Voltando ao catálogo...")
        sleep(1.5)




    elif catalogo == 3:
        print("HISTÓRICO DE TRANSAÇÕES")
        print("-" * 30)

        if len(transicoes) == 0:
            print("Nenhuma transação registrada ainda.")
        else:
            for i in range(len(transicoes)):
                transacao = transicoes[i]

                tipo = transacao.get("tipo", "desconhecido").upper()
                valor = transacao.get("valor", transacao.get("valor mensal", 0.0))
                descricao = transacao.get("descricao", "Sem descrição")
                frequencia = transacao.get("frequencia", "")

                if frequencia != "":
                    print(f"{i+1}. [{tipo}] R$ {valor:.2f} - {descricao} ({frequencia})")
                else:
                    print(f"{i+1}. [{tipo}] R$ {valor:.2f} - {descricao}")



    elif catalogo == 4:
        filtro = input("Digite a categoria que deseja buscar (despesa ou receita): ").lower()
        print(f"\nTransações do tipo: {filtro.upper()}")
        encontrou = False

        for transacao in transicoes:
            if transacao.get("tipo", "").lower() == filtro:
                valor = transacao.get("valor", transacao.get("valor mensal", 0.0))
                descricao = transacao.get("descricao", "Sem descrição")
                frequencia = transacao.get("frequencia", "")
                encontrou = True

                if frequencia != "":
                    print(f"- R$ {valor:.2f} - {descricao} ({frequencia})")
                else:
                    print(f"- R$ {valor:.2f} - {descricao}")

        if not encontrou:
            print("Nenhuma transação encontrada nessa categoria.")

    elif catalogo == 5:
        print("Encerrando o sistema financeiro...")
        break

    else:
        print("Opção inválida. Tente novamente.")
