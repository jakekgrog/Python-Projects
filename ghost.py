import sys, os

def create_project(project_name):
    try:
        try:
            os.mkdir(project_name)
        except OSError:
            print("Directory exists")
        try:
            os.chdir(project_name)
            print(os.getcwd())
        except OSError:
            print("Couldnt change directory")
        try:
            open("index.html", 'w+')
        except OSError:
            print("couldnt find file")
        try:
            os.mkdir('assets')
            os.mkdir('css')
        except OSError:
            print('couldnt create directories')
        try:
            os.chdir('css')
        except OSError:
            print("couldnt change to css")
        try:
            with open('style.css', 'w+') as f:
                pass
        except OSError:
            print("couldnt open style")
        os.chdir('../assets')
        os.mkdir('javascript')
        os.mkdir('images')
    except:
        print("Unhandled exception")

def main():
    project_name = sys.argv[1]
    create_project(project_name)

if __name__=="__main__":
    main()
