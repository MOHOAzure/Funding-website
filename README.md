# Funding website
A django-based website for funding hack day projects

![](https://i.imgur.com/SCzH9MR.png)

## Env Requriements
- Python 3.8.5
- Django 3.0

## Run server steps
- python manage.py makemigrations funding
- python manage.py migrate --run-syncdb
- python manage.py loaddata init.json (fill db with a superuser, a funder, and a demo project)
- python manage.py runserver
  
  

## Webpages
- Home/Login page: [site.url]
	- Account: user_demo / user_password
- Funding page: [site.url]/funding (redirected after login)
- Logout page: [site.url]/logout
- Admin page: [site.url]/admin
	- Account: admin_demo / admin_demo


