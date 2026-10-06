from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
n = np.ones(3) / np.sqrt(3)
cross = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
def P(r):
    a = 2*np.pi*r/3
    return np.cos(a)*np.eye(3) + (1-np.cos(a))*np.outer(n, n) - np.sin(a)*cross

expected = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
assert np.allclose(P(0), np.eye(3))
assert np.allclose(P(1), expected)
for r in np.linspace(0, 1, 301):
    assert np.allclose(P(r).T @ P(r), np.eye(3))
    assert np.allclose(np.linalg.det(P(r)), 1)
    assert np.allclose(P(r) @ n, n)

fig = plt.figure(figsize=(8.8, 5.8))
ax = fig.add_subplot(111, projection='3d')
colors = ['#155fa0', '#b34529', '#268154']
r = np.linspace(0, 1, 241)
for j, col in enumerate(colors):
    e = np.eye(3)[:, j]
    curve = np.array([P(v) @ e for v in r])
    ax.plot(*curve.T, color=col, lw=2.7, label=rf'$e_{j}\mapsto e_{(j-1)%3}$')
    ax.scatter(*curve[0], c=col, s=40)
    ax.scatter(*curve[-1], c=col, s=80, marker='>')
    ax.quiver(0, 0, 0, *e, color='#7b8490', alpha=.65, arrow_length_ratio=.06)
    label_point = 1.10*e
    if j == 0:
        label_point += np.array([.08, -.07, -.10])
    ax.text(*label_point, rf'$e_{j}$', fontsize=12)
diag = np.array([-1.15*n, 1.35*n])
ax.plot(*diag.T, ls='--', color='#5a4e80', lw=1.4)
ax.text(*(1.37*n), r'$n=(1,1,1)/\sqrt{3}$', fontsize=11, color='#5a4e80')
ax.set(xlim=(-.75, 1.15), ylim=(-.75, 1.15), zlim=(-.75, 1.15),
       xlabel=r'$x_0$', ylabel=r'$x_1$', zlabel=r'$x_2$')
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=24, azim=34)
ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_zticks([0, 1])
ax.legend(loc='upper left', bbox_to_anchor=(-.13, .97), frameon=False)
fig.suptitle('The three-coordinate cycle preserves orientation', fontsize=15)
fig.text(.5, .035, r'$P_r:$ rotation about $n$ through $-2\pi r/3$; '
         r'$P_1(x_0,x_1,x_2)=(x_1,x_2,x_0)$; $\det P_r=+1$',
         ha='center', fontsize=11)
fig.tight_layout(rect=[0, .08, 1, .95])
for ext in ['svg', 'png']:
    fig.savefig(out / f'KT-KK-21-suspension-rotation.{ext}', dpi=170,
                bbox_inches='tight', metadata={'Creator': 'Original mathematical figure; CC0'})
print('Rendered exact-formula sampled rotation diagram; endpoint and orthogonality checks passed')
