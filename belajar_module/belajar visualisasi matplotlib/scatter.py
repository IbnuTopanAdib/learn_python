from matplotlib import pyplot as plt
import numpy as np
def linear(el):
    return (2 * el) + 3
def kuadrat(el):
    return el**2


ro = list(range(1, 12))
x = list(map(linear, ro))
y = list(map(kuadrat, x))
x = np.array(x)
y = np.array(y)
colors = (y + 5)/ (x)
size = colors**2
print(size)
plt.style.use('ggplot')
plt.scatter(x, y, s = size, c = colors, marker = 'X', cmap= 'Blues',
            edgecolors = 'black', linewidths=1, alpha= 0.85)

cbar = plt.colorbar()
cbar.set_label('Kekuatan')

plt.show()
plt.savefig("assets/scatter1.png")


