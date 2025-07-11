# Antibiotic Dosage Range Calculator

# Step 1: Get user input
weight = float(input("Enter patient body weight in kg: "))
drug = input("Enter the antibiotic name: ").lower()

# Step 2: Define dosage guidelines (mg/kg/day or mg/kg/dose for antibiotics)
antibiotic_dosage_guidelines = {
    "amoxicillin": (20, 40),     # mg/kg/day
    "azithromycin": (10, 12),    # mg/kg/day
    "cefixime": (8, 12),         # mg/kg/day
    "ciprofloxacin": (10, 15),   # mg/kg/dose
    "erythromycin": (30, 50),    # mg/kg/day
    "clindamycin": (8, 25),      # mg/kg/day
    "metronidazole": (15, 30),   # mg/kg/day
    "chloramphenicol": (50, 100) # mg/kg/day
}

# Step 3: Check if drug is in the antibiotic list
if drug in antibiotic_dosage_guidelines:
    min_dose, max_dose = antibiotic_dosage_guidelines[drug]

    # Calculate weight-based dose range
    min_total = min_dose * weight
    max_total = max_dose * weight

    # Display result
    print(f"\n Recommended daily dose for {drug.title()} based on {weight} kg body weight:")
    print(f"   ➤ Minimum dose: {min_total:.2f} mg/day")
    print(f"   ➤ Maximum dose: {max_total:.2f} mg/day")
else:
    print(" Sorry, this antibiotic is not in the dosage database.")

