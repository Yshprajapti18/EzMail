python3 -m ensurepip --default-pip
python3 -m pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py collectstatic
