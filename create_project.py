import os
import sys
import shutil


def activate_venv(venv_name):
    
    venv_dir = os.path.abspath(venv_name)

    os.environ["VIRTUAL_ENV"] = venv_dir

    venv_path = os.path.join(venv_dir, "Scripts")

    os.environ["PATH"] = venv_path + os.pathsep + os.environ["PATH"]


def check_for_existing_venv(filepath, venv_name):
    
    if venv_name in os.listdir(filepath):
        full_path = os.path.join(filepath, venv_name)
        shutil.rmtree(full_path)


def get_venv_name():

    if len(sys.argv) > 1:
        return sys.argv[1]
    
    return "env"

def get_project_name():

    if len(sys.argv) > 2:
        return sys.argv[2]
    
    return "src"


def build_venv(venv_name=None):

    venv_name = get_venv_name()

    venv_filepath = os.path.abspath(venv_name)
    check_for_existing_venv(os.path.dirname(venv_filepath), venv_name)

    try:
        import virtualenv

    except ImportError:
        os.system("pip install virtualenv")

    os.system(f"python -m venv {venv_name}")


def install_django():

    venv_name = get_venv_name()
    
    activate_venv(venv_name)

    os.system("pip install django")


def build_django_project(project_name=None):
    
    venv_name = get_venv_name()

    project_name = get_project_name()

    activate_venv(venv_name)

    os.system(f"django-admin startproject {project_name}")


def create_template_folder():
    
    project_name = get_project_name()

    full_path_to_project = os.path.abspath(project_name)

    os.makedirs(os.path.join(full_path_to_project, "templates"), exist_ok=True)


def install_additional_libraries():

    venv_name = get_venv_name()
    
    if len(sys.argv) > 3:
        all_libraries = " ".join(sys.argv[3:])

        activate_venv(venv_name)

        os.system(f"pip install {all_libraries}")


build_venv()
install_django()
build_django_project()
create_template_folder()
install_additional_libraries()
