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

    # Creating a bar plot for the difference between real and predicted data
    difference = np.array(grams) - power_law(np.array(conductance), c, d)

    # Finding the index of the maximum difference
    max_diff_index = np.argmax(np.abs(difference))

    # Defining colors for each bar
    colors = ['red' if i == max_diff_index else 'blue' if d < 0 else 'green' for i, d in enumerate(difference)]

    plt.bar(grams, difference, alpha=1, color=colors, width=40, label='Difference')

    plt.title('Difference between force and predicted force for RP-C18.3-ST')
    plt.xlabel('Force [g]')
    plt.ylabel('Difference [g]')

    # Adding labels for values on the X-axis
    plt.xticks(grams, fontsize=8)  # Setting a smaller font size
    plt.yticks(fontsize=8)  # Setting a smaller font size

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

    # Finding and printing the maximum difference value
    max_difference = np.max(np.abs(difference))
    print("Maximum difference value:", max_difference)

    return predicted_force


# Test data
grams_small_31 = [30, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_small_31 = [300, 530, 890, 1110, 1350, 1450, 1510, 1620, 1650, 1700, 1760, 1830, 1910, 1950, 1990, 2020]

grams_big_11 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]
ADC_big_11 = [210, 431, 559, 851, 1119, 1339, 1453, 1589, 1685, 1829, 1917, 1957, 2007, 2037, 2100]

# Values applied to stm32
volt_in = 2.95
resistor_small = 4700
resistor_big = 2200
max_bits = 4095

# Generating plots and calculations
predicted_force_small = generate_plot(ADC_small_31, grams_small_31, volt_in, resistor_small, max_bits)
predicted_force_big = generate_plot(ADC_big_11, grams_big_11, volt_in, resistor_big, max_bits)
