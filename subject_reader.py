"""
I had ask to my classmate so it may some logical is similar
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    for each in data:
        print(f'{each[0]} is taught by {each[1]} and has {each[2]} students')  # I still not so understand why and how


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    dossier = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        dossier.append(parts)
    input_file.close()
    return dossier


main()