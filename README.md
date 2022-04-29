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
| ❌ | BS5 for styling | Local path (latest BS5 stable version) |
| ❌ | Simple Custom Login / Register pages | - | 
| ❌ | Password Recovery | - | 
| ❌ | Unitary tests | - |
| ❌ | SCSS to CSS compilation | via Gulp |
| ✔️ | Rate Limiter for Login & Register | via [Flask-RateLimiter](https://pypi.org/project/Flask-RateLimiter/) |
| ✔️ | [Flask-Talisman](https://pypi.org/project/flask-talisman/) | Default policy |
| ❌ | Passwords Checks | Configurable Min/Max Lenght, Strength |
| ❌ | Check email is valid & exists | via [validate-email-address](https://pypi.org/project/validate-email-address/) package |
| ❌ | Failed Logins Count | - |
| ❌ | Account Suspension for X failed logins | Limit in Config |
| ❌ | Page Compression | via [Flask-Minify](https://pypi.org/project/Flask-Minify/) |
| ❌ | Deployment | [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/) / Nginx (reverse proxy) | 
| ❌ | HEROKU integration | - |
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

## ✨ Code-base structure

The project has a super simple structure, represented as bellow:

> **@ToDo**

<br />

## ✨ Recompile CSS

To recompile SCSS files, follow this setup:

> **@ToDo**

<br />

--- 
**Flask Best Practices** - Provided by AppSeed
