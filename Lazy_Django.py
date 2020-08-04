import subprocess
import os


def test():
    print('its working')

def create_env():
    process1 = subprocess.run("python -m venv env ",shell=True)
    print('please activate your env manually and then perform the additional steps')
    exit()


def install_django():
    process1 = subprocess.run("pip install Django",shell=True)
    print("Django installed")

def start_server():
    process1 = subprocess.run("django-admin startproject server")
    print("your server name is 'server' by default")

def migrate():
    process1 = subprocess.run("python .\server\manage.py makemigrations",shell=True)
    process2 = subprocess.run("python .\server\manage.py migrate",shell=True)

def create_super_user():
    process1 = subprocess.run("python .\server\manage.py createsuperuser",shell=True)


def run_server():
    subprocess.call('start python .\server\manage.py runserver', shell=True)

def create_app():
    app_name = input('The App Name: ')
    process1 = subprocess.run(f"python .\server\manage.py startapp {app_name}",shell=True)




print('please make sure that your env is activated')
while True:
    print('''
    [0]-Test
    [1]-Create the env
    [2]-Install Django
    [3]-Create server
    [4]-Migrate DB
    [5]-Create Admin
    [6]-Run server
    [7]-Create App
    [*]-Do it All

    ''')
    x = input('Choose Command: ')
    if x == '1':
        create_env()
    elif  x == '2':
        install_django()
    elif x == '3':
        start_server() 
    elif x == '4':
        migrate()
    elif x == '5':
        create_super_user()
    elif x == '6':
        run_server()
    elif x == '7':
        create_app()
    elif x == '*':
        install_django()
        start_server()
        migrate()
        create_super_user()
        run_server()
        print('All done')
    elif x == '0':
        test()
    else:
        print('ERROR')
