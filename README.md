# Blog Webpage (Demo)

## Setup Guide
1. Clone the repository
```commandline
git clone https://github.com/LinLin-0628/BiliBili-Django-Tutorial.git

OR

git clone git@github.com:LinLin-0628/BiliBili-Django-Tutorial.git
```

2. Setup python virtual environment (For MacOS & Linux)
```commandline
cd BiliBili-Django-Tutorial
python -m venv .venv
source venv/bin/activate
```

3. Install all dependencies (modules / packages)
```commandline
pip install -r requirements.txt
```

4. Change database settings if needed
```ignorelang

```

5. Migrate database
```commandline
python manage.py makemigrations
python manage.py migrate
```

6. Run server
```commandline
python manage.py runserver
```