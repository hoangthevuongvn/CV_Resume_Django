# CV_Resume_Django from Hoàng Thế Vượng

How to install:

Install virtualenv If you haven't installed yet:
python3 -m pip install --user virtualenv

Create youre virtual environment:
python3 -m venv your_env_name

Activate virual environment:

On Windows, run:
your_env_name\Scripts\activate.bat

On Linux or MacOS, run:
source youre_env_name/bin/activate

Clone Source:
git clone https://github.com/hoangthevuongvn/CV_Resume_Django.git

cd CV_Resume_Django

Install all the necessary packages:
python -m pip install -r requirements.txt

Complete all of the migrations:
python manage.py makemigrations
python manage.py migrate

Create a super user for yourself:
python manage.py createsuperuser

Run server:
python manage.py runserver










