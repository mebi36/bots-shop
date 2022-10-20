"""
# This is bots-shop
Welcome to the backend of the Bots Shop.

# Initial Setup


#### To begin, clone the repository

```
git clone https://github.com/mebi36/bots-shop
```


#### Set up your python virtual environment
```
virtualenv env
```
For Unix-based OS's

Activate the virtual environment:
```
source env/bin/activate
```

#### Install the requirements.txt file
Navigate into the bots-shop directory
```
cd bots-shop/
```

Install project dependencies:
```
pip install -r requirements.txt
```
#### Make and apply migrations 
Navigate to folder containing project's manage.py file
```
cd botsshop
```
Make the migrations:
```
python manage.py makemigrations client order product
```
Apply the migrations:
```
python manage.py migrate
```

#### You can use the demo data provided to populate the db
First, start the django shell provided by manage.py:
```
python manage.py shell
```
Then import the method for installing the fixtures:

```
>from fixture.installfixtures import install_fixtures
```
Run the method:
```
>install_fixtures()
```
Exit:
```
>quit()
```

#### You can now start a localserver and navigate the browsable api
```
python manage.py runserver localhost:8000
```

You can navigate the browsable api: http://localhost:8000/api/v1/product/all/

To login:
    If you installed the fixtures provided above, you can use: <br />
        username: overlord  <br />
        password: overlord101  <br />
        pk: 1 <br />

other urls:
http://localhost:8000/api/v1/product/all/  <br />
http://localhost:8000/api/v1/client/<int:pk>/  <br />
http://localhost:8000/api/v1/client/create/  <br />
http://localhost:8000/api/v1/order/history/  <br />

## To run project-wide unit tests:
```
python manage.py test
```

## To view auto-generated documentation:
Navigate to the folder of interest and open it's index.html file in a browser
"""