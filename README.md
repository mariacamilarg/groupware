# GROUPWARE

Project for: Groupware and Collaborative Systems @ Université Paris-Sud

## How to run it

Install the app from root directory groupware/

```
pip install --editable .
```

Instruct flask to use the right application

```
export FLASK_APP=keepcode
```

If you're developping:

```
export FLASK_ENV=development
```

If you are initializing the database for the first time:

```
flask init-db
```

Now you can run it on the web:

```
flask run
```

The application will greet you on http://localhost:5000/

## Built With

* Python
* Flask
* Bootstrap [minty](https://bootswatch.com/minty)

## Authors

* **Maria Camila Remolina Gutiérrez** - [mariacamilarg](https://github.com/mariacamilarg)
* **Rafael Blanco** - [rafaelblanco25](https://github.com/rafaelblanco25)
* **Zujany Salazar** - [zujany](https://github.com/zujany)
