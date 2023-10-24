def convert(n):
    # Base case: if number is 0, return 0.
    if n==0:
        return 0
    
    # Extracting the last digit of the number.
    digit = n % 10
    
    # If the digit is 0, replace it with 5.
    if digit == 0:
        digit = 5
    
    # Recursively converting the remaining part of the number and multiplying it by 10 to add the replaced digit.
    return convert(n//10) * 10 + digit

# Function to convert all 0s to 5s in a given number (wrapper function).
def convertFive(n):
    # Base case: if number is 0, return 5.
    if n==0:
        return 5
    else:
        # Calling the recursive function to convert the number.
        return convert(n)
