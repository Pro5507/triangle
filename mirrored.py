a = int(input("Enter the number of rows: "))
for i in range(a):
    # Print spaces for mirroring the triangle
    for j in range(a - i - 1):
        print("  ", end="")  # Two spaces to maintain the structure
    # Print the asterisks
    for j in range(i + 1):
        print("* ", end="")
    print()  # Move to the next line
