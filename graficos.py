import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt


class visualizacao_dados:

    def __init__(self, data):

        self.data = data;
    def plot_top_n(df, top_n=10):
        fig, axes = plt.subplots(3, 4, figsize=(45, 30))
        for i, column in enumerate(df.columns):
            contagens = df[column].value_counts().reset_index()
            contagens.columns = ["Categoria", "Contagem"]
            top_contagens = contagens.head(top_n)
            outros_contagem = contagens[top_n:].sum()
            outros_contagens = pd.DataFrame({"Categoria": ["Outros"], "Contagem": [outros_contagem["Contagem"]]})
            final_contagens = pd.concat([top_contagens, outros_contagens])
            sns.barplot(x="Contagem", y="Categoria", data=final_contagens, ax=axes[i // 4, i % 4], orient="h")
            axes[i // 4, i % 4].set_xlabel("Contagem")
            axes[i // 4, i % 4].set_ylabel("Categoria")
            axes[i // 4, i % 4].set_title(f" {column}")
        plt.tight_layout()
        plt.show()

    def plot_bolsa_type(df):
        sns.countplot(x='TIPO_BOLSA', data=df)
        plt.show()

    def plot_bolsas_por_regiao(df):
        regiao_brasil = df['REGIAO_BENEFICIARIO_BOLSA'].value_counts()
        df_top_10 = df[df['REGIAO_BENEFICIARIO_BOLSA'].isin(regiao_brasil.index)]
        plt.figure(figsize=(12, 6))
        sns.countplot(x='REGIAO_BENEFICIARIO_BOLSA', hue='TIPO_BOLSA', data=df_top_10, palette='viridis')
        plt.xlabel('Regiões')
        plt.ylabel('Número de Bolsas')
        plt.title('Número de bolsas ofertadas por Região')
        plt.xticks(rotation=45, ha='right') 
        plt.legend(title='Tipo de Bolsa', bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.show()

    def plot_frequencia_colunas_categoricas(df):
        colunas_categoricas = df.select_dtypes(include=['object'])
        for coluna in colunas_categoricas.columns:
            frequencia = df[coluna].value_counts()
            plt.figure(figsize=(10, 5))
            sns.barplot(x=frequencia.index, y=frequencia.values, alpha=0.8)
            plt.title(f'Frequência para a coluna {coluna}')
            plt.ylabel('Número de Ocorrências', fontsize=12)
            plt.xlabel(coluna, fontsize=12)
            plt.show()

    def print_tabela_contingencia(df):
        tabela_contingencia = pd.crosstab(df['TIPO_BOLSA'], df['NOME_CURSO_BOLSA'])
        tabela_contingencia_com_margens = pd.crosstab(df['TIPO_BOLSA'], df['NOME_CURSO_BOLSA'], margins=True, margins_name="Total")
        print("Tabela de Contingência:")
        print(tabela_contingencia)
        print("\nTabela de Contingência com Margens:")
        print(tabela_contingencia_com_margens)

    def print_chi_square_results(df):
        nomes_colunas = df.columns
        categorical_cols = list(nomes_colunas)
        results = []
        for i in range(len(categorical_cols)):
            for j in range(i+1, len(categorical_cols)):
                contingency_table = pd.crosstab(df[categorical_cols[i]], df[categorical_cols[j]])
                _, p_value, _, _ = chi2_contingency(contingency_table)
                results.append((categorical_cols[i], categorical_cols[j], p_value))
        results_df = pd.DataFrame(results, columns=['Variable_1', 'Variable_2', 'P_Value'])
        print(results_df)
