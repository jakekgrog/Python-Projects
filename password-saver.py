import sys

def argparser(site, name, password):
    with open("passwords.txt", "a") as f:
        line = site + " " + name + " " + password + "\n"
        f.write(line)
    
def fetcher(site):
    with open("passwords.txt", "r") as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            parts = lines[i].strip().split()
            if parts[0] == site:
                print parts[1:]
            i += 1
                
    
def main():
    site = sys.argv[1]
    if len(sys.argv) > 2:
        name = sys.argv[2]
        password = sys.argv[3]
        argparser(site, name, password)
    else:
        fetcher(site)

if __name__ == "__main__":
    main()