import matplotlib.pyplot as plt

# Data for the first dataset
name1 = 'RP-C7.6-LT'
force1 = [114, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
silicone1 = [None, None, None, None, None, None, 700, 905, 1140, 1253, 1310, 1395, 1473, 1542, 1627]
flat_overlay1 = [None, 463, 643, 1052, 1138, 1459, 1573, 1642, 1675, 1795, 1963, 2023, 2102, 2232, 2257]
convex_overlay1 = [320, 631, 1003, 1423, 1601, 1711, 1842, 1903, 1972, 1996, 2105, 2146, 2189, 2210, 2225]

# Data for the second dataset
name2 = 'RP-C18.3-ST'
force2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
silicone2 = [730, 900, 1020, 1040, 1340, 1400, 1550, 1610, 1720, 1820, 1920, 1980, 2015, 1999, 2010]
flat_overlay2 = [None, 480, 590, 730, 840, 860, 900, 960, 1100, 1280, 1400, 1515, 1560, 1610, 1630]
convex_overlay2 = [840, 1290, 1620, 1790, 1850, 1980, 2080, 2160, 2230, 2300, 2330, 2390, 2430, 2450, 2500]

# Function to plot the data
def plot_data(name, force, silicone, flat_overlay, convex_overlay):
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.yticks(range(0, max(convex_overlay) + 50, 100))
    plt.xticks(range(0, max(force) + 1, 100))
    plt.plot(force, silicone, marker='o', markersize=8, label='silicone without overlay')
    plt.plot(force, flat_overlay, marker='o', markersize=8, label='flat overlay')
    plt.plot(force, convex_overlay, marker='o', markersize=8, label='convex overlay')
    plt.title(f'{name} work range silicone and with overlays')
    plt.xlabel('Force [g]')
    plt.ylabel('Value [bit]')
    plt.legend(fontsize='large')
    plt.show()

# Plotting two separate graphs
plot_data(name1, force1, silicone1, flat_overlay1, convex_overlay1)
plot_data(name2, force2, silicone2, flat_overlay2, convex_overlay2)

