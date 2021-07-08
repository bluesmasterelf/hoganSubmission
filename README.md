Greetings,

To boot the app, please perform the following steps. 

1) clone repo

2) If you open a separate command prompt or terminal, 
activate the environment by running 
source env/bin/activate (Linux/macOS) or
env\scripts\activate (Windows). 
You know the environment is activated when the command prompt shows (env) at the beginning.
Note: application was developed and tested in Windows 10 Pro Environment.

3) execute python manage.py migrate

4) execute python manage.py runserver

5) In Google Chrome, navigate to localhost:8000


Notes:
- I followed the this tutorial and modified as needed: https://code.visualstudio.com/docs/python/tutorial-django
- The database is the default sqlite3 and can be managed directly as such
- I've left css, styling and such very minimal as I'm not using React and there's really no end to how much time you can sink into such matters. 
- The testing is 'comprehensive' insofar as each main kind of testing (service, unit, repository) is demonstrated, 
	but rather than duplicate and modify for every case, I tried to get at least one example of each kind of test for each kind of file or method.
- The navigation is obviously quite clunky. I'd normally want in-view dynamic page generation without leaning so heavily on pathing. 
- I've never really used Django before. 
- I've never used Python for enterprise efforts before - only very many proof of concept scripts to justify work in a language like Java or C#

