import sqlite3
from rich import print
from rich.console import Console
from rich.table import Table

# Instancia o console
console = Console()

# Função para conectar com o banco de dados
def conectar_banco_dados():
    conn = sqlite3.connect('filmes.db')
    conn.row_factory = sqlite3.Row
    return conn

# Função para contar o número de filmes na tabela
def contar_filmes(conn):
    # Consulta para contar o número de filmes na tabela
    consulta = "SELECT COUNT(*) FROM filmes"
    cursor = conn.execute(consulta)
    resultado = cursor.fetchone()[0]
    
    # Exibe o resultado com formatação
    console.print(f"[bold green]Quantidade de filmes no banco de dados:[/bold green] [blue]{resultado}[/blue]")

# Função para listar quantos filmes têm Português como língua original
def filmes_port(conn):
    # Consulta SQL para contar o número de filmes com Português como língua original
    consulta = "SELECT COUNT(*) FROM filmes WHERE original_language = 'pt'"
    cursor = conn.execute(consulta)
    
    # Obtém o resultado da consulta
    resultado = cursor.fetchone()[0]
    
    # Exibe o resultado com formatação
    print(f"[bold green]Quantidade de filmes com língua original em Português:[/bold green] [blue]{resultado}[/blue]")

# Função para listar quantos filmes foram lançados entre os anos 2000 e 2023
def filmes_2000_2023(conn):
    # Consulta SQL para contar o número de filmes lançados entre os anos 2000 e 2023
    consulta = "SELECT COUNT(*) FROM filmes WHERE release_date >= '2000/01/01' AND release_date <= '2023/12/31'"
    cursor = conn.execute(consulta)

    # Obtém o resultado da consulta
    resultado = cursor.fetchone()[0]
    
    # Exibe o resultado com formatação
    print(f"[bold green]Quantidade de filmes lançados entre 2000 e 2023: [/bold green] [blue]{resultado}[/blue]")

# Função para listar os 10 filmes melhores avaliados
def listar_melhores_avaliados(conn):
    # Consulta SQL para obter os 10 filmes melhores avaliados
    consulta = "SELECT title, vote_average FROM filmes ORDER BY vote_average DESC LIMIT 10"
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os filmes
    table = Table(title="10 Filmes Melhores Avaliados")
    table.add_column("Título", style="cyan")
    table.add_column("Avaliação Média", style="magenta")
    
    # Adiciona as linhas com os filmes à tabela
    for row in cursor:
        title, vote_average = row
        table.add_row(title, f"{vote_average:.1f}")
    
    # Imprime a tabela com os 10 filmes melhores avaliados
    console.print(table)

# Função para listar os 10 filmes piores avaliados
def listar_piores_avaliados(conn):
    # Consulta SQL para obter os 10 filmes piores avaliados
    consulta = "SELECT title, vote_average FROM filmes ORDER BY vote_average ASC LIMIT 10"
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os filmes
    table = Table(title="10 Filmes Piores Avaliados")
    table.add_column("Título", style="cyan")
    table.add_column("Avaliação Média", style="magenta")
    
    # Adiciona as linhas com os filmes à tabela
    for row in cursor:
        title, vote_average = row
        table.add_row(title, f"{vote_average:.1f}")
    
    # Imprime a tabela com os 10 filmes piores avaliados
    console.print(table)

# Função para listar os 10 gêneros com mais filmes
def listar_generos_mais_filmes(conn):
    # Consulta SQL para obter os 10 gêneros com mais filmes
    consulta = "SELECT genres, COUNT(*) AS total_filmes FROM filmes WHERE genres IS NOT NULL AND genres != '' GROUP BY genres ORDER BY total_filmes DESC LIMIT 10"
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os gêneros
    table = Table(title="10 Gêneros com Mais Filmes")
    table.add_column("Gênero", style="cyan")
    table.add_column("Total de Filmes", style="magenta")
    
    # Adiciona as linhas com os gêneros à tabela
    for row in cursor:
        genre, total_filmes = row
        table.add_row(genre, f"{total_filmes}")
    
    # Imprime a tabela com os 10 gêneros com mais filmes
    console.print(table)

# Função para listar os 10 gêneros de filmes melhores avaliados
def listar_generos_melhores_avaliados(conn):
    # Consulta SQL para obter os 10 gêneros de filmes melhores avaliados
    consulta = "SELECT genres, AVG(vote_average) AS media_avaliacao FROM filmes GROUP BY genres ORDER BY media_avaliacao DESC LIMIT 10"
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os gêneros
    table = Table(title="10 Gêneros de Filmes Melhores Avaliados")
    table.add_column("Gênero", style="cyan")
    table.add_column("Média de Avaliação", style="magenta")
    
    # Adiciona as linhas com os gêneros à tabela
    for row in cursor:
        genre, media_avaliacao = row
        table.add_row(genre, f"{media_avaliacao:.1f}")
    
    # Imprime a tabela com os 10 gêneros de filmes melhores avaliados
    console.print(table)

# Função para exibir os 10 filmes de ação mais populares em inglês lançados a partir de 2023
def exibir_filmes_acao_populares_port(conn):
    # Consulta SQL para obter os 10 filmes de ação mais populares em inglês lançados a partir de 2023
    consulta = "SELECT title, popularity, original_language, release_date, genres FROM filmes WHERE genres LIKE '%Action%' AND original_language = 'en' AND release_date > '2022-12-31' ORDER BY popularity DESC LIMIT 10"

    cursor = conn.execute(consulta)

    # Cria uma tabela visual para exibir os filmes de ação mais populares
    table = Table(title="10 filmes de ação mais populares em português lançados a partir de 2023")
    table.add_column("Título", style="cyan")
    table.add_column("Pontuação de popularidade", style="magenta")
    table.add_column("Idioma original", style="green")
    table.add_column("Data de lançamento", style="blue")
    table.add_column("Gêneros", style="yellow")

    # Adiciona as linhas com as informações dos filmes à tabela
    for row in cursor:
        # Desempacota a linha em cinco variáveis
        filme, pontuacao, idioma_original, data_lancamento, generos = row
        # Adiciona uma linha à tabela com os dados do filme
        table.add_row(filme, f"{pontuacao:.1f}", idioma_original, data_lancamento, generos)

    # Imprime a tabela com os 10 filmes de ação mais populares em inglês lançados a partir de 2023
    console.print(table)

# Função para exibir 10 filmes cuja duração é maior que a média da duração dos gêneros desses filmes
def filmes_media_duracao_maior_genero(conn):
    
    # Subconsulta para calcular a média de duração para cada gênero
    consulta = """
        WITH media_duracao_por_genero AS (
            SELECT genres, AVG(runtime) as media_duracao
            FROM filmes
            GROUP BY genres
        )
        -- Consulta principal para obter os filmes com duração maior que a média da duração dos gêneros
        SELECT f.title, f.genres, f.runtime, md.media_duracao
        FROM filmes AS f
        JOIN media_duracao_por_genero AS md ON f.genres = md.genres
        WHERE f.runtime > md.media_duracao
        ORDER BY f.runtime DESC
        LIMIT 10
    """
    cursor = conn.execute(consulta)

    # Cria a tabela para exibir os resultados
    table = Table(title="10 filmes cuja duração é maior que a média da duração dos gêneros desses filmes")
    table.add_column("Título", style="cyan")
    table.add_column("Duração (em minutos)", style="magenta")
    table.add_column("Gêneros", style="green")
    table.add_column("Média da Duração (em minutos)", style="blue")

    # Adiciona os dados à tabela
    for row in cursor:
        # Desempacota cada linha em quatro variáveis
        filme, generos, duracao, media_duracao = row
        # Adiciona uma linha à tabela com os dados do filme
        table.add_row(filme, str(duracao), generos, f"{media_duracao:.1f}")

    # Exibe a tabela no console
    console.print(table)

# Função para exibir o total de filmes por ano de lançamento
def total_filmes_ano(conn):
    
    # Consulta SQL para obter o total de filmes por ano de lançamento
    consulta = """
        SELECT STRFTIME('%Y', release_date) AS ano, COUNT(*) AS total_filmes
        FROM filmes
        WHERE ano IS NOT NULL AND ano != ''
        GROUP BY ano
        ORDER BY total_filmes DESC
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="Total de filmes por ano de lançamento")
    table.add_column("Ano de lançamento", style="cyan")
    table.add_column("Total de filmes", style="magenta")
    
    # Itera sobre cada linha retornada pela consulta
    for row in cursor:
        # Desempacota cada linha nos campos "ano" e "total_filmes"
        ano, total_filmes = row
        
        # Adiciona uma nova linha à tabela com os dados de "ano" e "total_filmes"
        table.add_row(str(ano), str(total_filmes))
    
    # Imprime a tabela com os resultados no console
    console.print(table)

# Função para exibir o total de filmes por idioma
def total_filmes_idioma(conn):
    
    # Consulta SQL para obter o total de filmes por idioma
    consulta = """
        SELECT original_language, COUNT(*) AS total_filmes
        FROM filmes
        WHERE original_language IS NOT NULL AND original_language != ''
        GROUP BY original_language
        ORDER BY total_filmes DESC
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="Total de filmes por idioma")
    table.add_column("Idioma", style="cyan")
    table.add_column("Total de filmes", style="magenta")
    
    # Itera sobre cada linha retornada pela consulta
    for row in cursor:
        # Desempacota cada linha nos campos "idioma" e "total_filmes"
        idioma, total_filmes = row
        
        # Adiciona uma nova linha à tabela com os dados de "idioma" e "total_filmes"
        table.add_row(idioma, str(total_filmes))
    
    # Imprime a tabela com os resultados no console
    console.print(table)

# Função para exibir os 10 filmes com maiores orçamentos
def filmes_maiores_orcamentos(conn):
    
    # Consulta SQL para obter os 10 filmes com maiores orçamentos
    consulta = """
        SELECT title, budget
        FROM filmes
        ORDER BY budget DESC
        LIMIT 10
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="10 filmes com maiores orçamentos")
    table.add_column("Título", style="cyan")
    table.add_column("Orçamento", style="magenta")
    
    # Itera sobre cada linha retornada pela consulta
    for row in cursor:
        # Desempacota cada linha nos campos "título" e "orçamento"
        titulo, orcamento = row
        
        # Adiciona uma nova linha à tabela com os dados de "título" e "orcamento"
        table.add_row(titulo, str(orcamento))
    
    # Imprime a tabela com os resultados no console
    console.print(table)

# Função para exibir os 10 filmes com maiores bilheterias
def filmes_maiores_bilheterias(conn):
    
    # Consulta SQL para obter os 10 filmes com maiores bilheterias
    consulta = """
        SELECT title, revenue
        FROM filmes
        ORDER BY revenue DESC
        LIMIT 10
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="10 filmes com maiores bilheterias")
    table.add_column("Título", style="cyan")
    table.add_column("Bilheteria", style="magenta")
    
    # Itera sobre cada linha retornada pela consulta
    for row in cursor:
        # Desempacota cada linha nos campos "título" e "bilheteria"
        titulo, bilheteria = row
        
        # Adiciona uma nova linha à tabela com os dados de "título" e "bilheteria"
        table.add_row(titulo, str(bilheteria))
    
    # Imprime a tabela com os resultados no console
    console.print(table)

# Função para exibir os 10 filmes com maiores retornos sobre o investimento
def filmes_maiores_lucros(conn):
    
    # Consulta SQL para obter os 10 filmes com maiores retornos sobre o investimento
    consulta = """
        SELECT title, revenue, budget, (revenue / budget) AS retorno_investimento
        FROM filmes
        WHERE budget > 0
        ORDER BY retorno_investimento DESC
        LIMIT 10
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="10 filmes com maiores retornos sobre o investimento")
    table.add_column("Título", style="cyan")
    table.add_column("Retorno", style="magenta")
    
    # Itera sobre cada linha retornada pela consulta
    for row in cursor:
        # Desempacota a linha nos campos "título" e "retorno_investimento"
        titulo, _, _, retorno_investimento = row
        
        # Adiciona uma nova linha à tabela com o título do filme e o retorno sobre o investimento
        table.add_row(titulo, str(retorno_investimento))
    
    # Imprime a tabela com os resultados no console
    console.print(table)

# Função para exibir os 10 filmes com alta popularidade, mas baixa média de votos
def filmes_alta_popularidade_baixo_votos(conn):
    
    # Consulta SQL para obter os 10 filmes com alta popularidade e baixa média de votos
    consulta = """
        SELECT title, popularity, vote_average
        FROM filmes
        WHERE popularity > (SELECT AVG(popularity) FROM filmes)
        AND vote_average < (SELECT AVG(vote_average) FROM filmes)
        ORDER BY popularity DESC
        LIMIT 10
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="10 filmes com alta popularidade, mas baixa média de votos")
    table.add_column("Título", style="cyan")
    table.add_column("Popularidade", style="magenta")
    table.add_column("Média de votos", style="green")
    
    # Itera sobre cada linha retornada pela consulta
    for row in cursor:
        # Desempacota cada linha nos campos "título", "popularidade" e "média de votos"
        titulo, popularidade, media_votos = row
        
        # Adiciona uma nova linha à tabela com os dados de "título", "popularidade" e "média de votos"
        table.add_row(titulo, str(popularidade), str(media_votos))
    
    # Imprime a tabela com os resultados no console
    console.print(table)

# Função para exibir os 10 filmes com baixa popularidade, mas alta média de votos
def filmes_baixa_popularidade_alta_votos(conn):
    
    # Consulta SQL para obter os 10 filmes com baixa popularidade e alta média de votos
    consulta = """
        SELECT title, popularity, vote_average
        FROM filmes
        WHERE popularity < (SELECT AVG(popularity) FROM filmes)
        AND vote_average > (SELECT AVG(vote_average) FROM filmes)
        ORDER BY vote_average DESC
        LIMIT 10
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="10 filmes com baixa popularidade, mas alta média de votos")
    table.add_column("Título", style="cyan")
    table.add_column("Popularidade", style="magenta")
    table.add_column("Média de votos", style="green")
    
    # Itera sobre cada linha retornada pela consulta
    for row in cursor:
        # Desempacota cada linha nos campos "título", "popularidade" e "média de votos"
        titulo, popularidade, media_votos = row
        
        # Adiciona uma nova linha à tabela com os dados de "título", "popularidade" e "média de votos"
        table.add_row(titulo, str(popularidade), str(media_votos))
    
    # Imprime a tabela com os resultados no console
    console.print(table)

# Função para exibir os 10 filmes com mais participações de diferentes países
def filmes_participacoes_paises(conn):
    
    # Consulta SQL para obter os 10 filmes com mais participações de diferentes países
    consulta = """
        SELECT title, LENGTH(production_countries) - LENGTH(REPLACE(production_countries, ', ', '')) + 1 AS num_paises
        FROM filmes
        ORDER BY num_paises DESC
        LIMIT 10
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="10 filmes com mais participações de diferentes países")
    table.add_column("Título", style="cyan")
    table.add_column("Número de países", style="magenta")
    
    # Itera sobre cada linha retornada pela consulta
    for row in cursor:
        # Desempacota cada linha nos campos "título" e "número de países"
        titulo, num_paises = row
        
        # Adiciona uma nova linha à tabela com os dados de "título" e "número de países"
        table.add_row(titulo, str(num_paises))
    
    # Imprime a tabela com os resultados no console
    console.print(table)

# Função para exibir filmes com títulos idênticos, mas de idiomas diferentes
def filmes_titulos_similares(conn):
    
    # Consulta SQL para obter filmes com títulos idênticos, mas de idiomas diferentes
    consulta = """
        SELECT f1.title, f2.title, f1.id, f2.id, f1.original_language, f2.original_language
        FROM filmes AS f1
        JOIN filmes AS f2 ON f1.title = f2.title AND f1.id != f2.id AND f1.original_language != f2.original_language
        ORDER BY f1.title
        DESC LIMIT 10
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="Filmes com títulos idênticos, mas de idiomas diferentes")
    table.add_column("Título Filme 1", style="cyan")
    table.add_column("Título Filme 2", style="magenta")
    table.add_column("ID Filme 1", style="cyan")
    table.add_column("ID Filme 2", style="magenta")
    table.add_column("Idioma Filme 1", style="cyan")
    table.add_column("Idioma Filme 2", style="magenta")
    
    # Itera sobre cada linha retornada pela consulta
    for row in cursor:
        # Desempacota cada linha nos campos correspondentes
        filme1, filme2, id_filme1, id_filme2, idioma_filme1, idioma_filme2 = row
        
        # Adiciona uma nova linha à tabela com os dados de cada filme
        table.add_row(filme1, filme2, str(id_filme1), str(id_filme2), idioma_filme1, idioma_filme2)
    
    # Imprime a tabela com os resultados no console
    console.print(table)

# Função para retornar os meses em que mais filmes foram lançados
def meses_mais_filmes(conn):
    
    # Consulta SQL para obter o total de filmes por mês, com o nome do mês em português
    consulta = """
    SELECT 
        CASE STRFTIME('%m', release_date)
            WHEN '01' THEN 'Janeiro'
            WHEN '02' THEN 'Fevereiro'
            WHEN '03' THEN 'Março'
            WHEN '04' THEN 'Abril'
            WHEN '05' THEN 'Maio'
            WHEN '06' THEN 'Junho'
            WHEN '07' THEN 'Julho'
            WHEN '08' THEN 'Agosto'
            WHEN '09' THEN 'Setembro'
            WHEN '10' THEN 'Outubro'
            WHEN '11' THEN 'Novembro'
            WHEN '12' THEN 'Dezembro'
            ELSE 'Desconhecido'
        END AS mes_portugues,
        COUNT(*) AS total_filmes
    FROM filmes
    WHERE release_date IS NOT NULL AND release_date != ''
    GROUP BY mes_portugues
    ORDER BY total_filmes DESC
    """
    
    cursor = conn.execute(consulta)
    
    # Criar a tabela para exibir os resultados
    table = Table(title="Meses com mais lançamentos de filmes")
    table.add_column("Mês", style="cyan")
    table.add_column("Total de filmes", style="magenta")
    
    # Adiciona os dados à tabela
    for row in cursor:
        # Desempacota cada linha em duas variáveis
        mes_portugues, total_filmes = row
        # Adiciona uma linha à tabela com os dados
        table.add_row(mes_portugues, str(total_filmes))
    
    # Exibe a tabela no console
    console.print(table)

# Função para exibir os 10 filmes mais populares com a temática Inteligência Artificial (IA)
def filmes_tematica_ia(conn):
    
    # Consulta SQL para obter os 10 filmes mais populares com a temática Inteligência Artificial
    consulta = """
    SELECT title, keywords, popularity 
    FROM filmes 
    WHERE keywords LIKE '%artificial intelligence%' 
    ORDER BY popularity DESC 
    LIMIT 10
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="10 filmes mais populares com a temática IA")
    table.add_column("Filmes", style="cyan")
    table.add_column("Popularidade", style="magenta")
    
    # Itera sobre os resultados retornados pela consulta
    for row in cursor:
        # Desempacota cada linha em duas variáveis
        filmes, _, popularidade = row
        
        # Adiciona uma linha à tabela com os dados
        table.add_row(filmes, str(popularidade))
    
    # Exibe a tabela no console
    console.print(table)

# Função para exibir os filmes melhores avaliados lançados no dia 04/04/1999
def filmes_lancados_04_04_1999(conn):
    
    # Consulta SQL para obter os filmes lançados em 04/04/1999, ordenados por média de votos
    consulta = """
    SELECT title, vote_average, genres, release_date 
    FROM filmes 
    WHERE release_date == '1999-04-04' 
    ORDER BY vote_average DESC 
    LIMIT 10
    """
    
    # Executa a consulta SQL na conexão fornecida
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir os resultados
    table = Table(title="Filmes melhores avaliados lançados no dia 04/04/1999")
    table.add_column("Filmes", style="cyan")
    table.add_column("Média de votos", style="magenta")
    table.add_column("Gêneros", style="blue")
    
    # Itera sobre os resultados retornados pela consulta
    for row in cursor:
        # Desempacota cada linha em três variáveis
        filmes, votos, generos, _ = row
        
        # Adiciona uma linha à tabela com os dados
        table.add_row(filmes, str(votos), generos)
    
    # Exibe a tabela no console
    console.print(table)

# Função para exibir os nomes das colunas de uma tabela
def exibir_nomes_colunas(conn, nome_tabela):
    
    # Consulta para obter informações sobre as colunas da tabela
    consulta = f"PRAGMA table_info({nome_tabela})"
    cursor = conn.execute(consulta)
    
    # Cria uma tabela visual para exibir as colunas
    table = Table(title=f"Colunas da tabela '{nome_tabela}'")
    table.add_column("ID", justify="right")
    table.add_column("Nome da coluna")
    
    # Adiciona as colunas à tabela
    for coluna in cursor:
        table.add_row(str(coluna[0]), coluna[1])
    
    # Imprime a tabela
    console.print(table)



