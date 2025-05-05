# Twitter API

This is a Django-based REST API project that provides functionality for posts, likes, follows, and user registration.

## Setup Instructions

### 1. Clone the Repository
Download the project by cloning the repository:
```bash
git clone https://github.com/diskrat/twitter-api.git
cd twitter-api
```

### 2. Create Virtual Enviroment 
Create and activate a virtual environment to isolate dependencies:

```bash
# On Linux / macOS 
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Setup Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server
```bash
python manage.py runserver
```


## Entity-Relationship Diagram (ERD) 

The overall idea was not running a `count(*)`(the Justin Bieber problem) every time someone runs a `GET /posts/`.
The solution was updating the `like_count` every time someone like/dislike


![db](imgs/db_schema.svg)


## Tech choices
I worked with what was given most of it is new to me 
- Mostly used `django.model` [docs](https://docs.djangoproject.com/en/5.2/topics/db/models/);
- [DRF](https://www.django-rest-framework.org/) Guides and API Reference;
- and the [simplejwt plugin for DRF](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)


## **USE CASES**

### **User Registration**

*   Users should be able to sign up via the API by providing an email, username, and password.
*   Use JWT to handle authentication for login and session management.

### **Post Creation**

*   Authenticated users can create a post with text and one image as content
*   Posts can be **liked** by other users.

### **Follow/Unfollow User**

*   Users should be able to follow or unfollow others.
*   The feed should only show posts from users the authenticated user follows.

### **Viewing Feed**

*   The user can view a paginated list of posts from the users they follow.
*   Posts should be ordered by creation time, from most recent to oldest.


# Next Steps
- Fix DB types mismatch
- Implement the "Only see posts from people I follow" feature
- Tests
- PostgreSQL as DB
- Frontend Using MaterialUI
- package everything in a Docker compose file

# Extras
Used HyperlinkModels to be easy to navigate because some parts are missing for the fully functioning project.

Post only working through context is one of the problems created while I was trying to make it work with minimal work.

Postgres implementation is harder than I thought and I spent too much time trying to understand it.

**This is Hard.**