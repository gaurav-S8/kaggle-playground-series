# Import Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Iterable, Tuple, Optional, Dict

def plot_bar_counts(
    series_list: List[Iterable],
    labels: List[str],
    x_label: str,
    y_label: str,
    title: str,
    colors: List[str] = None,
    alpha: float = 0.4,
    fig_size: Tuple[int, int] = (10, 6)
) -> None:
    if colors is None:
        colors = ['blue', 'orange', 'green', 'red', 'purple'][:len(series_list)]

    # Combine categories across all series
    all_categories = set()
    for series in series_list:
        all_categories.update(series.unique())
    categories = sorted(all_categories)

    # Compute counts for each series
    counts = []
    for series in series_list:
        counts.append(series.value_counts().reindex(categories, fill_value = 0))

    # Sort categories by ascending count of first series
    order = counts[0].sort_values().index
    categories = order.tolist()
    counts = [c.loc[order] for c in counts]

    n = len(series_list)
    x = np.arange(len(categories))
    width = 0.8 / n

    plt.figure(figsize = fig_size)
    for i, (count, label, color) in enumerate(zip(counts, labels, colors)):
        offset = (i - n / 2 + 0.5) * width
        bars = plt.bar(x + offset, count, width, label = label, color = color, alpha = alpha)
        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{int(height)}",
                ha = 'center',
                va = 'bottom'
            )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(x, categories)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_bar_percentages(
    series_list: List[Iterable],
    labels: List[str],
    x_label: str,
    y_label: str,
    title: str,
    colors: List[str] = None,
    alpha: float = 0.4,
    fig_size: Tuple[int, int] = (10, 6)
) -> None:
    if colors is None:
        colors = ['blue', 'orange', 'green', 'red', 'purple'][:len(series_list)]

    # Combine categories across all series
    all_categories = set()
    for series in series_list:
        all_categories.update(series.unique())
    categories = sorted(all_categories)

    # Compute percentages for each series
    percs = []
    for series in series_list:
        counts = series.value_counts().reindex(categories, fill_value = 0)
        percs.append(100 * counts / len(series))

    # Sort categories by ascending percentage of first series
    order = percs[0].sort_values().index
    categories = order.tolist()
    percs = [p.loc[order] for p in percs]

    n = len(series_list)
    x = np.arange(len(categories))
    width = 0.8 / n

    plt.figure(figsize = fig_size)
    for i, (perc, label, color) in enumerate(zip(percs, labels, colors)):
        offset = (i - n / 2 + 0.5) * width
        bars = plt.bar(x + offset, perc, width, label = label, color = color, alpha = alpha)
        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{height:.2f}%",
                ha = 'center',
                va = 'bottom'
            )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(x, categories)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_hist_counts(
    series1: Iterable,
    series2: Iterable,
    label1: str,
    label2: str,
    num_bins: int,
    x_label: str,
    y_label: str,
    title: str,
    colors: Tuple[str, str] = ('blue', 'orange'),
    alpha: float = 0.4,
    fig_size: Tuple[int, int] = (10, 6)
) -> None:
    bins = np.linspace(
        min(series1.min(), series2.min()),
        max(series1.max(), series2.max()),
        num_bins + 1
    )
    plt.figure(figsize = fig_size)
    color1, color2 = colors
    bin_centers = (bins[:-1] + bins[1:]) / 2
    counts1, _ = np.histogram(series1, bins = bins)
    counts2, _ = np.histogram(series2, bins = bins)

    plt.hist(series1, bins = bins, color = color1, alpha = alpha, edgecolor = 'black', linewidth = 1, label = label1)
    plt.hist(series2, bins = bins, color = color2, histtype = 'step', linewidth = 2, label = label2)

    plt.plot(bin_centers, counts1, color = color1, linestyle = '--', linewidth = 1.5)
    plt.plot(bin_centers, counts2, color = color2, linestyle = '--', linewidth = 1.5)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(bins, rotation = 45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_hist_percentages(
    series1: Iterable,
    series2: Iterable,
    label1: str,
    label2: str,
    num_bins: int,
    x_label: str,
    y_label: str,
    title: str,
    colors: Tuple[str, str] = ('blue', 'orange'),
    alpha: float = 0.4,
    fig_size: Tuple[int, int] = (10, 6)
) -> None:
    bins = np.linspace(
        min(series1.min(), series2.min()),
        max(series1.max(), series2.max()),
        num_bins + 1
    )
    color1, color2 = colors
    bin_centers = (bins[:-1] + bins[1:]) / 2

    counts1, _ = np.histogram(series1, bins = bins)
    counts2, _ = np.histogram(series2, bins = bins)

    pct1 = 100 * counts1 / len(series1)
    pct2 = 100 * counts2 / len(series2)

    plt.figure(figsize = fig_size)
    weights1 = np.ones(len(series1)) * 100 / len(series1)
    weights2 = np.ones(len(series2)) * 100 / len(series2)
    plt.hist(series1, bins = bins, weights = weights1, color = color1, alpha = alpha, edgecolor = 'black', linewidth = 1, label = label1)
    plt.hist(series2, bins = bins, weights = weights2, color = color2, histtype = 'step', linewidth = 2, label = label2)

    plt.plot(bin_centers, pct1, color = color1, linestyle = '--', linewidth = 1.5)
    plt.plot(bin_centers, pct2, color = color2, linestyle = '--', linewidth = 1.5)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(bins, rotation = 45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_stacked_bar_by_target(
    feature: Iterable,
    target: Iterable,
    x_label: str,
    y_label: str,
    title: str,
    colors: List[str] = None,
    alpha: float = 0.8,
    rotation: int = 0,
    fig_size: Tuple[int, int] = (10, 6)
) -> None:
    cross_tab = pd.crosstab(feature, target, normalize = 'index') * 100
    ax = cross_tab.plot(
        kind = 'bar',
        stacked = True,
        edgecolor = 'black',
        figsize = fig_size,
        color = colors,
        alpha = alpha
    )
    # Add percentage labels
    for bars in ax.containers:
        for bar in bars:
            height = bar.get_height()
            if height > 2:
                ax.text(
                    bar.get_x() + bar.get_width() / 2,
                    bar.get_y() + height / 2,
                    f"{height:.1f}%",
                    ha = 'center',
                    va = 'center',
                    fontsize = 9
                )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation = rotation)
    plt.tight_layout()
    plt.show()

def plot_box_by_target(
    feature: Iterable,
    target: Iterable,
    x_label: str,
    y_label: str,
    title: str,
    colors: List[str] = None,
    alpha: float = 0.6,
    fig_size: Tuple[int, int] = (10, 6)
) -> None:
    classes = sorted(target.unique())
    data = [feature[target == cls] for cls in classes]

    if colors is None:
        colors = ['blue', 'orange', 'green', 'red'][:len(classes)]

    plt.figure(figsize = fig_size)
    bp = plt.boxplot(
        data,
        labels = classes,
        patch_artist = True,
        medianprops = dict(color = 'black'),
        whiskerprops = dict(color = 'black'),
        capprops = dict(color = 'black'),
        flierprops = dict(markeredgecolor = 'black')
    )
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(alpha)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_grouped_bar_by_target(
    feature: Iterable,
    target: Iterable, 
    x_label: str,
    y_label: str,
    title: str,
    fig_size: Tuple[int, int] = (10, 6)
) -> None:
    cross_tab = (pd.crosstab(feature, target)/len(target)) * 100
    plt.figure(figsize = fig_size)
    cross_tab.plot(
        kind = 'bar',
        width = 0.8,
        edgecolor = 'black'
    )
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(title = 'Heart Disease Class')
    plt.xticks(rotation = 0)
    plt.tight_layout()
    plt.show()

def plot_2d_scatter_by_class(
    x: pd.Series,
    y: pd.Series,
    target: pd.Series,
    title: Optional[str] = None,
    figsize: tuple = (10, 6),
    alpha: float = 0.3,
    s: int = 1,
    colors: Optional[dict] = None,
    labels: Optional[dict] = None
) -> None:
    unique_classes = sorted(target.unique())
    
    default_colors = {cls: color for cls, color in zip(unique_classes, ['blue', 'orange', 'red'])}
    default_labels = {cls: str(cls) for cls in unique_classes}
    
    colors = colors or default_colors
    labels = labels or default_labels

    plt.figure(figsize = figsize)
    for cls in unique_classes:
        mask = (target == cls).values
        plt.scatter(
            x[mask],
            y[mask],
            c = colors[cls],
            label = labels[cls],
            alpha = alpha,
            s = s
        )
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    plt.title(title or f'{x.name} vs {y.name}')
    plt.legend()
    plt.show()