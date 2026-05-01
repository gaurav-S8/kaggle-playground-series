import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
 
competitions = [
    {"label": "S6E2\nHeart Disease", "rank": 2073, "total": 4370},
    {"label": "S6E3\nCustomer Churn", "rank": 1160, "total": 4142},
    {"label": "S6E4\nIrrigation Need", "rank": 1330, "total": 4315},
]
 
labels = [c["label"] for c in competitions]
percentiles = [round((1 - c["rank"] / c["total"]) * 100, 1) for c in competitions]
ranks = [c["rank"] for c in competitions]
totals = [c["total"] for c in competitions]
 
fig, ax = plt.subplots(figsize = (10, 6))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')
 
x = np.arange(len(labels))
 
ax.plot(
    x, percentiles, color = '#8957e5', linewidth = 2.5, zorder = 3, marker = 'o', 
    markersize = 10, markerfacecolor = 'white', markeredgecolor = '#8957e5', markeredgewidth = 2
)
ax.fill_between(x, percentiles, alpha = 0.15, color = '#8957e5', zorder = 2)
 
# Annotate points
for i, (rank, total, pct) in enumerate(zip(ranks, totals, percentiles)):
    ax.text(
        i,
        pct + 2,
        f'Rank {rank}/{total}\nTop {100 - pct:.1f}%',
        ha = 'center', va = 'bottom',
        color = 'white', fontsize = 10, fontweight = 'bold'
    )
 
ax.set_xticks(x)
ax.set_xticklabels(labels, color = 'white', fontsize = 11)
ax.set_ylabel('Percentile (Higher = Better)', color='white', fontsize = 11)
ax.set_title('Kaggle Playground Series — Rank Progression', color = 'white', fontsize = 14, fontweight = 'bold', pad = 20)
ax.set_ylim(0, 100)
ax.yaxis.set_tick_params(labelcolor = 'white')
ax.grid(axis = 'y', color = '#30363d', linestyle = '--', zorder = 0)
ax.spines[:].set_color('#30363d')
 
plt.tight_layout()
plt.savefig('../Assets/rank_progression.png', dpi = 150, bbox_inches = 'tight', facecolor = '#0d1117')
plt.show()
print("Chart saved as rank_progression.png")