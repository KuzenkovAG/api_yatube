# API for Yatube v.0.1.0
API services for [Yatube project]
## Features
- View posts, groups;
- Create or Update own posts;
- Create comments for posts.

## Tech
- Python 3.9
- Django
- rest_framework

## History
- v.0.1.0 [API_Yatube] <- you are here


## Installation (for Windows)
Clone repository
```sh
git clone git@github.com:KuzenkovAG/api_yatube.git
```
Install environment
```sh
python -m venv venv
```
Activate environment
```sh
source venv/Scripts/activate
```
Install requirements
```sh
pip install -r requirements.txt
```
Make migrate
```sh
python yatube_api/manage.py migrate
```
Run server
```sh
python yatube_api/manage.py runserver
```

## Available endpoints
| endpoint | methods | description |
| - | - | - |
| api/v1/api-token-auth/ | POST | Send login and password, receive token |
| api/v1/posts/ | GET, POST | Receive posts or create post |
| api/v1/posts/{post_id}/ | GET, PUT, PATCH, DELETE | Receive, update, delete post |
| api/v1/groups/ | GET | Receive groups list |
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


   [Yatube project]: <https://github.com/KuzenkovAG/yatube_new_feature>
   [API_Yatube]: <https://github.com/KuzenkovAG/api_yatube>