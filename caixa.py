def caixa_eletronico(valor):
    if valor < 10 or valor > 600:
        print("O valor do saque deve ser entre 10 e 600 reais.")
        return
    
    notas = [100, 50, 10, 5, 1]
    distribuicao = {}

    for nota in notas:
        quantidade_notas = valor // nota
        valor -= quantidade_notas * nota
        distribuicao[nota] = quantidade_notas

    print("Notas distribuídas:")
    for nota, quantidade in distribuicao.items():
        if quantidade > 0:
            print(f"{quantidade} nota(s) de R${nota}")

# Exemplo de uso
valor_saque = int(input("Informe o valor do saque: "))
caixa_eletronico(valor_saque)
