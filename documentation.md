# Orbit Documentation

## Endpoints

### Auth Token Summerize

| Path | Method | Description | Response Codes |
| ------ | ------ | ------ | ------ |
| /api/token/ | POST | Get fresh token | 200, 404 |


## API DETAILS

#### 1. Get Fresh Token:
Example json data
```json
{
    "username": "default",
    "password": "default"
}
```

Example Curl Request

```sh
curl --location --globoff 'http://127.0.0.1:8000/api/token/' \
--data '{
    "username": "default",
    "password": "default"
}'
```

Example Response's
- 200 Success
    ```json
        {
            "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUz...",
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUz..."
        }
    ```
- 404 Not Found
    ```json
        {
            "detail": "No User matches the given query."
        }
    ```

### Event API's Summerize

| Path | Method | Description | Response Codes |
| ------ | ------ | ------ | ------ |
| /api/v1/events | POST | Creates new event | 201, 400, 401 |
| /api/v1/events | GET | Get List of all events | 200, 401 |
| /api/v1/events/upcomings/ | GET | Get list of events upcoming next 24 hours | 200, 401 |
| /api/v1/events/category/{categoryName} | GET | Get event list by category name | 200, 401 |
| /api/v1/events/{id} | GET | Get an event by id | 200, 401, 404  |
| /api/v1/events/{id} | PUT | Update an existing event | 200, 400, 401 |
| /api/v1/events/{id} | DELETE | Delete an existing event | 204, 401, 404 |

*401 Unauthorized
*200,201.. Success Response
*400 Bad Request

## API DETAILS

#### 1. Create An Event:

 Example Json data
```json
{
    "title": "Sis's birthday",
    "description": "Don't forget to celebrate sisy's birthday",
    "date": "2024-10-11",
    "time": "09:00:00",
    "category_name": "Family"
}
```
Example curl request
```sh
curl --location --request POST 'http://127.0.0.1:8000/api/v1/events/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...' \
--data '{
    "title": "Test From Postman Title",
    "date": "2024-10-12",
    "time": "08:33:10",
    "category_name": "Test",
    "description": "Testimontial"
}'
```
Example Response's

- 200 Success
    ```json
        {
            "id": 5,
            "title": "Sis's birthday",
            "slug": "sis-s-birthday",
            "description": "Don't forget to celebrate sisy's birthday",
            "category": {
                "id": 2,
                "name": "Family",
                "slug": "family"
            }
        }
    ```

- 400 Bad Request
    ```json
        {
            "category_name": [
                "This field is required."
            ]
        }
    ```
- 401 Unauthorized
    ```json
        {
            "detail": "Authentication credentials were not provided."
        }
    ```

#### 2. List of Events:


Example Curl Request
```sh
curl --location 'http://127.0.0.1:8000/api/v1/events' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...'
```
Example Response's

- 200 Success 
    ```json
        [
            {
                "id": 10,
                "title": "Test From Postman Title",
                "slug": "test-from-postman-title",
                "description": "Testimontial",
                "date": "2024-10-12",
                "time": "08:33:10",
                "category": {
                    "id": 2,
                    "name": "Test",
                    "slug": "test"
                }
            }
        ]
    ```

- 401 Unauthorized
    ```json
        {
            "detail": "Authentication credentials were not provided."
        }
    ```

### 3. Get list of events upcoming next 24 hours:

Example Curl Request

```sh
curl --location 'http://127.0.0.1:8000/api/v1/events/upcoming' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...'
```
Example Response's

- 200 Success
    ```json
        [
            {
                "id": 10,
                "title": "Test From Postman Title",
                "slug": "test-from-postman-title",
                "description": "Testimontial",
                "date": "2024-10-12",
                "time": "08:33:10",
                "category": {
                    "id": 2,
                    "name": "Test",
                    "slug": "test"
                }
            }
        ]
    ```
- 401 Unauthorized
    ```json
        {
            "detail": "Authentication credentials were not provided."
        }
    ```

### 4. Get event list by category name:

Example Curl Request

```sh
curl --location 'http://127.0.0.1:8000/api/v1/events/category/Test/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...'
```

Example Response's

- 200 Success
    ```json
        [
            {
                "id": 10,
                "title": "Test From Postman Title",
                "slug": "test-from-postman-title",
                "description": "Testimontial",
                "date": "2024-10-12",
                "time": "08:33:10",
                "category": {
                    "id": 2,
                    "name": "Test",
                    "slug": "test"
                }
            }
        ]
    ```
- 401 Unauthorized
    ```json
        {
            "detail": "Authentication credentials were not provided."
        }
    ```

### 5. Get an event by id:

Example Curl Request

```sh
curl --location 'http://127.0.0.1:8000/api/v1/events/9/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...'
```
Example Response's
- 200 Success
    ```json
    ```

- 404 Not Found
    ```json
        {
            "detail": "No User matches the given query."
        }
    ```

- 401 Unauthorized
    ```json
        {
            "detail": "Authentication credentials were not provided."
        }
    ```

### 6. Update an existing event:

Example Curl Request

```sh
curl --location --request PUT 'http://127.0.0.1:8000/api/v1/events/2/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...' \
--data '{
    "title": "Test From Postman Update",
    "date": "2024-8-14",
    "time": "11:33:10",
    "description": "Lorem ipsum sit dolor amet",
    "category_name": "Healt"
}'
```

Example Response's
- 200 Success
    ```json
        {
            "id": 5,
            "title": "Sis's birthday",
            "slug": "sis-s-birthday",
            "description": "Don't forget to celebrate sisy's birthday",
            "category": {
                "id": 2,
                "name": "Family",
                "slug": "family"
            }
        }
    ```
    
- 404 Not Found
    ```json
        {
            "detail": "No User matches the given query."
        }
    ```

- 401 Unauthorized
    ```json
        {
            "detail": "Authentication credentials were not provided."
        }
    ```

### 7. Delete an existing event

Example Curl Request

```sh
curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/events/1/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsIn...'
```

Example Response's
- 204 Success
    ```json 
        No Content
    ```
    
- 404 Not Found
    ```json
        {
            "detail": "No User matches the given query."
        }
    ```

- 401 Unauthorized
    ```json
        {
            "detail": "Authentication credentials were not provided."
        }
    ```



