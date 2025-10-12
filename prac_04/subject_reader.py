"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    """Load data from file and display subject information."""
    data = load_data()

def load_data():
    """Read data from file formatted """
    subject_data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])  # Convert student count to int
        subject_data.append(parts)
    input_file.close()
    return subject_data

main()