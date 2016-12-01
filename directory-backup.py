import os

def main():
    files = os.listdir(".")
    i = 0
    while i < len(files):
        file_ext = files[i].split(".")[-1]
        if os.path.isfile(files[i]) == True and file_ext != "bak":
            with open(files[i], "r") as file_src:
                w = file_src.read()
            with open(files[i] + ".bak", "w") as f:
                f.write(w)
        i += 1
        
if __name__ == "__main__":
    main()