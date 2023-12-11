echo("Building Awesome Recipe")
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
echo("Awesome Recipe is now LIVE")