import numpy as np
import matplotlib.pyplot as plt

# Data
sensor = np.arange(60000, 1800, -10)  # Ohms (20 grams - 2000)'
resistor = 4700  # Ohms
volt = 2.95  # V
bit = 4095

current = volt / (resistor + sensor)
volt_aoc = current * resistor

# Creating data for the plot
voltages = [i / bit * volt for i in range(bit + 1)]
values = list(range(bit + 1))

# Creating the plot
plt.plot(voltages, values)

# Adding titles and axis labels
plt.title('Relationship between Voltage and Values')
plt.xlabel('Voltage (V)')
plt.ylabel('Value')

# Min and max points
min_voltage_aoc = np.min(volt_aoc)
max_voltage_aoc = np.max(volt_aoc)

# Min and max on the plot
m, b = np.polyfit(voltages, values, 1)
values_min = m * min_voltage_aoc + b
values_min = int(round(values_min))
values_max = m * max_voltage_aoc + b
values_max = int(round(values_max))

print(f"Minimum voltage value: {min_voltage_aoc} V Minimum value: {values_min}")
print(f"Maximum voltage value: {max_voltage_aoc} V Maximum value: {values_max}")
print(f"Voltage difference: {max_voltage_aoc - min_voltage_aoc} V Value difference: {values_max - values_min}")

# Filling the area between min and max points
plt.fill_between(voltages, values, color="grey", where=(voltages >= min_voltage_aoc) & (voltages <= max_voltage_aoc))
plt.scatter([min_voltage_aoc, max_voltage_aoc], [values_min, values_max], c='red', label='Points (min, max)')

# Displaying the plot
plt.legend()
plt.show()

print(f"Manufacturer data values:")
print(f"Voltage: 0..{volt}V   |   Working range: 0..1024   |   Force: 0.2..20N")
print(f"bit/N = {round(bit/(20-0.2), 2)}")
print(f"Voltage per bit: {round(volt/bit * 1000, 2)} mV")
print(f"Calculated data values:")
print(f"Voltage: {min_voltage_aoc}..{max_voltage_aoc}V   |   Working range: {values_min}..{values_max}   |   Force: 0.2..20N")
print(f"bit/N = {round(values_max/(20-0.2), 2)}")
print(f"Voltage per bit: {round((max_voltage_aoc-min_voltage_aoc)/(values_max-values_min) * 1000, 2)} mV")







