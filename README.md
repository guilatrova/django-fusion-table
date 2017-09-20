# Django Fusion Tables

## About this project

A simple project which handles locations in Google Maps while manipulating data in database and Google Fusion Tables.
It basically: 

- Validates if your location is valid (not a wood/mountain/ocean area)
- Save lat, lon and addres both to database as Google Fusion Tables

But you also can: reset both data, lists data from database, view your locations in maps retrieved from Fusion Tables.

**Warning** This project uses some **ES6 stuff**. It don't uses Angular/React/Webpack/Babel to avoid over-engineering and keep it simple.

## `djgmaps` module
Main django module, contains base `urls.py` and `settings.py`.

## `fusiontables` module
It centers every logic and handling to Google Fusion Tables (as name suggests). **This module is highly reusable, can be set in any other Django project.** Following **S**olid principles, you will find there:

- **GoogleAuthFactory** - Used to build Google Authentication stuff, like url, credentials and service. _(can be found in factories.py)_
- **Permissions** - Checks if a user can manipulate data (Already did a login, Google Auth Session not expired) _(can be found in permissions.py)_
- **FusionTableService** - Handles requests/queries to Google Fusion Tables. _(can be found in services.py)_
- **views.py** - Only one view that redirects to Google OAuth URL.
- **decorators.py** - You may find really cool stuff over there. It makes easy to inject new behaviors in some requests.

### Module dependencies & requirements
It requires:
- djangorestframework
- google-api-python-client
- client_secrets.json file
- `CREDENTIALS_KEY` and `TABLE_ID` set in `settings.py`

## `locations` app

This app implements models and uses service from above module. Note how it's **higly decoupled** from it. You will find only a bind with decorators and permissions in `views.py` which handles requests to default module and uses service provided by `fusiontables`.

## Scripts

It uses jQuery, bootstrap, and a simple third party file that extends jQuery to allows `$.delete`. You will find also:

#### `gmaps.js`

Handle Google Maps stuff like:
- Start map
- Bind fusion table to it
- Handle map click
- Validates address

#### `locations.js`

Handle API stuff like:
- Save location
- Retrieve locations
- Display locations in table
- Reset locations
- Display error message

# Run it (Windows)

```
git clone https://github.com/guilatrova/django-fusion-table.git          
virtualenv .ve
.ve\scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```