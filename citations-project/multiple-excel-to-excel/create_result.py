import os
os.chdir(os.path.dirname(__file__))
cwd = os.getcwd()

for file in os.listdir(cwd):
    filename = os.fsdecode(file)
    if filename.endswith('.xlsx'):
        print(filename)
    else:
        pass