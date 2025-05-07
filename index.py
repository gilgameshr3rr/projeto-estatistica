from kaggle.api.kaggle_api_extended import KaggleApi
import os

# Cria a pasta 'dados' 
os.makedirs("dados", exist_ok=True)

# Autenticação com a API do Kaggle
api = KaggleApi()
api.authenticate()

# Baixa e descompacta o dataset
api.dataset_download_files(
    'asaniczka/video-game-sales-2024',
    path='dados/',
    unzip=True
)

print("Download concluído com sucesso!")






