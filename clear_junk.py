import os, time
from datetime import datetime

path = 'C:\\Users\\lawre\\Downloads\\Junk\\'

files = os.listdir(path)
removed_files = []

for f in files:
    d_modified = datetime.strptime(time.ctime(os.path.getmtime(path + '\\' + f)), '%a %b %d %H:%M:%S %Y')
    diff = datetime.today() - d_modified

    f_size = os.path.getsize(path + '\\' + f)/1000000

    if(diff.days > 20):
        os.remove(path+'\\'+f)
        removed_files.append(f'{f}\t{f_size}MB')

with open(r'C:\Users\lawre\Downloads\Projects\automate_stuff\clear_junk_log.tsv', 'a+') as f:
    f.write(f"{datetime.today().strftime('%d-%b-%Y')}: ")

    if not removed_files:
        f.write("No files removed today\n")
    else:
        for fi in removed_files:
            f.write(f'{fi}\n')

exit()