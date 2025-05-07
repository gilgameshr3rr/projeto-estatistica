import pandas as pd

# Testando
caminho_arquivo = 'dados/vgchartz-2024.csv'

df = pd.read_csv(caminho_arquivo)

try:
    df = pd.read_csv(caminho_arquivo)
    print("Visualizando as 5 primeiras linhas:")
    print(df.head(5))
except FileNotFoundError:
    print(f"Arquivo '{caminho_arquivo}' não encontrado. Execute 'index.py' primeiro.")


# Acessando outros dados 

print("Tamanho do dataset:")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")

print("\nNomes das colunas:")
print(df.columns)

print("\nInformações gerais:")
df.info()