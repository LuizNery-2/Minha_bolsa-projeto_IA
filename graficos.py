import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt


class visualizacao_dados:

    def __init__(self, data):

        self.data = data;

    def count_plot_target(self, save_path="static/target_plot.png"):
        sns.countplot(x='TIPO_BOLSA', data=self.data)
        plt.savefig(save_path)
        plt.close()

    def count_plot_df(self, save_path="static/df_plot.png"):
        df = self.data
        top_n = 10
        fig, axes = plt.subplots(3, 4, figsize=(20, 10))
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
        plt.savefig(save_path)
        plt.close()