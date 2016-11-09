import os, shutil

def extract(path, ext):
    for root, dirs, files in os.walk("./data/dump", topdown=False):
        for name in files:
            if name.split('.')[-1] == ext:
                shutil.move(os.path.join(root, name), os.path.join('./data/%s'%ext, name))
                print "[SUCCESS]", os.path.join(root, name), "->", os.path.join('./data/%s'%ext, name)



if __name__ == '__main__':
    root = "./data/dump"
    langs = ['py', 'java', 'rb', 'cpp', 'c']

    [extract(root, x) for x in langs]
