import csv

with open("insurance.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)



# Print first 5 records
print("First 5 rows")

for row in data[:5]:
    print(row)

# Print total number of records
print(f"\nTotal number of records: {len(data)}")

# Separate smoker and non-smoker charges

smoker_charges = []

non_smoker_charges = []

for row in data:
    charge = float(row["charges"])
    if row["smoker"] == "yes":
        smoker_charges.append(charge)
    else:
        non_smoker_charges.append(charge)

# Calculate average charges

avg_smoker_charges = sum(smoker_charges) / len(smoker_charges)
avg_non_smoker_charges = sum(non_smoker_charges) / len(non_smoker_charges)

print(f"\nAverage insurance charge for smokers: ${avg_smoker_charges:.2f}")
print(f"Average insurance charge for non-smokers: ${avg_non_smoker_charges:.2f}")

# Separate charges based on BMI

normal_bmi_charges = []
obese_bmi_charges = []

for row in data:
    bmi = float(row['bmi'])
    charge = float(row['charges'])
    if bmi > 30:
        obese_bmi_charges.append(charge)

    else:
        normal_bmi_charges.append(charge)

avg_obese = sum(obese_bmi_charges) / len(obese_bmi_charges)
avg_normal = sum(normal_bmi_charges) / len(normal_bmi_charges)

print(f"\nAveragecharge for BMI > 30 (obese): ${avg_obese:.2f}")
print(f"\nAveragecharge for BMI <= 30 (noramal): ${avg_obese:.2f}")

# Create a dictionary to store total charges and counts for each region
region_totals = {}
region_counts = {}

for row in data:
    region = row['region']
    charge = float(row['charges'])

    # Initialize if region not in dictionary
    if region not in region_totals:
        region_totals[region] = 0
        region_counts[region] = 0

    region_totals[region] += charge
    region_counts[region] += 1

# Calculate and print average charge per region
print("\nAverage insurance charge by region:")
for region in region_totals:
    avg = region_totals[region] / region_counts[region]
    print(f"{region.title()}: ${avg:.2f}")

import matplotlib.pyplot as plt

# Calculate average charges per region (from previous step)
region_averages = {}

for region in region_totals:
    avg = region_totals[region] / region_counts[region]
    region_averages[region] = avg

# Prepare data for plotting
regions = list(region_averages.keys())
averages = list(region_averages.values())

# Create the bar chart
plt.figure(figsize=(8, 5))
plt.bar(regions, averages, color='pink')
plt.title('Average Insurance Charges by Region')
plt.xlabel('Region')
plt.ylabel('Average Charges ($)')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Show the plot
plt.tight_layout()
plt.show()
