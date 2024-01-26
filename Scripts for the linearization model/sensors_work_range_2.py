import matplotlib.pyplot as plt
# Dane
#RP-C7.6-LT
# force = [114, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
# silicone = [None, None, None, None, None, None, 700, 905, 1140, 1253, 1310, 1395, 1473, 1542, 1627]
# flat_overlay = [None, 463, 643, 1052, 1138, 1459, 1573, 1642, 1675, 1795, 1963, 2023, 2102, 2232, 2257]
# convex_overlay = [320, 631, 1003, 1423, 1601, 1711, 1842, 1903, 1972, 1996, 2105, 2146, 2189, 2210, 2225]

#RP-C18.3-ST
# force = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
# silicone = [730, 900, 1020, 1040, 1340, 1400, 1550, 1610, 1720, 1820, 1920, 1980, 2015, 1999, 2010]
# flat_overlay = [None, 480, 590, 730, 840, 860, 900, 960, 1100, 1280, 1400, 1515, 1560, 1610, 1630]
# convex_overlay = [840, 1290, 1620, 1790, 1850, 1980, 2080, 2160, 2230, 2300, 2330, 2390, 2430, 2450, 2500]



# Data
grams_small_31 = [30, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_small_31 = [300, 530, 890, 1110, 1350, 1450, 1510, 1620, 1650, 1700, 1760, 1830, 1910, 1950, 1990, 2020]

grams_small_21 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_small_21 = [220, 460, 900, 1070, 1170, 1250, 1290, 1320, 1400, 1535, 1600, 1645, 1640, 1720, 1790]

grams_big_11 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_big_11 = [210, 431, 559, 851, 1119, 1339, 1453, 1589, 1685, 1829, 1917, 1957, 2007, 2037, 2100]

grams_big_17 = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_big_17 = [351, 789, 1035, 1135, 1233, 1305, 1357, 1547, 1733, 1811, 1956, 2085, 2137, 2189]

# Adding a grid
plt.grid(True, linestyle='--', alpha=0.7)

# Adding more values on the y-axis
plt.yticks(range(0, max(ADC_big_17) + 50, 100))
# Adding values every 100 on the x-axis
plt.xticks(range(0, max(grams_small_31) + 1, 100))

# Plotting the curves
plt.plot(grams_small_31, ADC_small_31, marker='o', markersize=8, label='Middle Finger ID 31')
plt.plot(grams_small_21, ADC_small_21, marker='o', markersize=8, label='Index Finger ID 21')
plt.plot(grams_big_11, ADC_big_11, marker='o', markersize=8, label='Thumb ID 11')
plt.plot(grams_big_17, ADC_big_17, marker='o', markersize=8, label='Palm ID 17')

# Adding labels
plt.title('Sensors Test in the Final Version of the Glove')
plt.xlabel('Force [g]')
plt.ylabel('Value [bit]')
# Enlarging the legend
plt.legend(fontsize='large')

# Displaying the plot
plt.show()
