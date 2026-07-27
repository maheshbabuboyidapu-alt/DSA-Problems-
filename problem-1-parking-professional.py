# Parking Fee Calculator with Tiered Rates
base_rate = 30  # First 2 hours
tier2_rate = 20  # Hours 2-5
tier3_rate = 10  # Hours 5+

# Taking input from customer
h = int(input("Enter the number of hours parked: "))

# If vehicle parked below or equal to 2 hours
if h <= 2:
    print(f"The fee of parking is ₹{base_rate}")

# If vehicle parked between 2 and 5 hours
elif h <= 5:
    tier2_hours = h - 2
    total_rate = base_rate + (tier2_rate * tier2_hours)
    print(f"The fee of parking is ₹{total_rate}")

# If vehicle parked more than 5 hours
elif h > 5:
    tier2_total = tier2_rate * 3
    tier3_hours = h - 5
    total = base_rate + tier2_total + (tier3_hours * tier3_rate)
    
    # Apply 10% discount if fee is above 200
    if total > 200:
        discount = total * 0.10
        total -= discount
    
    print(f"The fee of parking is ₹{total}")