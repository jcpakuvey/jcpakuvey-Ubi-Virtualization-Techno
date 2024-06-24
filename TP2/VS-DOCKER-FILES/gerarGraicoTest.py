import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
labels = ['Single Core', 'Multi Core']
os_scores = [710, 1538]
container_scores = [551, 1198]

x = np.arange(len(labels))  # O índice das etiquetas
width = 0.35  # A largura das barras

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, os_scores, width, label='Sistema Operativo')
bars2 = ax.bar(x + width/2, container_scores, width, label='Contentor')

# Adicionar alguns textos
ax.set_ylabel('Scores')
ax.set_title('Resultados do Geekbench: Sistema Operativo vs Contentor')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Função para adicionar os valores das barras
def autolabel(bars):
    """Anexa um rótulo com o valor em cada barra."""
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 pontos de deslocamento vertical
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(bars1)
autolabel(bars2)

fig.tight_layout()

plt.show()