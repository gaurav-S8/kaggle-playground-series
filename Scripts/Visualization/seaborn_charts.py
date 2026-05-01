# Import Libraries
import pandas as pd
import seaborn as sns
from typing import Optional
import matplotlib.pyplot as plt

def plot_correlation_heatmap(
    df: pd.DataFrame,
    columns: list[str],
    title: str = 'Correlation Heatmap',
    fig_size: tuple[int, int] = (10, 5)
) -> None:
    corr_matrix = df[columns].corr()
    plt.figure(figsize = fig_size)
    sns.heatmap(
        corr_matrix,
        annot = True,
        fmt = '.2f',
        cmap = 'coolwarm',
        vmin = -1,
        vmax = 1,
        square = True,
        linewidths = 0.5
    )
    plt.title(title)
    plt.tight_layout()
    plt.show()