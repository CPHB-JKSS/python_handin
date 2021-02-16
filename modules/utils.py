import os


def get_file_names(folderpath, out='files/output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    with open(out, 'w') as file_object:
        for root, dirs, files in os.walk(folderpath):
            for filename in files:
                file_object.write(filename + '\n')


def get_all_file_names(folderpath, out='files/output.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    # print(folderpath)

    folder = []
    with open(out, 'a') as file_object:

        for element in os.listdir(folderpath):
            if os.path.isdir(element):
                # print(element)
                file_object.write(element + '\n')
                folder.append(element)
            else:
                #print('- ' + element)
                file_object.write(element + '\n')

    for f in folder:
        get_all_file_names(folderpath + '/' + f)

        # for root, dirs, files in os.walk(folderpath):
        #     for directory in dirs:
        #         file_object.write(directory + '\n')
        #         for filename in files:
        #             file_object.write('- ' + filename + '\n')


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for file in file_names:
        with open('files/' + file) as file_object:
            for line in file_object:
                print(line)
                break


def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for file in file_names:
        with open('files/' + file) as file_object:
            for line in file_object:
                if '@' in line:
                    print(line)


def write_headlines(md_files, out='files/output.txt'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    for file in md_files:
        with open('files/' + file) as file_object:
            for line in file_object:
                if '#' in line:
                    with open(out, 'a') as file_object:
                        file_object.write(line)
