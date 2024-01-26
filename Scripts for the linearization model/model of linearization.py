import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def generate_plot(ADC, grams, volt_in, resistor, max_bits):
    # Generating data
    voltage_aoc = np.array(ADC) * (volt_in / max_bits)
    sensor = (volt_in * resistor) / voltage_aoc - resistor
    conductance = 1000000 / sensor
    newton = np.round(np.array(grams) * 0.00980665, 1)

    def power_law(x, c, d):
        return c * np.power(x, d)

    # Fitting a power-law model to the data
    params, covariance = curve_fit(power_law, conductance, grams)

    # Extracting parameters
    c, d = params
    print("Value of parameter c:", c)
    print("Value of parameter d:", d)

    # Creating a plot
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.plot(conductance, grams, 'o', label='Data')
    plt.plot(conductance, power_law(np.array(conductance), c, d), label='Power-law linearization')
    plt.title('Linearization of the RP-C18.3-ST sensor')
    plt.xlabel('Conductance [μS]')
    plt.ylabel('Force [g]')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Calculating data predicted by the model
    predicted_force = power_law(np.array(conductance), c, d)

    # Calculating percentage error
    error_percentage = np.abs((grams - predicted_force) / grams) * 100

    # Calculating mean error
    mean_error = np.mean(error_percentage)
    print("Mean percentage error:", mean_error)

    return predicted_force

# Example ADC data
# ADC_small = [62, 319, 436, 519, 554, 602, 621, 647, 653, 670, 677, 686, 690, 703, 715, 732] #RP-C7.6-LT
# grams_small = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]
#
# ADC_big = [15, 59, 383, 543, 637, 691, 738, 777, 792, 817, 830, 841, 845, 846, 850, 855, 858, 862] #RP-C18.3-ST
# grams_big = [15, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600]

# Tests on January 25, 2024
grams_small_31 = [30, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_small_31 = [300, 530, 890, 1110, 1350, 1450, 1510, 1620, 1650, 1700, 1760, 1830, 1910, 1950, 1990, 2020]

grams_small_21 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_small_21 = [220, 460, 900, 1070, 1170, 1250, 1290, 1320, 1400, 1535, 1600, 1645, 1640, 1720, 1790]

grams_big_11 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_big_11 = [210, 431, 559, 851, 1119, 1339, 1453, 1589, 1685, 1829, 1917, 1957, 2007, 2037, 2100]

grams_big_17 = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_big_17 = [351, 789, 1035, 1135, 1233, 1305, 1357, 1547, 1733, 1811, 1956, 2085, 2137, 2189]

# Values used for stm32
volt_in = 2.95
resistor_small = 4700
resistor_big = 2200
max_bits = 4095

# Generating plots and calculations
predicted_force = generate_plot(ADC_small_31, grams_small_31, volt_in, resistor_small, max_bits)
predicted_force = generate_plot(ADC_big_11, grams_big_11, volt_in, resistor_big, max_bits)




