# Projeto de Estatística Aplicada

## 🧑‍💻 Autores  
- Larissa Dantas Alves Ferreira (202421250040) - larissa-ferreira.lf@academico.ifpb.edu.br  
- Renata Morgana Galvíncio Silva (202421250044) - renata.galvincio@academico.ifpb.edu.br  
- Ryan de oliveira sousa (202421250017) - ryan.sousa@academico.ifpb.edu.br
 
## 🎯 Tema e Motivação  
  Este projeto tem como objetivo analisar estatisticamente os jogos eletrônicos mais vendidos nas últimas décadas até 2024 com base nos dados da plataforma VGChartz. O foco é investigar padrões de vendas globais e regionais, considerando aspectos como gênero, console, desenvolvedora, distribuidora, pontuação crítica, dentre outros.
  A relevância do tema está na expressiva influência que a indústria dos videogames exerce tanto na economia quanto na cultura digital contemporânea. Por meio de análises estatísticas descritivas, busca-se identificar tendências de consumo, distribuição de vendas por região, plataformas mais bem-sucedidas e a relação entre crítica especializada e desempenho comercial.

## 📊 Conjunto de Dados Selecionado  
- **Nome do conjunto de dados:**  
  Video Game Sales 2024

- **Fonte:**  
  https://www.kaggle.com/datasets/asaniczka/video-game-sales-2024/data?select=vgchartz-2024.csv

- **Descrição breve:**  
  O conjunto de dados reúne informações sobre jogos lançados e vendidos até o ano de 2024. Cada linha representa um título, com variáveis como nome do jogo (`title`), plataform (`console`), gênero (`genre`), desenvolvedora (`developer`), distribuidora (`publisher`), data de lançamento (`release_date`), pontuação da crítica (`critic_score`) e vendas totais (`total_sales`) em milhões de unidades, além de colunas que discriminam o volume de vendas por região geográfica: América do Norte (`na_sales`), Japão (`jp_sales`), Europa (`pal_sales`), outros países (`other_sales`). 

- **Justificativa para a escolha:**  
  Este conjunto de dados permite análises estatísticas descritivas robustas com variáveis numéricas (vendas) e categóricas (gênero, plataforma, desenvolvedora, etc). É possível comparar médias de vendas por região, identificar os gêneros mais lucrativos e entender o comportamento do mercado de acordo com a plataforma, permitindo investigações relevantes sobre o desempenho comercial dos jogos em diferentes contextos.

---

## ❓ Perguntas ou Hipóteses  
  1. Quais são os jogos com maiores vendas globais até 2024?
  2. Quais gêneros de jogos registraram maior média de vendas?
  3. Quais consoles se destacaram em termos de volume total de vendas?
  4. Existe diferença significativa entre as vendas nas principais regiões (América do Norte, Europa, Japão)?
  5. Jogos com maiores notas da crítica apresentam também maiores vendas?
  6. Qual distribuidora concentrou os jogos mais vendidos?

## 🔍 Metodologia  
Neste projeto, será realizada uma análise estatística descritiva com foco em:

1. **Análise Exploratória de Dados (EDA)**: verificação da estrutura dos dados, valores ausentes e outliers.
2. **Estatística Descritiva**: cálculo de média, moda, mediana e frequências para variáveis como `total_sales`, `genre`, `console`, `publisher` e `release_year`.
3. **Visualização de Dados**:
   - Gráficos de barras para comparar vendas por gênero, plataforma e região.
   - Gráficos de pizza para distribuição percentual de gêneros ou plataformas.
   - Gráficos de linha para evolução do número de lançamentos ao longo do tempo.
   - Boxplot: comparar a distribuição de vendas por plataforma ou por região.
4. **Análise Regional**: comparações entre vendas nas regiões `na_sales`, `jp_sales`, `pal_sales` e `other_sales`.
5. **Correlação**: análise da relação entre `critic_score` e `total_sales` para investigar a influência da crítica nas vendas.

## 🛠️ Ferramentas Utilizadas  
O projeto será desenvolvido com o uso das seguintes ferramentas e tecnologias:

- **Visual Studio Code (VS Code)** - editor principal para escrita e organização do código.
- **Google Colab** - ambiente online para execução interativa do código Python.
- **Python** - linguagem de programação utilizada para análise e manipulação de dados.
- **Pandas** - biblioteca Python para tratamento, organização e análise estatística de dados.
- **Kaggle** - plataforma de onde foi obtido o conjunto de dados utilizado no projeto.
- **GitHub** - para versionamento e organização do repositório do projeto.

## 📊 Acesse o notebook no Google Colab:  
- **Atividade 2** [🔗 Clique aqui para abrir no Colab](https://colab.research.google.com/github/gilgameshr3rr/projeto-estatistica/blob/project-edition-larissa/atividade-02/analise.ipynb)

## 📈 Resultados  
*A preencher após as análises.*  
Resumo visual e interpretativo dos principais achados.

## 📌 Conclusões  
*A preencher no final do projeto.*  
Síntese dos aprendizados e implicações das análises realizadas.

## ⚠️ Limitações e Trabalhos Futuros  
*A preencher no final do projeto.*  
Quais foram as limitações do estudo e o que poderia ser feito com mais tempo ou dados adicionais.

---

