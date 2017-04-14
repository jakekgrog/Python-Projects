import sys, os

def create_project(project_name):
    try:
        os.mkdir(project_name)
    except OSError:
        print("Directory exists!")

    try:
        os.chdir(project_name)

        open("index.html", 'w+')

        os.mkdir('assets')
        os.mkdir('css')
        os.chdir('css')

        with open('style.css', 'w+') as f:
            pass

        os.chdir('../assets')
        os.mkdir('javascript')
        os.mkdir('images')
    except:
        print("Unhandled exception.")

def main():
    project_name = sys.argv[1]
    create_project(project_name)

if __name__=="__main__":
    main()
