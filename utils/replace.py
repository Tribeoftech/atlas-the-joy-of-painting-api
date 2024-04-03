"""
Helper function to replace specific characters in file
Specifically clean up resources/dates.txt into format usable by Pandas read_csv
"""


def replace_char(file: str) -> None:
    """ Replace character in file with new value/character """
    with open(file, 'r') as f:
        text = f.read()
        text = text.replace(',', '')
        text = text.replace('"', '')
        text = text.replace(' (', ',')
        text = text.replace(')', ',')
    with open('../resources/modified_dates.txt', 'w') as f:
        f.write(text)


if __name__ == '__main__':
    replace_char('../resources/dates.txt')
