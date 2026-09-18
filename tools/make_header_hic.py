import cooler, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize
c = cooler.Cooler('/mnt/processed/wolffjoa/restart_of_prediction_project/originalData/GSE63525_GM12878_insitu_primary+replicate_combined_30_10kb.cool')
chrom = '2' if '2' in c.chromnames else 'chr2'
M = c.matrix(balance=False).fetch(f'{chrom}:56000000-66000000').astype(float)
n = M.shape[0]; depth = 130
L = np.log1p(M)
i, j = np.meshgrid(np.arange(n + 1), np.arange(n + 1), indexing='ij')
X = (i + j) / 2.0; Y = (j - i) / 2.0
L = np.where(np.triu(np.ones_like(L)) > 0, L, np.nan)
lo, hi = np.nanpercentile(L[L > 0], [20, 99.7])
# classic Hi-C palette (RdYlBu_r); weak contacts become transparent so the plot fades into the page
base = plt.get_cmap('RdYlBu_r')(np.linspace(0, 1, 256))
t = np.linspace(0, 1, 256)
base[:, 3] = np.clip((t - 0.08) / 0.42, 0, 1) ** 1.2
cmap = ListedColormap(base); cmap.set_bad((0, 0, 0, 0))
fig = plt.figure(figsize=(24, 24 * depth / 2 / n), dpi=100)
fig.patch.set_alpha(0)
ax = fig.add_axes([0, 0, 1, 1]); ax.patch.set_alpha(0)
ax.pcolormesh(X, Y, L, cmap=cmap, norm=Normalize(lo, hi), rasterized=True)
ax.set_xlim(depth / 2, n - depth / 2); ax.set_ylim(0, depth / 2); ax.axis('off')
fig.savefig('assets/img/header-hic.png', transparent=True)
