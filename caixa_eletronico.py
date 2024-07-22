class CaixaEletronico:
    def __init__(self):
        self.notas_disponiveis = [100, 50, 10, 5, 1]

    def sacar(self, valor):
        if valor < 10 or valor > 600:
            print("O valor do saque deve ser entre 10 e 600 reais.")
            return

        distribuicao = self.calcular_distribuicao_notas(valor)
        self.imprimir_distribuicao(distribuicao)

    def calcular_distribuicao_notas(self, valor):
        distribuicao = {}
        for nota in self.notas_disponiveis:
            quantidade_notas = valor // nota
            valor -= quantidade_notas * nota
            distribuicao[nota] = quantidade_notas
        return distribuicao

    def imprimir_distribuicao(self, distribuicao):
        print("Notas distribuídas:")
        for nota, quantidade in distribuicao.items():
            if quantidade > 0:
                print(f"{quantidade} nota(s) de R${nota}")

# Exemplo de uso
if __name__ == "__main__":
    valor_saque = int(input("Informe o valor do saque: "))
    caixa = CaixaEletronico()
    caixa.sacar(valor_saque)
