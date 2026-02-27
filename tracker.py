print("Bem-vindo ao Rastreador de Despesas Diárias!")

# Exibe o menu uma vez (otimizado com aspas triplas)
print("""
Menu:
1. Adicionar uma nova despesa
2. Ver todas as despesas
3. Calcular total e média das despesas
4. Limpar todas as despesas
5. Sair""")

# Inicializa uma lista vazia para armazenar as despesas
expenses = []

while True:
    # Recebe a escolha do usuário
    choice = input()
    
    if choice == "1":
        # Adiciona uma nova despesa
        amount = float(input())
        expenses.append(amount)
        print("Despesa adicionada com sucesso!")

    elif choice == "2":
        # Ver todas as despesas
        if len(expenses) == 0:
            print("Nenhuma despesa registrada ainda.")
        else:
            print("Suas despesas:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")

    elif choice == "3":
        # Calcula o total e a média das despesas (otimizado com sum())
        if len(expenses) == 0:
            print("Nenhuma despesa registrada ainda.")
        else:
            total = sum(expenses)  # ← Otimizado!
            average = total / len(expenses)
            print(f"Total de despesas: {total}")
            print(f"Média de despesas: {average}")

    elif choice == "4":
        # Limpa todas as despesas
        expenses = []
        print("Todas as despesas foram limpas.")

    elif choice == "5":
        # Sai do programa
        print("Saindo do Rastreador de Despesas Diárias. Até logo!")
        break

    else:
        print("Escolha inválida. Por favor, tente novamente.")