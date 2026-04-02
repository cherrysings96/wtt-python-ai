# with shutil

import shutil

with open("data.txt", "w+") as f:
    f.write("Hello good morning how is your day")
    f.seek(0)
    data = f.read()
    print(data)

shutil.copy("data.txt", "new.txt")