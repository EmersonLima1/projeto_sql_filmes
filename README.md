# Explorando um conjunto de dados sobre filmes com SQL e Python

<div align="justify">

Este projeto é focado em consultas SQL através de métodos Python, utilizando o conjunto de dados do TMDb (The Movie Database), uma base de dados abrangente que fornece informações sobre filmes, incluindo detalhes como títulos, avaliações, datas de lançamento, receitas, gêneros e muito mais. O projeto trabalha com um conjunto de dados contendo uma coleção de 1.000.000 de filmes da base de dados do TMDb.

Sinta-se à vontade para explorar os scripts Python que executam consultas SQL no banco de dados SQLite, aprimorando suas habilidades e conhecimento nas duas linguagens enquanto lida com um conjunto de dados rico e diversificado!

## Obtenção e Transformação da Base de Dados

A base de dados utilizada neste projeto foi obtida a partir do [Kaggle](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies/data), onde foi baixado o arquivo CSV contendo o conjunto de dados do TMDb (The Movie Database). O conjunto de dados é uma coleção de aproximadamente 1.000.000 de filmes com informações detalhadas, incluindo títulos, avaliações, datas de lançamento, receitas, gêneros e muito mais.

Após baixar o arquivo CSV, ele foi transformado em um banco de dados usando o SQLite3. O SQLite3 é um sistema de gerenciamento de banco de dados relacional leve e embutido, que é amplamente utilizado em aplicações de desktop e mobile devido à sua facilidade de uso e eficiência. Ele permite a execução de consultas SQL e é compatível com a linguagem Python.

A transformação do arquivo CSV em um banco de dados SQLite3 facilita a manipulação dos dados e a realização de consultas eficientes usando SQL em conjunto com Python.

## Conteúdo do Repositório

Neste repositório, você encontrará:

- **Códigos Python**: Os scripts Python usados no projeto estão disponíveis para download e visualização. Esses códigos demonstram como utilizar Python em conjunto com SQL para realizar consultas no banco de dados de filmes.

- **Banco de Dados `filmes.db`**: O banco de dados `filmes.db` é uma versão do conjunto de dados do TMDb (The Movie Database) transformada em um banco de dados SQLite3. Ele contém aproximadamente 1.000.000 de filmes com informações detalhadas, incluindo títulos, avaliações, datas de lançamento, receitas, gêneros e muito mais.

## Explicação das Consultas Utilizadas no Projeto

Neste projeto, você terá a oportunidade de aprender sobre as consultas SQL utilizadas em conjunto com Python para manipular o banco de dados `filmes.db`. As consultas são feitas com base nas escolhas do usuário durante a execução do código `app.py`.

Quando o código `app.py` é executado, uma interface de terminal é exibida, apresentando diferentes opções ao usuário. Cada opção corresponde a uma consulta específica a ser executada no banco de dados.

Ao escolher uma opção, um método correspondente é chamado a partir do arquivo `funcoes_db.py`. Cada método executa uma consulta SQL diferente no banco de dados `filmes.db` para retornar as informações solicitadas pelo usuário.

O código `criar_banco.py` é responsável por transformar o arquivo CSV baixado do Kaggle em um banco de dados SQLite3 (`filmes.db`). Esse processo facilita a manipulação e a realização de consultas eficientes no banco de dados usando SQL em conjunto com Python.

Nas seções seguintes, você encontrará explicações detalhadas de cada uma das consultas utilizadas no projeto:

### Consulta para contar o número de filmes na tabela

    SELECT COUNT(*) FROM filmes

- A consulta SQL (SELECT COUNT(*) FROM filmes) é usada para contar o número total de filmes na tabela filmes. Ela retorna um único valor que representa o total de filmes.
- `SELECT COUNT(*)`: A cláusula SELECT é usada para especificar quais colunas ou expressões desejamos recuperar dos dados. Neste caso, estamos utilizando a função agregada COUNT(*) para contar o número total de linhas na tabela filmes. O asterisco * indica que queremos contar todas as linhas.
- `FROM filmes`: A cláusula FROM especifica de qual tabela os dados serão selecionados. Neste caso, a tabela é filmes, que contém os dados sobre filmes.

### Consulta para contar o número de filmes que têm o Português (pt) como idioma original

    SELECT COUNT(*) FROM filmes WHERE original_language = 'pt'

- A consulta SQL (SELECT COUNT(*) FROM filmes WHERE original_language = 'pt') é usada para contar o número total de filmes na tabela filmes onde o idioma original (original_language) é pt (Português).
- `WHERE original_language = 'pt'`: A cláusula WHERE é usada para filtrar os filmes com base na condição especificada. Neste caso, estamos filtrando os filmes cujo idioma original (original_language) é 'pt' (Português).

### Consulta para contar quantos filmes foram lançados entre os anos 2000 e 2023

    SELECT COUNT(*) FROM filmes WHERE release_date >= '2000-01-01' AND release_date <= '2023-12-31'

- A consulta SQL (SELECT COUNT(*) FROM filmes WHERE release_date >= '2000-01-01' AND release_date <= '2023-12-31') conta o número de filmes com datas de lançamento (release_date) entre 1º de janeiro de 2000 e 31 de dezembro de 2023.
- `WHERE release_date >= '2000-01-01' AND release_date <= '2023-12-31'`: A cláusula WHERE filtra os filmes com base nas condições especificadas. Estamos selecionando apenas os filmes cuja data de lançamento (release_date) esteja entre 1º de janeiro de 2000 e 31 de dezembro de 2023.

### Consulta para listar os 10 filmes com as melhores avaliações médias

    SELECT title, vote_average FROM filmes ORDER BY vote_average DESC LIMIT 10

- A consulta SQL (SELECT title, vote_average FROM filmes ORDER BY vote_average DESC LIMIT 10) é usada para selecionar o título (title) e a avaliação média (vote_average) dos 10 filmes com as maiores avaliações médias. A consulta ordena (ORDER BY) os resultados em ordem decrescente (DESC) de avaliação média (vote_average) e limita (LIMIT) a quantidade de resultados a 10 filmes.
- `ORDER BY vote_average`: A cláusula ORDER BY é usada para ordenar os resultados com base na avaliação média (vote_average).
- `DESC`: A palavra-chave DESC indica que os resultados devem ser ordenados em ordem decrescente (da maior para a menor) com base na avaliação média.
- `LIMIT 10`: A cláusula LIMIT especifica o número máximo de resultados a serem retornados. Neste caso, estamos limitando os resultados aos 10 filmes com as maiores avaliações médias.

### Consulta para listar os 10 filmes com as piores avaliações médias

    SELECT title, vote_average FROM filmes ORDER BY vote_average ASC LIMIT 10

- A consulta SQL (SELECT title, vote_average FROM filmes ORDER BY vote_average ASC LIMIT 10) seleciona os títulos (title) e as avaliações médias (vote_average) dos filmes da tabela filmes. A consulta ordena os resultados por vote_average em ordem ascendente (ASC), o que significa que os filmes com as avaliações mais baixas aparecerão primeiro.
- `ASC`: A palavra-chave ASC indica que os resultados devem ser ordenados em ordem ascendente (do menor para o maior) com base na avaliação média.

### Consulta para listar os 10 gêneros de filmes com as melhores avaliações médias

    SELECT genres, AVG(vote_average) AS media_avaliacao FROM filmes GROUP BY genres ORDER BY media_avaliacao DESC LIMIT 10

- A consulta SQL (SELECT genres, AVG(vote_average) AS media_avaliacao FROM filmes GROUP BY genres ORDER BY media_avaliacao DESC LIMIT 10) é usada para selecionar os gêneros de filmes (genres) e a avaliação média (media_avaliacao) dos 10 gêneros de filmes com as avaliações médias mais altas.
- `GROUP BY genres`: A cláusula GROUP BY agrupa os resultados com base nos gêneros de filmes (genres), para calcular a média das avaliações para cada gênero.
- `AVG(vote_average) AS media_avaliacao`: A função agregada AVG(vote_average) calcula a média das avaliações (vote_average) de todos os filmes de cada gênero especificado na cláusula GROUP BY genres. Ou seja, ela gera a média das avaliações para cada gênero de filmes.
- Ao usar AS media_avaliacao, estamos renomeando o resultado da função AVG(vote_average) para media_avaliacao, facilitando a identificação dos dados no resultado da consulta. Isso ajuda a tornar a consulta mais legível, permitindo que o resultado da média das avaliações seja acessado com o nome media_avaliacao nas instruções posteriores.

### Consulta para os 10 filmes de ação mais populares que têm o Inglês (en) como idioma original lançados a partir de 2023

    SELECT title, popularity, original_language, release_date, genres FROM filmes WHERE genres LIKE '%Action%' AND original_language = 'en' AND release_date > '2022-12-31' ORDER BY popularity DESC LIMIT 10

- A consulta SQL (SELECT title, popularity, original_language, release_date, genres FROM filmes WHERE genres LIKE '%Action%' AND original_language = 'en' AND release_date > '2022-12-31' ORDER BY popularity DESC LIMIT 10) é usada para selecionar os títulos (title), pontuações de popularidade (popularity), idiomas originais (original_language), datas de lançamento (release_date) e gêneros (genres) dos 10 filmes de ação mais populares em inglês lançados a partir de 2023.
- `SELECT title, popularity, original_language, release_date, genres`: A cláusula SELECT especifica as colunas que queremos recuperar da tabela filmes: título do filme (title), pontuação de popularidade (popularity), idioma original (original_language), data de lançamento (release_date) e gêneros (genres).
- `WHERE genres LIKE '%Action%'`: A cláusula WHERE filtra os resultados para incluir apenas os filmes cujo gênero (genres) contém a palavra "Action". O operador LIKE com o uso de curinga (%) permite combinar qualquer gênero que contenha "Action".
- O operador LIKE é um operador SQL utilizado para realizar buscas com base em padrões de texto.
- O curinga % é um caractere especial usado com o operador LIKE para representar qualquer sequência de caracteres. 
- `AND original_language` = 'en': Filtra os resultados para incluir apenas os filmes cujo idioma original (original_language) seja inglês ('en').
- `AND release_date > '2022-12-31'`: Filtra os resultados para incluir apenas os filmes com data de lançamento (release_date) posterior a 31 de dezembro de 2022.

### Consulta para listar os 10 filmes cuja duração é maior que a média de duração dos gêneros desses filmes

#### Consulta principal
    SELECT f.title, f.genres, f.runtime, md.media_duracao
    FROM filmes AS f
    JOIN media_duracao_por_genero AS md ON f.genres = md.genres
    WHERE f.runtime > md.media_duracao
    ORDER BY f.runtime DESC
    LIMIT 10

 - `SELECT f.title, f.genres, f.runtime, md.media_duracao`: Seleciona as colunas title (título do filme), genres (gêneros do filme), runtime (duração do filme em minutos), e media_duracao (média de duração dos gêneros) das tabelas filmes (abreviada como f) e media_duracao_por_genero (abreviada como md).
 - `FROM filmes AS f`: Especifica a tabela de origem (filmes) para a consulta principal, referenciada pelo alias f.
 - `JOIN media_duracao_por_genero AS md ON f.genres = md.genres`: Realiza um join entre as tabelas filmes e media_duracao_por_genero, correspondendo os gêneros (genres) de ambas as tabelas.
 - `WHERE f.runtime > md.media_duracao`: Filtra os resultados para incluir apenas os filmes (f.runtime) com duração maior que a média de duração dos gêneros (md.media_duracao) correspondentes.
 - `ORDER BY f.runtime DESC`: Ordena os resultados com base na duração (f.runtime) em ordem decrescente (do maior para o menor).
 - `LIMIT 10`: Limita o resultado a apenas 10 filmes.

##### Subconsulta
    WITH media_duracao_por_genero AS (
    SELECT genres, AVG(runtime) as media_duracao
    FROM filmes
    GROUP BY genres)

- `WITH media_duracao_por_genero AS`: Define uma subconsulta (ou CTE, Common Table Expression) chamada media_duracao_por_genero.
- `SELECT genres, AVG(runtime) as media_duracao`: Seleciona os gêneros (genres) dos filmes e calcula a média de duração (AVG(runtime)) para cada gênero.
- `FROM filmes`: Especifica a tabela filmes como a origem dos dados para calcular a média de duração.
- `GROUP BY genres`: Agrupa os resultados pelos gêneros para calcular a média de duração separadamente para cada gênero.

### Consulta para retornar o total de filmes por ano de lançamento

    SELECT STRFTIME('%Y', release_date) AS ano, COUNT(*) AS total_filmes
    FROM filmes
    WHERE release_date IS NOT NULL AND release_date != ''
    GROUP BY ano
    ORDER BY total_filmes DESC

 - A consulta SQL em questão é usada para contar o total de filmes lançados por ano. Os dados são agrupados por ano de lançamento (ano) e a consulta retorna o total de filmes (total_filmes) para cada ano.
 - `SELECT STRFTIME('%Y', release_date) AS ano, COUNT(*) AS total_filmes`: Seleciona o ano de lançamento (ano) a partir da data de lançamento (release_date) usando a função STRFTIME com o formato de ano ('%Y') e o total de filmes (total_filmes) usando a função agregada COUNT(*).
 - `WHERE release_date IS NOT NULL AND release_date != ''`: Filtra os resultados para incluir apenas filmes com datas de lançamento válidas (não nulas e não vazias).
 - `GROUP BY ano`: Agrupa os resultados por ano de lançamento (ano) para calcular o total de filmes em cada ano.
 - `ORDER BY total_filmes DESC`: Ordena os resultados com base no total de filmes em ordem decrescente (do maior para o menor), para destacar os anos com mais lançamentos.

### Consulta para calcular o total de filmes por idioma

    SELECT original_language, COUNT(*) AS total_filmes
    FROM filmes
    WHERE original_language IS NOT NULL AND original_language != ''
    GROUP BY original_language
    ORDER BY total_filmes DESC

 - A consulta SQL em questão é usada para contar o total de filmes por idioma. A consulta agrupa os resultados pelo idioma original (original_language) dos filmes e retorna o total de filmes (total_filmes) para cada idioma.
 - `SELECT original_language, COUNT(*) AS total_filmes`: Seleciona o idioma original (original_language) e o total de filmes (total_filmes) usando a função agregada COUNT(*).
 - `GROUP BY original_language`: Agrupa os resultados pelo idioma original (original_language) para calcular o total de filmes em cada idioma.

### Consulta para retornar os 10 filmes com os maiores orçamentos

    SELECT title, budget
    FROM filmes
    ORDER BY budget DESC
    LIMIT 10

 - A consulta SQL em questão é usada para obter esses filmes, ordenando-os em ordem decrescente de orçamento.
 - `SELECT title, budget`: Seleciona o título (title) e o orçamento (budget) dos filmes.
 - `ORDER BY budget DESC`: Ordena os resultados pela coluna budget (orçamento) em ordem decrescente (DESC), o que significa que os filmes com os maiores orçamentos aparecerão primeiro na lista.

### Consulta para retornar os 10 filmes com as maiores bilheterias

    SELECT title, revenue
    FROM filmes
    ORDER BY revenue DESC
    LIMIT 10

 - A consulta SQL em questão obtém esses filmes, ordenando-os em ordem decrescente de bilheteria.
 - `SELECT title, revenue`: Seleciona o título (title) e a bilheteria (revenue) dos filmes.
 - `ORDER BY revenue DESC`: Ordena os resultados pela coluna revenue (bilheteria) em ordem decrescente (DESC), ou seja, os filmes com as maiores bilheterias aparecerão primeiro na lista.

### Consulta para retornar os 10 filmes com os maiores retornos sobre o investimento

    SELECT title, revenue, budget, (revenue / budget) AS retorno_investimento
    FROM filmes
    WHERE budget > 0
    ORDER BY retorno_investimento DESC
    LIMIT 10

 - A consulta SQL em questão obtém esses filmes, calculando o retorno sobre o investimento para cada um deles.
 - `SELECT title, revenue, budget, (revenue / budget) AS retorno_investimento`: Seleciona o título (title), a bilheteria (revenue), o orçamento (budget) e calcula o retorno sobre o investimento (revenue / budget) para cada filme. O cálculo do retorno sobre o investimento é feito dividindo a receita pelo orçamento de cada filme.
 - `WHERE budget > 0`: Filtra os resultados para considerar apenas filmes que tenham um orçamento (budget) maior que zero.
 - `ORDER BY retorno_investimento DESC`: Ordena os resultados pela coluna retorno_investimento em ordem decrescente (DESC), ou seja, os filmes com os maiores retornos sobre o investimento aparecerão primeiro na lista.

### Consulta para obter os 10 filmes com alta popularidade e baixa média de votos

    SELECT title, popularity, vote_average
    FROM filmes
    WHERE popularity > (SELECT AVG(popularity) FROM filmes)
    AND vote_average < (SELECT AVG(vote_average) FROM filmes)
    ORDER BY popularity DESC
    LIMIT 10

 - A consulta SQL em questão obtém os 10 filmes com alta popularidade, mas com baixa média de votos.
 - `SELECT title, popularity, vote_average`: Seleciona o título (title), a popularidade (popularity) e a média de votos (vote_average) para cada filme.
 - `WHERE popularity > (SELECT AVG(popularity) FROM filmes)`: Filtra os filmes com popularidade (popularity) maior que a média de popularidade de todos os filmes.
 - `AND vote_average < (SELECT AVG(vote_average) FROM filmes)`: Adiciona uma condição para filtrar os filmes com média de votos (vote_average) menor que a média de votos de todos os filmes.
 - `ORDER BY popularity DESC`: Ordena os resultados pela coluna popularity em ordem decrescente (DESC), ou seja, os filmes com a maior popularidade aparecerão primeiro na lista.
 - `LIMIT 10`: Limita a quantidade de resultados a 10 filmes, selecionando apenas os 10 filmes com alta popularidade e baixa média de votos.

### Consulta para obter os 10 filmes com baixa popularidade e alta média de votos

    SELECT title, popularity, vote_average
    FROM filmes
    WHERE popularity < (SELECT AVG(popularity) FROM filmes)
    AND vote_average > (SELECT AVG(vote_average) FROM filmes)
    ORDER BY vote_average DESC
    LIMIT 10

 - A consulta SQL em questão obtém os 10 filmes com baixa popularidade, mas com alta média de votos.
 - `SELECT title, popularity, vote_average`: Seleciona o título (title), a popularidade (popularity) e a média de votos (vote_average) para cada filme.
 - `WHERE popularity < (SELECT AVG(popularity) FROM filmes)`: Filtra os filmes com popularidade (popularity) menor que a média de popularidade de todos os filmes.
 - `AND vote_average > (SELECT AVG(vote_average) FROM filmes)`: Adiciona uma condição para filtrar os filmes com média de votos (vote_average) maior que a média de votos de todos os filmes.
 - `ORDER BY vote_average DESC`: Ordena os resultados pela coluna vote_average em ordem decrescente (DESC), ou seja, os filmes com a maior média de votos aparecerão primeiro na lista.
 - `LIMIT 10`: Limita a quantidade de resultados a 10 filmes, selecionando apenas os 10 filmes com baixa popularidade e alta média de votos.

### Consulta para obter os 10 filmes com mais participações de diferentes países

    SELECT title, LENGTH(production_countries) - LENGTH(REPLACE(production_countries, ', ', '')) + 1 AS num_paises
    FROM filmes
    ORDER BY num_paises DESC
    LIMIT 10

- A consulta SQL em questão obtém os 10 filmes com mais participações de diferentes países.
- `SELECT title, LENGTH(production_countries) - LENGTH(REPLACE(production_countries, ', ', '')) + 1 AS num_paises`: Seleciona o título (title) e calcula o número de participações de diferentes países (num_paises) para cada filme. O cálculo de num_paises é feito contando o número de vírgulas (, ) na coluna production_countries e adicionando 1 para obter o total de participações de países.
- `ORDER BY num_paises DESC`: Ordena os resultados pela coluna num_paises em ordem decrescente (DESC), ou seja, os filmes com mais participações de diferentes países aparecerão primeiro na lista.

### Consulta para obter filmes com títulos idênticos, mas de idiomas diferentes

    SELECT f1.title, f2.title, f1.id, f2.id, f1.original_language, f2.original_language
    FROM filmes AS f1
    JOIN filmes AS f2 ON f1.title = f2.title AND f1.id != f2.id AND f1.original_language != f2.original_language
    ORDER BY f1.title DESC LIMIT 10

- A consulta SQL em questão obtém os filmes que têm títulos idênticos, mas que são de idiomas diferentes.
- `SELECT f1.title, f2.title, f1.id, f2.id, f1.original_language, f2.original_language`: Seleciona os títulos, IDs e idiomas de dois filmes (f1 e f2) que possuem títulos idênticos, mas são de idiomas diferentes.
- `FROM filmes AS f1`: Especifica a tabela filmes como a origem dos dados para f1.
- `JOIN filmes AS f2 ON f1.title = f2.title AND f1.id != f2.id AND f1.original_language != f2.original_language`: Realiza uma junção (JOIN) entre os filmes f1 e f2 com base nos títulos idênticos (f1.title = f2.title), certificando-se de que não sejam o mesmo filme (f1.id != f2.id) e que tenham idiomas diferentes (f1.original_language != f2.original_language).
- `ORDER BY f1.title DESC LIMIT 10`: Ordena os resultados pelo título de f1 em ordem decrescente (DESC) e limita a quantidade de resultados a 10 pares de filmes com títulos idênticos e idiomas diferentes.

### Consulta para obter os meses com mais lançamentos de filmes

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

 - A consulta SQL em questão obtém os meses em português em que houve o maior número de lançamentos de filmes, bem como o total de filmes lançados em cada mês.
 - `SELECT`: Seleciona o mês em português e o total de filmes lançados nesse mês.
 - `CASE STRFTIME('%m', release_date)`: Utiliza uma função CASE para converter o mês da data de lançamento (release_date) em seu equivalente em português. O formato %m extrai  o mês da data.
 - `WHEN '01' THEN 'Janeiro'`: Traduz o número do mês para o nome do mês em português. Isso é feito para todos os meses de janeiro a dezembro.
 - `END AS mes_portugues`: A saída do CASE é renomeada para mes_portugues.
 - `COUNT(*) AS total_filmes`: Conta o número total de filmes lançados em cada mês e renomeia essa contagem para total_filmes.
 - `FROM filmes`: Especifica a tabela filmes como a origem dos dados.
 - `WHERE release_date IS NOT NULL AND release_date != ''`: Filtra os resultados para garantir que a data de lançamento (release_date) não seja nula ou vazia.
 - `GROUP BY mes_portugues`: Agrupa os filmes por mês em português.
 - `ORDER BY total_filmes DESC`: Ordena os resultados em ordem decrescente com base no total de filmes lançados por mês.

### Consulta para obter os 10 filmes mais populares com a temática Inteligência Artificial

    SELECT title, keywords, popularity 
    FROM filmes 
    WHERE keywords LIKE '%artificial intelligence%' 
    ORDER BY popularity DESC 
    LIMIT 10

 - Essa consulta SQL busca os filmes que contêm a palavra-chave "artificial intelligence" em seus dados de palavras-chave (keywords), e ordena os resultados pela popularidade em ordem decrescente e limita o resultado aos 10 filmes mais populares.
 - `SELECT title, keywords, popularity`: Seleciona o título (title), palavras-chave (keywords) e popularidade (popularity) dos filmes.
 - `WHERE keywords LIKE '%artificial intelligence%'`: Filtra os resultados para incluir apenas filmes que contenham a palavra-chave "artificial intelligence" em seus dados de palavras-chave (keywords).

### Consulta para obter os filmes mais populares lançados no dia 04/04/1999

    SELECT title, vote_average, genres, release_date 
    FROM filmes 
    WHERE release_date == '1999-04-04' 
    ORDER BY vote_average DESC 
    LIMIT 10

 - Essa consulta SQL obtém os filmes mais populares lançados no dia 04/04/1999.
 - `SELECT title, vote_average, genres, release_date`: Seleciona o título (title), média de votos (vote_average), gêneros (genres) e data de lançamento (release_date) dos filmes.
 - `WHERE release_date == '1999-04-04'`: Filtra os resultados para incluir apenas filmes lançados na data 04/04/1999.

### Consulta SQL para obter informações sobre as colunas da tabela

    PRAGMA table_info(nome_tabela)

 - A instrução SQL em questão exibe os nomes das colunas de uma tabela específica em um banco de dados SQLite. Ela realiza uma consulta usando a instrução PRAGMA table_info para obter informações sobre as colunas da tabela especificada.

## Conceitos importantes

- `fetchone` é um método utilizado em cursors que permite recuperar a próxima linha de resultados de uma consulta SQL. Ele é usado para obter um único registro de cada vez do conjunto de resultados retornado por uma consulta.
- `fetchall`: É um método utilizado em cursors que permite recuperar todas as linhas de resultados de uma consulta SQL de uma só vez. O resultado é uma lista de tuplas, com cada tupla representando uma linha do conjunto de resultados.
- `cursors` são objetos utilizados para interagir com um banco de dados a partir de uma aplicação. Um cursor atua como uma ponte entre a aplicação e o banco de dados, permitindo a execução de consultas e a manipulação de dados de forma eficiente.
- `execute`: É um método utilizado em cursors para executar consultas SQL ou comandos DML (Data Manipulation Language) como INSERT, UPDATE ou DELETE. O método aceita uma string com a consulta ou comando SQL a ser executado.






