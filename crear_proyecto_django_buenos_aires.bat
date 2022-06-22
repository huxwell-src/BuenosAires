python3 -m pip install --upgrade pip
pip install --upgrade virtualenv
python3 -m venv "C:\ProyectosDjango\AppWebBA_venv"
call cd /D "C:\ProyectosDjango"
call AppWebBA_venv\Scripts\activate.bat
python3 -m pip install --upgrade pip
pip install django
pip install cx_oracle
pip install pillow
pip install djangorestframework
call django-admin startproject AppWebBA
call cd AppWebBA
python3 manage.py startapp core
python3 manage.py startapp apirest
pip freeze > requirements.txt
call code "C:\ProyectosDjango\AppWebBA"