"""Cover image for the AF post: two fates of pi(t), one inequality apart.

Interior regime under free entry (A5): pi(t) = 1 - (La0/Lbar) * exp(gamma * t),
zero after t* = ln(Lbar/La0) / gamma. Same object as figure F1, stylized.
Regenerate with: python cover.py  (writes cover.png, 1200x630)
"""

import numpy as np
import matplotlib.pyplot as plt

# palette: validated categorical pair on light surface (CVD dE 74.6)
SURFACE = "#fcfcfb"
BLUE = "#2a78d6"
RED = "#e34948"
INK2 = "#52514e"
MUTED = "#898781"
BASELINE = "#c3c2b7"

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
})

RATIO = 0.06                          # La(0) / Lbar
T_STAR = 16.0
G_POS = np.log(1 / RATIO) / T_STAR    # ~0.176
G_NEG = -0.06
T_END = T_STAR + 4.5


def pi(t, gamma):
    return np.clip(1 - RATIO * np.exp(gamma * t), 0, 1)


fig, ax = plt.subplots(figsize=(12, 6.3), dpi=100)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(BASELINE)
ax.spines["bottom"].set_linewidth(1.2)
ax.set_yticks([])
ax.set_xticks([])
ax.set_ylim(-0.04, 1.12)
ax.set_xlim(-0.5, T_END + 6.4)        # room for end labels

t_neg = np.linspace(0, T_END - 0.4, 600)
ax.plot(t_neg, pi(t_neg, G_NEG), color=BLUE, lw=4.2, zorder=3,
        solid_capstyle="round")

t_pos = np.linspace(0, T_STAR, 600)
ax.plot(t_pos, pi(t_pos, G_POS), color=RED, lw=4.2, zorder=3,
        solid_capstyle="round")
ax.plot([T_STAR, T_END - 0.4], [0, 0], color=RED, lw=4.2, zorder=3,
        solid_capstyle="round")

ax.axvline(T_STAR, color=MUTED, lw=1.0, ls=(0, (4, 4)), zorder=2)
ax.text(T_STAR, -0.10, r"$t^{*}$", color=INK2, fontsize=17,
        ha="center", va="top", clip_on=False)

# direct labels at line ends (identity never color-alone)
ax.text(T_END + 0.35, pi(T_END - 0.4, G_NEG),
        "$\\gamma < 0$\nhumans persist",
        color=BLUE, fontsize=16, va="center", fontweight="bold",
        linespacing=1.35)
ax.text(T_END + 0.35, 0.06, "$\\gamma > 0$\nexcluded",
        color=RED, fontsize=16, va="center", fontweight="bold",
        linespacing=1.35)

ax.text(-0.5, 1.145,
        r"$\pi$  (human share of the economic loop)"
        "      same economy, one inequality apart",
        color=MUTED, fontsize=12.5, va="bottom")
ax.text(T_END + 6.4, -0.10, "time", color=MUTED, fontsize=12.5,
        ha="right", va="top", clip_on=False)

fig.subplots_adjust(left=0.045, right=0.985, top=0.90, bottom=0.10)
fig.savefig("cover.png", dpi=100, facecolor=SURFACE)
print("cover.png written, t* =", T_STAR, "gamma+ =", round(G_POS, 3))
