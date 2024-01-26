import matplotlib.pyplot as plt

# Data
weight = [15, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]

fsr400 = [0, 231, 308, 400, 477, 508, 544, 563, 580, 588, 603, 613, 622, 630, 631, 634, 637, 644]
rp_c76_lt = [0, 0, 62, 319, 436, 519, 554, 602, 621, 647, 653, 670, 677, 686, 690, 703, 715, 732]
rp_c183_st = [15, 59, 383, 543, 637, 691, 738, 777, 792, 817, 830, 841, 845, 846, 850, 855, 858, 862]

# Adding a grid
plt.grid(True, linestyle='--', alpha=0.7)

# Adding more values on the y-axis
plt.yticks(range(0, max(rp_c183_st) + 50, 50))
# Adding values every 100 on the x-axis
plt.xticks(range(0, max(weight) + 1, 100))

# Plotting the curves
plt.plot(weight, fsr400, marker='o', markersize=8, label='FSR400')
plt.plot(weight, rp_c76_lt, marker='o', markersize=8, label='RP-C7.6-LT')
plt.plot(weight, rp_c183_st, marker='o', markersize=8, label='RP-C18.3-ST')

# Adding labels
plt.title('Sensors Work Range')
plt.xlabel('Force [g]')
plt.ylabel('Value [bit]')
# Enlarging the legend
plt.legend(fontsize='large')

# Displaying the plot
plt.show()
