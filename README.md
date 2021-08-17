# Ticketing System

A simple Ticketing system.
یک سیستم تیکتینگ ( پرسش و پاسخ فنی )  ساده 


## Run On Windows

If You're On A Windows Machine , Make Environment Ready By Following Steps Below:
1. Install `python3`, `pip`, `virtualenv` 
2. Clone the project using:  `git clone https://github.com/tahadelshadi/ticketing.git`.
3. Make Environment Ready Like This:
``` Command Prompt
cd ticketing
virutalenv venv # Give Full Path To python.exe
venv\Scripts\activate
pip install -r requirements.txt # install requirements
python manage.py makemigrations 
python manage.py migrate # Create Database Tables

```
4. Run `Ticketing` using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your Ticketing version.

## Used in :

- [Tajrobam social media (soon) ]('#')


## TODO
- [x] logging system
- [x] registration system
- [x] creating department model
- [x] requirements.txt file
