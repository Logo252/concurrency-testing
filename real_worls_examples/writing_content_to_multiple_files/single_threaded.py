import os
from time import perf_counter


def replace_file_string_to_new_one(file, string, new_string):
    file_name = file.split('/')[-1]
    print(f'Processing the file {file_name}')

    with open(file, 'r') as f:
        content = f.read()

    content = content.replace(string, new_string)

    # Adding sample content
    # content = 'This is a sample content for the file file.txt'

    # write data into the file
    with open(file, 'w') as f:
        f.write(content)


def main():
    filed_dir = os.getcwd() + '/files'
    files = [
        filed_dir + '/file1.txt',
        filed_dir + '/file2.txt',
        filed_dir + '/file3.txt',
        filed_dir + '/file4.txt',
        filed_dir + '/file5.txt',
        filed_dir + '/file6.txt',
        filed_dir + '/file7.txt',
        filed_dir + '/file8.txt',
        filed_dir + '/file9.txt',
        filed_dir + '/file10.txt',
        filed_dir + '/file11.txt',
        filed_dir + '/file12.txt',
        filed_dir + '/file13.txt',
        filed_dir + '/file14.txt',
        filed_dir + '/file15.txt',
        filed_dir + '/file16.txt',
        filed_dir + '/file17.txt',
        filed_dir + '/file18.txt',
        filed_dir + '/file19.txt',
        filed_dir + '/file20.txt',
    ]

    for file in files:
        file_name = file.split('/')[-1]
        replace_file_string_to_new_one(file, string='file.txt', new_string=file_name)


if __name__ == "__main__":
    start_time = perf_counter()

    main()

    end_time = perf_counter()
    how_long_in_ms = (end_time - start_time) * 1000
    print(f'It took {how_long_in_ms :0.2f} ms to complete.')
