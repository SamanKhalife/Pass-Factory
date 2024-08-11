import itertools
import string
import os

def print_header():
    print("""
██████╗  █████╗ ███████╗███████╗      ███████╗ █████╗  ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝      ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██████╔╝███████║███████╗███████╗█████╗█████╗  ███████║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝
██╔═══╝ ██╔══██║╚════██║╚════██║╚════╝██╔══╝  ██╔══██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝
██║     ██║  ██║███████║███████║      ██║     ██║  ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝      ╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝
    """)

def get_characters(include_letters, include_digits, include_symbols):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if not characters:
        raise ValueError("At least one character type must be included.")
    return characters

def combinations(length, characters):
    # all possible combinations
    combinations = itertools.product(characters, repeat=length)

    return (''.join(comb) for comb in combinations)

def save(length, characters, filename):
    try:
        # Open a file to write
        with open(filename, "w") as file:
            for comb in combinations(length, characters):
                file.write(comb + "\n")
        print(f"All combinations of length {length} saved to '{filename}'.")
    except MemoryError:
        print("MemoryError: The file is too large to fit in memory. Consider using a smaller length.")

def main():
    print_header()
    try:
        # Get user input
        include_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        include_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'

        length = int(input("Enter the desired combination length: "))
        if length < 1:
            print("Combination length must be at least 1.")
            return

        characters = get_characters(include_letters, include_digits, include_symbols)

        filename = input("Enter the file name to save the combinations (e.g., 'combinations.txt'): ").strip()

        save(length, characters, filename)
    except ValueError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()