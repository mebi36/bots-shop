# bots-shop
Welcome to the backend of the Bots Shop.

## Initial Setup


# To begin, clone the repository

```
git clone https://github.com/mebi36/bots-shop
```


# Set up your python virtual environment
```
virtualenv env
```

Navigate into the bots-shop directory

# Install the requirements.txt file
```
pip install -r requirements.txt
```
# Make and apply migrations 
Make the migrations:
```
python manage.py makemigrations
```
Apply the migrations:
```
python manage.py migrate
```

# You can use the demo data provided to populate the db
First, start the django shell provided by manage.py:
```
python manage.py shell
```
Then import the method for installing the fixtures:

```
>>>from fixture.installfixtures import install_fixtures
```
Run the method:
```
>>>install_fixtures()
```
Exit:
```
>>>quit()
```

### You can now start a localserver and navigate the browsable api
```
python manage.py runserver localhost:8000
```

You can navigate the browsable api: http://localhost:8000/api/v1/product/all/

To login:
    If you installed the fixtures provided above, you can use: 
    username: overlord
    password: overlord101

urls:
    api/v1/product/all/
    api/v1/client/<int:pk>/
    api/v1/client/create/
    api/v1/order/history/
    api/v1/

