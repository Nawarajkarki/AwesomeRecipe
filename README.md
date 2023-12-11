<h1> Recipe Sharing Website</h1>

# Welcome to the **Recipe Sharing Website** Project

A platform where users can discover, share, and explore delicious recipes from around the world. This web application is built using Django, a high-level Python web framework, to provide a seamless experience for users to register, log in, and post their favorite recipes.

## Technologies used

- **Framework:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite

<h2>Features</h2>

  ## User Registration and Login:
  #### Users can create an account on the website by registering with their email and password. Once registered, they can log in to access their account and start sharing recipes.

  ##  Recipe Posting:
  #### Registered users can post their own recipes, including a title, description, ingredients, preparation instructions, and an optional image. This allows them to showcase their culinary creations and share them with the community.

<h2>Getting Started</h2>

Follow these steps to set up the Recipe Sharing Website on your local machine:

##  Clone the Repository:
#### Start by cloning this repository to your local machine using the following command:<br>
<br>

```
git clone https://github.com/Nawarajkarki/AwesomeRecipe.git
```

## Create Virtual Environment:
#### Navigate to the project directory and create a virtual environment:<br>
<br>

```shell
cd AwesomeRecipe
python -m venv venv
```


## Activate the Virtual Environment:
#### On Windows
    venv\Scripts\activate

#### On macOS and Linux:
    source venv/bin/activate


## Install Dependencies:
#### Install the required dependencies using pip:
    pip install -r requirements.txt

## Database Migration:
#### Apply the initial database migrations:
    python manage.py migrate

## Create Superuser:
#### Create a superuser account to access the Django admin interface:
    python manage.py createsuperuser

## Run the Development Server:
#### Start the development server:
    python manage.py runserver



## Access the Website:
#### Open your web browser and navigate to http://127.0.0.1:8000/  OR ([localhost:8000]) to access the Recipe Sharing Website.

<h2>Contribute</h2>

If you'd like to contribute to the development of this project, feel free to fork the repository and submit pull requests with your enhancements.
