# Problem: Find the smallest B where A×B is a perfect square
A = int(input())
B = 1  # Initialize B (will store our answer)

# Step 1: Factorize A into its prime factors
i = 2  # Start checking from the smallest prime (2)
while i * i <= A:  # Check up to sqrt(A) (no need to check larger than this)
    count = 0  # Count how many times 'i' divides A (exponent of 'i' in A's factors)
    
    # Keep dividing A by 'i' as long as it's divisible
    while A % i == 0:
        count += 1  # Increment exponent count
        A = A // i  # Reduce A by removing one factor of 'i'
    
    # Step 2: If the exponent of 'i' is odd, we need to include 'i' in B once
    # This makes the total exponent (original + 1) even
    if count % 2 != 0:
        B *= i  # Multiply B by 'i'
    
    i += 1  # Check the next possible factor

# Step 3: After loop, if A > 1, it means A itself is a prime number
# Its exponent is 1 (odd), so we must include it in B
if A > 1:
    B *= A

# Output the smallest B
print(B)
    