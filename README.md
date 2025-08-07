python3 -m venv env
source env/bin/activate

pip3 install flask

pip freeze > requirements.txt

pip install -r requirements.txt

python3 loginface.py
