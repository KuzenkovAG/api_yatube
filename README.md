# Yatube API
Social network with API services. 
It allow:
- Create Posts
- View Posts of other Users

## Tech
- Python 3.9
- Django REST Framework


## Installation (for Windows)
1. Clone repository on your PC
2. Open terminal and install vertual enviroment
```sh
py -3.9 -m venv venv
```
3. Install requirements
```sh
pip install -r requirements.txt
```
4. Make migrations and run server
```sh
python manage.py migrate
python manage.py runserver
```

## ENDPOINTS
| endpoint | methods | description |
| - | - | - |
| api/v1/api-token-auth/ | POST | Send login and password, receive token |
| api/v1/posts/ | GET, POST | Receive posts or create post |
| api/v1/posts/{post_id}/ | GET, PUT, PATCH, DELETE | Receive, update, delete post |
| api/v1/groups/ | GET | Receive groups |
| api/v1/groups/{group_id}/ | GET | Receive group |
| api/v1/posts/{post_id}/comments/ | GET, POST | Receive comments of post, create comment |
| api/v1/posts/{post_id}/comments/{comment_id}/ | GET, PUT, PATCH, DELETE | Receive, update, delete comment |

## Examples
Request
```sh
POST .../api/v1/posts/
{
    "text": "Text of post.",
    "group": 1
} 
```
Response
```sh
{
    "id": 14,
    "text": "Text of post.",
    "author": "anton",
    "image": null,
    "group": 1,
    "pub_date": "2021-06-01T08:47:11.084589Z"
} 
```
