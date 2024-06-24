import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
labels = ['Single Core', 'Multi Core']
os_scores = [710, 1538]
container_scores = [551, 1198]
overheads = [0.223943661971831, 0.2210663198959688]

x = np.arange(len(labels))  # O índice das etiquetas
width = 0.25  # A largura das barras

fig, ax1 = plt.subplots()

# Gráfico de barras para os scores
bars1 = ax1.bar(x - width, os_scores, width, label='Sistema Operativo')
bars2 = ax1.bar(x, container_scores, width, label='Contentor')

# Configurações do eixo Y para os scores
ax1.set_ylabel('Scores')
ax1.set_title('Resultados do Geekbench e Overheads')
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.legend(loc='upper left')

# Função para adicionar os valores das barras
def autolabel(bars, ax):
    """Anexa um rótulo com o valor em cada barra."""
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 pontos de deslocamento vertical
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(bars1, ax1)
autolabel(bars2, ax1)

# Eixo Y secundário para os overheads
ax2 = ax1.twinx()
bars3 = ax2.bar(x + width, overheads, width, label='Overhead', color='gray')

# Configurações do eixo Y para os overheads
ax2.set_ylabel('Overhead')
ax2.legend(loc='upper right')

def autolabel_overhead(bars, ax):
    """Anexa um rótulo com o valor em cada barra."""
    for bar in bars:
        height = bar.get_height()
        ax.annotate('{:.2f}'.format(height),
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 pontos de deslocamento vertical
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel_overhead(bars3, ax2)

fig.tight_layout()

plt.show()