import glob

my_path = '/Program Files'

files = glob.glob(my_path + '/**', recursive=True)

print(files)

