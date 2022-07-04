import os
import shutil


directory = os.getcwd()

def build_docs():
    os.makedirs(os.path.join(directory,'docs','_build','html'), exist_ok=True)
    shutil.copyfile(os.path.join(directory,'docs','_static','index.html'), os.path.join(directory,'docs','_build','html','index.html'))
    os.system(f"sphinx-build -a -b html -D language=es {os.path.join(directory,'docs')} {os.path.join(directory,'docs','_build','html','es')}")
    os.system(f"sphinx-build -a -b html -D language=en {os.path.join(directory,'docs')} {os.path.join(directory,'docs','_build','html','en')}")

if __name__ == '__main__':

    build_docs()
