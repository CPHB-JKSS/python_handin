import argparse


def print_file_content(file):
    """Can print content of a csv file to the console"""

    with open(file) as file_object:
        contents = file_object.read()

    print(contents)


def write_list_to_file(output_file, lst):
    """Can take a list of tuple and write each element to a new line in file"""

    with open(output_file, 'w') as file_object:
        for t in lst:
            for element in t:
                file_object.write(element + '\n')


def write_arb_strings_to_file(output_file, *strings):
    """Can take an arbitrary number of strings and write each element to a new line in file"""

    with open(output_file, 'w') as file_object:
        for s in strings:
            file_object.write(s + '\n')


def read_csv(input_file):
    """Take a csv file and read each row into a list"""
    lst = []
    with open(input_file) as file_object:
        for row in file_object:
            lst.append(row)

    return lst


# Used for when you run the module seperately.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Used to read and write to text files locally'
    )
    parser.add_argument('file', help='')
    parser.add_argument('destination', help='')
