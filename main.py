import pandas as pd
# import matplotlib.pyplot as plt

G = 1.327E11
pi = 3.14159
c = 2.998E5

# Asking for user input
SolarMass = float(input("How many solar masses do you want to start: "))
S = int(SolarMass)

data = []

for m in range(S, 500, 100):
    C = 4 * pi * G * m / (c * c)
    data.append((m, C))
   # print("Hole Mass: ", m, "solar masses")
   # print("Circumference: ", C, "kilometers\n")

# Create a DataFrame
df = pd.DataFrame(data, columns=['Black Hole Mass (Solar Masses)', 'Circumference (kilometers)'])

# Display DataFrame
print(df)

# Plotting the data
# plt.plot(df['Black Hole Mass (Solar Masses)'], df['Circumference (kilometers)'], marker='o', linestyle='-')
# plt.xlabel('Black Hole Mass (Solar Masses)')
# plt.ylabel('Circumference (kilometers)')
# plt.title('Circumference of Event Horizon for Different Black Hole Masses')
# plt.grid(True)
# plt.show()
