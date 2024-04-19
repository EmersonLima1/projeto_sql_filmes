from rich import print
from funcoes_db import *

def listar_opcoes():
    # Lista das opções
    opcoes = [
        "1. Exibir a quantidade total de filmes no banco de dados",
        "2. Exibir os nomes das colunas da tabela 'filmes'",
        "3. Exibir a quantidade de filmes com português como língua original",
        "4. Exibir a quantidade de filmes lançados entre 2000 e 2023",
        "5. Exibir os 10 filmes com melhores avaliações",
        "6. Exibir os 10 filmes com piores avaliações",
        "7. Exibir os 10 gêneros com o maior número de filmes",
        "8. Exibir os 10 gêneros de filmes com melhores avaliações",
        "9. Exibir os 10 filmes de ação mais populares em inglês lançados a partir de 2023",
        "10. Exibir 10 filmes com duração maior que a média de duração em seus respectivos gêneros",
        "11. Exibir o total de filmes lançados por ano de lançamento",
        "12. Exibir o total de filmes por idioma",
        "13. Exibir os 10 filmes com maiores orçamentos",
        "14. Exibir os 10 filmes com maiores bilheterias",
        "15. Exibir os 10 filmes com maiores retornos de investimento (bilheteria / orçamento)",
        "16. Exibir 10 filmes com alta popularidade mas baixa média de votos",
        "17. Exibir 10 filmes com baixa popularidade mas alta média de votos",
        "18. Exibir os 10 filmes com mais participações de diferentes países",
        "19. Filmes com títulos idênticos",
        "20. Meses em que os filmes são lançados com mais frequência",
        "21. Filmes mais populares com a temática Inteligência Artificial",
        "22. Filmes melhores avaliados lançados no dia 04/04/1999",
        "0. Sair"
    ]
    
    # Calcula a largura máxima das opções para definir o tamanho da caixa
    largura_max = max(len(opcao) for opcao in opcoes)
    
    # Exibe a caixa de opções com uma borda
    print("+" + "-" * (largura_max + 4) + "+")
    for opcao in opcoes:
        print(f"| {opcao.ljust(largura_max)} |")
    print("+" + "-" * (largura_max + 4) + "+")

# Função principal para gerenciar o sistema
def main():
  
    # Estabelece a conexão com o banco de dados
    conn = conectar_banco_dados()
    
    while True:

        print("[bold cyan]Escolha uma das opções abaixo:[/bold cyan]")

        # Exibe o menu de opções
        listar_opcoes()
        
        # Obtém a escolha do usuário
        escolha = input("Digite o número da opção escolhida: ")
        
        # Verifica a escolha do usuário e executa a operação correspondente
        if escolha == '1':
            contar_filmes(conn)
        elif escolha == '2':
            exibir_nomes_colunas(conn, 'filmes')
        elif escolha == '3':
            filmes_port(conn)
        elif escolha == '4':
            filmes_2000_2023(conn)
        elif escolha == '5':
            listar_melhores_avaliados(conn)
        elif escolha == '6':
            listar_piores_avaliados(conn)
        elif escolha == '7':
            listar_generos_mais_filmes(conn)
        elif escolha == '8':
            listar_generos_melhores_avaliados(conn)
        elif escolha == '9':
            exibir_filmes_acao_populares_port(conn)
        elif escolha == '10':
            filmes_media_duracao_maior_genero(conn)
        elif escolha == '11':
            total_filmes_ano(conn)
        elif escolha == '12':
            total_filmes_idioma(conn)
        elif escolha == '13':
            filmes_maiores_orcamentos(conn)
        elif escolha == '14':
            filmes_maiores_bilheterias(conn)
        elif escolha == '15':
            filmes_maiores_lucros(conn)
        elif escolha == '16':
            filmes_alta_popularidade_baixo_votos(conn)
        elif escolha == '17':
            filmes_baixa_popularidade_alta_votos(conn)
        elif escolha == '18':
            filmes_participacoes_paises(conn)
        elif escolha == '19':
            filmes_titulos_similares(conn)
        elif escolha == '20':
            meses_mais_filmes(conn)
        elif escolha == '21':
            filmes_tematica_ia(conn)
        elif escolha == '22':
            filmes_lancados_04_04_1999(conn)
        elif escolha == '0':
            print("[bold red]Saindo...[/bold red]")
            break
        else:
            print("[bold red]Opção inválida. Por favor, tente novamente.[/bold red]")
    
    # Fecha a conexão com o banco de dados
    conn.close()

# Executa a função principal
if __name__ == '__main__':
    main()
