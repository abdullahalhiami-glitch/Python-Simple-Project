for i in range(1, 13):
    row = ""
    for j in range(1, 13):
        # Formats each calculation to be 12 characters wide to ensure alignment
        row += f"{i} x {j} = {i * j:<4} | "
    print(row)


