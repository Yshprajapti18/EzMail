python3.11 -m ensurepip --default-pip
python3.11 -m pip install --upgrade pip
pip install -r requirements.txt
python3.11 manage.py collectstatic
