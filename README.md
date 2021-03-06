# Flask Best Practices

A simple `Flask` codebase that provides best practices for a secure production deployment.

> Status: **WIP** (not stable)

<br />
<br />

> Checklist 

| Status | Item | info | 
| --- | --- | --- |
| ✔️ | `Up-to-date Dependencies` | - |
| ✔️ | Flask-Login, Flask-SqlAlchemy | - |
| ✔️ | BS5 for styling | Local path (latest BS5 stable version) |
| ✔️ | Simple Custom Login / Register pages | - | 
| ✔️ | Password Recovery | - | 
| ✔️ | Unitary tests | - |
| ✔️ | SCSS to CSS compilation | via pyScss |
| ✔️ | Rate Limiter for Login & Register | via [Flask-RateLimiter](https://pypi.org/project/Flask-RateLimiter/) |
| ✔️ | [Flask-Talisman](https://pypi.org/project/flask-talisman/) | Default policy |
| ✔️ | Passwords Checks | Configurable Min/Max Lenght, Strength WIP |
| ✔️ | Check email is valid & exists | via [validate-email-address](https://pypi.org/project/validate-email-address/) package |
| ✔️ | Failed Logins Count | - |
| ❌ | Account Suspension for X failed logins | Limit in Config |
| ✔️ | Page Compression | via [Flask-Minify](https://pypi.org/project/Flask-Minify/) |
| ✔️ | Deployment | [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) / Nginx (reverse proxy) | 
| ✔️ | HEROKU integration | TODO add secrets to git repo | 
| ✔️ | Docker | - |

<br />

## ✨ Build from sources

```bash
$ # Clone the sources
$ git clone https://github.com/app-generator/sample-flask-best-practices.git
$ cd sample-flask-best-practices
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
$
$ # Run the application
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the app in browser: http://127.0.0.1:5000/
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## ✨ Build from docker
```bash
$ # Run using docker-compose
$ docker-compose build  # This will build the containers
$ docker-compose up     # This will bring up the application
$ # Open the application on you browser using you IPv4 Address on your browser i.e., only 2 routes available for auth /login ,/register
$ # To find IPv4 Address
$ # (Windows) ipconfig
$ # (Unix/Mac) ifconfig
```

## ✨ Deploy on github workflow
```bash
$ # First set the git secrets using this https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository
$ # Add the following keys to the secrets : HEROKU_APP_NAME , HEROKU_EMAIL , HEROKU_API_KEY
$ # In the Dockerfile comment the line `CMD [ "uwsgi", "--socket", "0.0.0.0:5000", "--protocol", "http", "--wsgi", "run:app" ]`
$ # Use the direct flask application run by uncommenting/adding the line `CMD [ "python", "run.py"]`
$ # on push to the master/main the GH workflow will automatically create and push the image to your heroku
```

## ✨ Code-base structure
The project has a super simple structure, represented as below:
```
< PROJECT ROOT >
   |
   |-- app/
   |    |
   |    |-- __init__.py                 # Initialization of app
   |    |-- config.py                   # Handlers for the front end routes
   |    |-- setup_security.py                      
   |    |-- auth/
   |    |
   |    |   |-- __init__.py
   |    |   |-- email.py
   |    |   |-- forms.py
   |    |   |-- models.py               # Database models for storing data
   |    |   |-- routes.py               # REST API hanlder
   |    |
   |    |-- static/                     # CSS files, Javascripts files
   |    |   
   |    |   |-- css/
   |    |   |
   |    |   |   |-- bootstrap.min.css
   |    |   |   |-- bootstrap.min.css.map
   |    |   |   |-- style.css
   |    |   |
   |    |   |-- js/
   |    |   |
   |    |   |   |-- bootstrap.min.js
   |    |   |   |-- jquery.min.js
   |    |   |
   |    |-- templates/
   |    |
   |    |    |-- auth/                    # Auth related pages login/register
   |    |    |
   |    |    |    |-- login.html
   |    |    |    |-- register.html
   |    |    |    |-- reset_password.html
   |    |    |    |-- reset_password_request.html
   |    |    |
   |    |    |-- bootstrap/
   |    |    |
   |    |    |    |-- bs5_base.html
   |    |    |
   |    |    |-- email/
   |    |    |  
   |    |    |    |-- reset_password.html
   |    |    |    |-- reset_password.txt
   |    |    |
   |    |    |-- forms/
   |    |    |
   |    |    |    |-- forms.html
   |    |    |
   |    |    |-- navbar/
   |    |    |  
   |    |    |    |-- messages.html
   |    |    |    |-- navbar.html
   |    |    |-- base.html
   |    |
   |    |-- utils/
   |    |
   |    |    |-- __init__.py
   |    |    |-- app_logger.py
   |    |    |-- decorators.py
   |    |    |-- mailer.py
   |    |
   |-- requirements.txt
   |-- run.py
   |
   |-- ************************************************************************
```
  
> **@ToDo**

<br />

## ✨ Recompile CSS

To recompile SCSS files, follow this setup:

> **@ToDo**

<br />

--- 
**Flask Best Practices** - Provided by AppSeed
