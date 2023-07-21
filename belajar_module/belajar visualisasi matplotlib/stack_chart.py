import matplotlib.pyplot as plt

# top striker kuntul fc
john = [2, 1, 0, 2, 2, 0, 1, 0, 2, 0]
ibnu = [0, 3, 0, 1, 0, 0, 1, 0, 2, 0]
trondol = [0, 0, 0, 1, 0, 0, 1, 1, 5, 2]
match = list(range( 1, 11))

# top karyawan
jane = [2, 4, 2, 3, 0, 3, 3]
lisa = [3, 2, 5, 2, 8, 3, 2]
jenny = [3, 2, 1, 3, 0, 2, 3]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

labels_striker = ['john', 'ibnu', 'trondol']
labels_karyawan = ['jane', 'lisa', 'jenny']
colors = ['#1f77b4', '#2ca02c', '#d62728']

def plot_strikers():
    plt.stackplot(match, john, ibnu, trondol, labels=labels_striker, colors=colors)
    plt.title("Top Score Kuntul FC Last 10 Match")
    plt.legend(loc='upper left')
    plt.savefig("assets/top_strikers.png")
    plt.show()

plot_strikers()

def plot_contribution():
    plt.stackplot(days, jane, lisa, jenny, labels= labels_karyawan)
    plt.title('Top Karyawan')
    plt.legend(loc = 'upper left')
    plt.savefig("assets/top_karyawan.png")
    plt.show()

plot_contribution()