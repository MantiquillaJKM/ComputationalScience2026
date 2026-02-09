from decimal import Decimal, getcontext, ROUND_HALF_UP

# Set precision to handle 100+ decimals
getcontext().prec = 120 

# Pi to 100 decimals
pi_100 = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')

def truncate(number, n):
    s = str(number)
    if '.' in s:
        integer, decimal_part = s.split('.')
        return Decimal(f"{integer}.{decimal_part[:n]}")
    return number

def round_decimal(number, n):
    return number.quantize(Decimal(10)**-n, rounding=ROUND_HALF_UP)

# Your specific test intervals
decimals = [20, 40, 60, 80, 100]

# Sphere Volume: 4/3 * pi * r^3
r = Decimal(5)
multiplier = (Decimal(4)/3) * (r**3)

# To store results for gap calculation
results = []

for d in decimals:
    pi_trunc = truncate(pi_100, d)
    pi_round = round_decimal(pi_100, d)
    
    v_trunc = multiplier * pi_trunc
    v_round = multiplier * pi_round
    
    # Store results to compare decimal stages later
    results.append({
        'decimal': d,
        'v_trunc': v_trunc,
        'v_round': v_round
    })
    
    print(f"\n[ DECIMAL PLACES: {d} ]")
    print(f"Truncated Volume: {v_trunc}")
    print(f"Rounded Volume:   {v_round}")
    print("-" * 50)

print("\n--- DIFFERENCE BETWEEN DECIMAL STAGES (THE GAP) ---")
# Calculate the difference between consecutive decimal precisions
for i in range(1, len(results)):
    prev = results[i-1]
    curr = results[i]
    
    gap_trunc = curr['v_trunc'] - prev['v_trunc']
    gap_round = curr['v_round'] - prev['v_round']
    
    print(f"\n[ STAGE GAP: {prev['decimal']} to {curr['decimal']} Decimals ]")
    print(f"Truncation Change: {gap_trunc:.2e}")
    print(f"Rounding Change:   {gap_round:.2e}")