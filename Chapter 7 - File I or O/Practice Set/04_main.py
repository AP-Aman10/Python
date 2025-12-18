def generate_table(number):
    """
    Generate a multiplication table for 'number' and save it to a file,
    including a completion message at the end.
    """
    table_content = ""
    for i in range(1, 11):
        table_content += f"{number} X {i} = {number * i}\n"

    # Add completion message at the end of the table
    table_content += f"\n--- Multiplication Table of {number} Completed ---"

    # Make sure the folder "tables" exists manually before running
    file_path = f"Chapter 7 - File I or O/Tables/Table_{number}.txt"
    with open(file_path, "w") as file:
        file.write(table_content)

    print(f"Table of {number} has been saved.")

# Generate tables from 1 to 20
for num in range(1, 21):
    generate_table(num)