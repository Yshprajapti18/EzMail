python3.10 -m ensurepip --default-pip
python3.10 -m pip install --upgrade pip
pip install -r requirements.txt
python3.10 manage.py collectstatic
