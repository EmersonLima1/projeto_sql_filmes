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







    








- O método fetchone() é usado para obter o resultado da consulta. O primeiro elemento retornado pela consulta (cursor.fetchone()) é o número total de filmes.
- `fetchone` é um método utilizado em cursors que permite recuperar a próxima linha de resultados de uma consulta SQL. Ele é usado para obter um único registro de cada vez do conjunto de resultados retornado por uma consulta.
- `cursors` são objetos utilizados para interagir com um banco de dados a partir de uma aplicação. Um cursor atua como uma ponte entre a aplicação e o banco de dados, permitindo a execução de consultas e a manipulação de dados de forma eficiente.






