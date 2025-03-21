# Harry Potter API

## Setup the Project

### 1. Install Dependencies
First, install the required dependencies.
```sh
pip install -r requirements.txt
```

### 2. Apply Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 3. Create a Superuser (Optional)
To access the Django admin panel:
```
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### 4. Start the Django Server
Run the following command to start the development server:
```
python manage.py runserver
```
The server will start at:
```
http://127.0.0.1:8000/
```

## API Endpoints
### Get All Characters
```
Method: GET
Endpoint: /api/characters/
Description: Fetch all Harry Potter characters.
```

Let me know if you need any modifications! 

