import numpy as np

# Initial data
sensor = np.arange(72000, 1800, -10)  # Ohms (20 grams - 2000)
resistor = np.arange(100, 40000, 100)  # Ohms
volt = 2.95  # V
bit = 4096

# Creating data for the plot
voltages = [i / bit * volt for i in range(bit + 1)]
values = list(range(bit + 1))

max_difference = -float('inf')  # Initializing max difference as negative infinity
max_resistor = None  # Initializing resistor value corresponding to the max difference

for i in range(len(resistor)):
    current = volt / (resistor[i] + sensor)
    volt_aoc = current * resistor[i]

    min_voltage_aoc = np.min(volt_aoc)
    max_voltage_aoc = np.max(volt_aoc)

    m, b = np.polyfit(voltages, values, 1)
    values_min = m * min_voltage_aoc + b
    values_min = int(round(values_min))
    values_max = m * max_voltage_aoc + b
    values_max = int(round(values_max))

    difference = values_max - values_min

    if difference > max_difference:
        max_difference = difference
        max_resistor = resistor[i]
        max_values_min = values_min
        max_values_max = values_max

print(f"Maximum difference between values_max and values_min: {max_difference}")
print(f"Resistor corresponding to this difference: {max_resistor} Ohms")
print(f"For this resistor, values_min: {max_values_min} and values_max: {max_values_max}")

