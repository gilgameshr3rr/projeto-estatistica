import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv('dados/vgchartz-2024.csv')

# Número total de registros e variáveis
num_linhas, num_colunas = df.shape
print(f"Total de registros (linhas): {num_linhas}")
print(f"Total de variáveis (colunas): {num_colunas}")

# Classificação de variáveis
quantitativas = []
qualitativas = []

for coluna in df.columns:
    if pd.api.types.is_numeric_dtype(df[coluna]):
        quantitativas.append(coluna)
    else:
        qualitativas.append(coluna)

print("\nVariáveis quantitativas:")
print(quantitativas)

print("\nVariáveis qualitativas:")
print(qualitativas)

# Tabela resumo
resumo = pd.DataFrame({
    'Variável': quantitativas + qualitativas,
    'Tipo': ['Quantitativa'] * len(quantitativas) + ['Qualitativa'] * len(qualitativas)
})

print("\nTabela resumo das variáveis:")
print(resumo)