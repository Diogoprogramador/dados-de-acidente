import pandas as pd
import matplotlib.pyplot as plt



# Carregar os dados (substitua o caminho do arquivo CSV)
file_path = "datatran2024.csv"  # Substitua pelo caminho correto
df = pd.read_csv(file_path, delimiter=";", encoding='latin1')

# Converter a coluna 'horario' para formato datetime, especificando o formato
df['horario'] = pd.to_datetime(df['horario'], format='%H:%M:%S', errors='coerce')

# Agora, você pode acessar a hora com .dt.hour sem o aviso
df['hora'] = df['horario'].dt.hour

# Exibir as primeiras linhas para verificar
print(df[['horario', 'hora']].head())


# 1. Top 10 Municípios com Mais Acidentes
top_municipios = df['municipio'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_municipios.plot(kind='bar', color='skyblue')
plt.title('Top 10 Municípios com Mais Acidentes')
plt.xlabel('Município')
plt.ylabel('Número de Acidentes')
plt.xticks(rotation=45, ha='right')  # Rotação para os rótulos
plt.tight_layout()
plt.show()

# 2. Top 10 Causas de Acidente
top_causas = df['causa_acidente'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_causas.plot(kind='bar', color='lightcoral')
plt.title('Top 10 Causas de Acidente')
plt.xlabel('Causa do Acidente')
plt.ylabel('Número de Acidentes')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 3. Distribuição dos Acidentes por Dia da Semana
top_dia_semana = df['dia_semana'].value_counts().sort_index()  # Ordenar para dias da semana em ordem
plt.figure(figsize=(10, 6))
top_dia_semana.plot(kind='bar', color='lightgreen')
plt.title('Distribuição dos Acidentes por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Número de Acidentes')
plt.tight_layout()
plt.show()

# 4. Distribuição de Acidentes por Faixa de Horário
# Podemos criar uma faixa de horário se tivermos dados de hora
# Caso 'horario' esteja no formato de string (por exemplo '14:30:00'), convertemos para hora
df['horario'] = pd.to_datetime(df['horario'], errors='coerce').dt.hour
top_horarios = df['horario'].value_counts().sort_index()  # Ordena por hora
plt.figure(figsize=(10, 6))
top_horarios.plot(kind='bar', color='lightblue')
plt.title('Distribuição de Acidentes por Faixa de Horário')
plt.xlabel('Hora do Dia')
plt.ylabel('Número de Acidentes')
plt.tight_layout()
plt.show()

# 5. Distribuição de Feridos por Tipo (Leves, Graves, Ilesos, etc.)
# Criar gráfico de barras para a quantidade de feridos por tipo
feridos_tipo = df[['feridos_leves', 'feridos_graves', 'ilesos', 'mortos']].sum()
plt.figure(figsize=(10, 6))
feridos_tipo.plot(kind='bar', color='Purple')
plt.title('Distribuição de Feridos por Tipo')
plt.xlabel('Tipo de Ferido')
plt.ylabel('Número de Feridos')
plt.tight_layout()
plt.show()
