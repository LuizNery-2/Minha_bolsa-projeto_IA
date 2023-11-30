import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt


df = pd.read_csv('pda-prouni-2017.csv',  sep =';')
df.head(20)


# Checando duplicatas
duplicates = df.drop_duplicates(subset ="TIPO_BOLSA")
duplicates

# Assuming df is your DataFrame
columns_to_drop = ["CODIGO_EMEC_IES_BOLSA","CPF_BENEFICIARIO_BOLSA", "DT_NASCIMENTO_BENEFICIARIO", "ANO_CONCESSAO_BOLSA"]

# Drop the specified columns
df.drop(columns=columns_to_drop, inplace=True)

df.to_csv("proUni2017_tratados.csv",index=False)

colunas_categoricas = df.select_dtypes(include=['object'])  # Seleciona colunas do tipo 'object'
df.mode()

# Loop pelas colunas categóricas e calcular as frequências
for coluna in colunas_categoricas.columns:
    frequencia = df[coluna].value_counts()
    print(f"Frequência para a coluna '{coluna}':\n{frequencia}\n")

sns.countplot(x='TIPO_BOLSA', data=df, )
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

# Suponha que você queira exibir os 10 maiores dados para cada coluna
top_n = 10

fig, axes = plt.subplots(3, 4, figsize=(45, 30))

for i, column in enumerate(df.columns):
    contagens = df[column].value_counts().reset_index()
    contagens.columns = ["Categoria", "Contagem"]

    # Selecione os top_n maiores valores
    top_contagens = contagens.head(top_n)

    # Calcule a soma dos "Outros"
    outros_contagem = contagens[top_n:].sum()
    outros_contagens = pd.DataFrame({"Categoria": ["Outros"], "Contagem": [outros_contagem["Contagem"]]})

    # Concatene os top_n e "Outros"
    final_contagens = pd.concat([top_contagens, outros_contagens])

    # Crie um gráfico de barras horizontais usando o Seaborn
    sns.barplot(x="Contagem", y="Categoria", data=final_contagens, ax=axes[i // 4, i % 4], orient="h")

    # Adicione rótulos aos eixos e ao gráfico
    axes[i // 4, i % 4].set_xlabel("Contagem")
    axes[i // 4, i % 4].set_ylabel("Categoria")
    axes[i // 4, i % 4].set_title(f" {column}")

# Ajuste o espaçamento entre os subplots
plt.tight_layout()

# Exiba os gráficos
plt.show()


tabela_contingencia = pd.crosstab(df['TIPO_BOLSA'], df['NOME_CURSO_BOLSA'])

# Você também pode adicionar margens para obter totais de linha e coluna
tabela_contingencia_com_margens = pd.crosstab(df['TIPO_BOLSA'], df['NOME_CURSO_BOLSA'], margins=True, margins_name="Total")

# Exibir as tabelas de contingência
print("Tabela de Contingência:")
print(tabela_contingencia)
print("\nTabela de Contingência com Margens:")
print(tabela_contingencia_com_margens)

import pandas as pd
from scipy.stats import chi2_contingency

# Assuming df is your DataFrame
nomes_colunas = df.columns
pd.set_option('display.max_columns', 25)

# Correctly defining categorical_cols as a list of column names
categorical_cols = list(nomes_colunas)

# Calculating the chi-square test and storing the results
results = []
for i in range(len(categorical_cols)):
    for j in range(i+1, len(categorical_cols)):
        contingency_table = pd.crosstab(df[categorical_cols[i]], df[categorical_cols[j]])
        _, p_value, _, _ = chi2_contingency(contingency_table)
        results.append((categorical_cols[i], categorical_cols[j], p_value))

# Creating the DataFrame of results
results_df = pd.DataFrame(results, columns=['Variable_1', 'Variable_2', 'P_Value'])
print(results_df)

#1 Qual região do Brasil que mais ofertou bolsas de estudo no ano de 2017?(gráfico)
regiao_brasil = df['REGIAO_BENEFICIARIO_BOLSA'].value_counts()

# Criar um DataFrame apenas com os top 10 cursos
df_top_10 = df[df['REGIAO_BENEFICIARIO_BOLSA'].isin(regiao_brasil.index)]

# Criar gráfico de barras empilhadas
plt.figure(figsize=(12, 6))
sns.countplot(x='REGIAO_BENEFICIARIO_BOLSA', hue='TIPO_BOLSA', data=df_top_10, palette='viridis')
plt.xlabel('Regiões')
plt.ylabel('Número de Bolsas')
plt.title('Número de bolsas ofertadas por Região')
plt.xticks(rotation=45, ha='right')  # Ajusta a inclinação dos rótulos para melhor leitura
plt.legend(title='Tipo de Bolsa', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

#2 Qual a Raça/cor que disponibilizou mais bolsas integrais/parciais?
raca_cor = df['RACA_BENEFICIARIO_BOLSA'].value_counts()

# Criar um DataFrame apenas com os top 10 cursos
df_top_10 = df[df['RACA_BENEFICIARIO_BOLSA'].isin(raca_cor.index)]

# Criar gráfico de barras empilhadas
plt.figure(figsize=(12, 6))
sns.countplot(x='RACA_BENEFICIARIO_BOLSA', hue='TIPO_BOLSA', data=df_top_10, palette='Set2')
plt.xlabel('Raça/cor')
plt.ylabel('Número de Bolsas')
plt.title('Número de bolsas ofertadas por Raça/cor')
plt.xticks(rotation=45, ha='right')  # Ajusta a inclinação dos rótulos para melhor leitura
plt.legend(title='Tipo de Bolsa', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

#3 Qual curso ofertou mais bolsas integrais, e parciais?
import matplotlib.pyplot as plt
import seaborn as sns

# Supondo que você tenha uma coluna 'NOME_CURSO_BOLSA' e 'TIPO_BOLSA' no DataFrame df
top_10_cursos = df['NOME_CURSO_BOLSA'].value_counts().head(10)

# Criar um DataFrame apenas com os top 10 cursos
df_top_10 = df[df['NOME_CURSO_BOLSA'].isin(top_10_cursos.index)]

# Criar gráfico de barras empilhadas
plt.figure(figsize=(12, 6))
sns.countplot(x='NOME_CURSO_BOLSA', hue='TIPO_BOLSA', data=df_top_10, palette='Purples')
plt.xlabel('Curso')
plt.ylabel('Número de Bolsas')
plt.title('Top 10 Cursos com mais bolsas ofertadas por tipo da bolsa')
plt.xticks(rotation=45, ha='right')  # Ajusta a inclinação dos rótulos para melhor leitura
plt.legend(title='Tipo de Bolsa', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
