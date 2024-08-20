class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao


class Sessao:
    def __init__(self, filme, horario, preco):
        self.filme = filme
        self.horario = horario
        self.preco = preco


class Ingresso:
    def __init__(self, sessao):
        self.sessao = sessao


class Cinema:
    def __init__(self):
        self.filmes = []
        self.sessoes = []

    def adicionar_filme(self, filme):
        self.filmes.append(filme)

    def adicionar_sessao(self, sessao):
        self.sessoes.append(sessao)

    def listar_filmes(self):
        print("\nFilmes disponíveis:")
        for idx, filme in enumerate(self.filmes, start=1):
            print(f"{idx}. {filme.titulo} ({filme.duracao} min)")

    def listar_sessoes(self):
        print("\nSessões disponíveis:")
        for idx, sessao in enumerate(self.sessoes, start=1):
            print(f"{idx}. {sessao.filme.titulo} - {sessao.horario} - R${sessao.preco:.2f}")

    def comprar_ingresso(self):
        self.listar_sessoes()
        escolha = int(input("Escolha a sessão pelo número: ")) - 1
        sessao_escolhida = self.sessoes[escolha]
        qtd_ingressos = int(input("Quantos ingressos deseja comprar? "))

        total = sessao_escolhida.preco * qtd_ingressos
        print(
            f"\nVocê comprou {qtd_ingressos} ingressos para '{sessao_escolhida.filme.titulo}' às {sessao_escolhida.horario}.")
        print(f"Total a pagar: R${total:.2f}")


def main():
    cinema = Cinema()

    # Adicionando filmes
    filme1 = Filme("Matrix", 136)
    filme2 = Filme("O Senhor dos Anéis", 178)
    filme3 = Filme("Star Wars", 121)

    cinema.adicionar_filme(filme1)
    cinema.adicionar_filme(filme2)
    cinema.adicionar_filme(filme3)

    # Adicionando sessões
    sessao1 = Sessao(filme1, "14:00", 20.0)
    sessao2 = Sessao(filme2, "17:00", 25.0)
    sessao3 = Sessao(filme3, "20:00", 22.0)

    cinema.adicionar_sessao(sessao1)
    cinema.adicionar_sessao(sessao2)
    cinema.adicionar_sessao(sessao3)

    while True:
        print("\nSistema de Cinema")
        print("1. Listar filmes")
        print("2. Listar sessões")
        print("3. Comprar ingresso")
        print("4. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cinema.listar_filmes()
        elif opcao == 2:
            cinema.listar_sessoes()
        elif opcao == 3:
            cinema.comprar_ingresso()
        elif opcao == 4:
            print("Obrigado por usar o sistema de cinema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
