import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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
