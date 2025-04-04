# Harry Potter API
## How to Run the Project
Clone the Repository:
```
git clone https://github.com/your-username/harry-potter-api.git
cd harry-potter-api
```

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

### 3. Start the Django Server
Run the following command to start the development server:
```
python manage.py runserver
```
The server will start at:
```
http://127.0.0.1:8000/
```

### 4. Access the API:
Open your browser or Postman and navigate to:
```
http://127.0.0.1:8000/api/characters/
```

## API Endpoints
### 1. Get All Characters
Retrieve a list of all characters.

URL: /api/characters/

Method: GET

Response: List of all characters.

```
GET http://127.0.0.1:8000/api/characters/
```
Example Response:
```
[
    {
        "id": 51,
        "role": "headmaster",
        "name": "Ron Weasley",
        "wand": "Willow and Unicorn Hair",
        "patronus": "Jack Russell Terrier",
        "house": 20
    },
    {
        "id": 52,
        "role": "student",
        "name": "Ron Weasley",
        "wand": "Willow and Unicorn Hair",
        "patronus": "Jack Russell Terrier",
        "house": 20
    },
    {
        "id": 53,
        "role": "student",
        "name": "Ron Weasley",
        "wand": "Willow and Unicorn Hair",
        "patronus": "Jack Russell Terrier",
        "house": 1
    },
    {
        "id": 54,
        "role": "student",
        "name": "Hermione Granger",
        "wand": "Vine and Dragon Heartstring",
        "patronus": "Otter",
        "house": 1
    }
]
```
### 2. GET a Specific Character
Retrieve details of a specific character by ID.

URL: /api/characters/<id>/

Method: GET

Response: Details of the character.

Example Request:
```
GET http://127.0.0.1:8000/api/characters/53/
```
Example Response:
```
{
    "id": 53,
    "role": "student",
    "name": "Ron Weasley",
    "wand": "Willow and Unicorn Hair",
    "patronus": "Jack Russell Terrier",
    "house": 1
}
```
### 3. Filter Characters
Filter characters by house, role.

URL: /api/characters/?<filter>=<value>

Method: GET

Filters:

house__name: Filter by house name (e.g., Gryffindor).

role: Filter by role (e.g., student, professor).



Example Requests:

Filter by house:

```
GET http://127.0.0.1:8000/api/characters/?house=20
```
Filter by role:
```
GET http://127.0.0.1:8000/api/characters/?role=student
```

### 4. POST a New Character

Add a new character to the directory.

URL: /api/characters/

Method: POST

Body: JSON object with character details.


Example Request:
```
POST http://127.0.0.1:8000/api/characters/
```
Body:
```
{
    "name": "Draco Malfoy",
    "house": 2,
    "role": "student",
    "wand": "Hawthorn and Unicorn Hair",
    "patronus": "None"
}

    
```
### 5. PUT (Update) a Character

Update details of a specific character by ID.

  URL: /api/characters/<id>/
  
  Method: PUT
  
  Body: JSON object with updated character details.
  
  Example Request: 
  
  ```
  PUT http://127.0.0.1:8000/api/characters/51/
  ```
  Body 
  ```
  {
        "role": "Head Auror",
        "name": "Ron Weasley",
        "wand": "Willow and Unicorn Hair",
        "patronus": "Jack Russell Terrier",
        "house": 20
    }
  ```
### 6. DELETE a Character

  Delete a specific character by ID.
  
  URL: /api/characters/<id>/
  
  Method: DELETE
  
  Response: 204 No Content if successful.
  
  Example Request: 
  ```
  DELETE http://127.0.0.1:8000/api/characters/51/
  ```




Let me know if you need any modifications! 

