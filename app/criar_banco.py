import pandas as pd
import sqlite3

# Leitura do arquivo CSV
df = pd.read_csv('dados/TMDB_movie_dataset_v11.csv')

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('filmes.db')

# Transformação do DataFrame para uma tabela no banco de dados
df.to_sql('filmes', conn, if_exists='replace', index=False)

# Fechamento da conexão
conn.close()
