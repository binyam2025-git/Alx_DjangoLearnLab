\### 📝 Social Media API



This project is a social media API built with Django and Django REST Framework. It provides core functionalities for users to register, log in, create posts, and interact with other users through a follow/unfollow system and a personalized content feed.



\#### \*\*Key Features\*\*



\* \*\*User Management:\*\* Register and log in with a custom user model.

\* \*\*Post Management:\*\* Create, retrieve, update, and delete posts.

\* \*\*User Relationships:\*\* Follow and unfollow other users.

\* \*\*Personalized Feed:\*\* View an aggregated feed of posts from all followed users, ordered by recency.



---



\### 🚀 \*\*Getting Started\*\*



\#### \*\*Prerequisites\*\*



\* Python 3.12

\* Django

\* Django REST Framework



\#### \*\*Installation\*\*



1\.  \*\*Clone the repository:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/Alx\_DjangoLearnLab/social\_media\_api.git](https://github.com/Alx\_DjangoLearnLab/social\_media\_api.git)

&nbsp;   cd social\_media\_api

&nbsp;   ```

2\.  \*\*Install dependencies:\*\*

&nbsp;   ```bash

&nbsp;   pip install django djangorestframework

&nbsp;   ```

3\.  \*\*Run migrations:\*\*

&nbsp;   ```bash

&nbsp;   python manage.py makemigrations

&nbsp;   python manage.py migrate

&nbsp;   ```

4\.  \*\*Create a superuser\*\* (optional, for admin access):

&nbsp;   ```bash

&nbsp;   python manage.py createsuperuser

&nbsp;   ```

5\.  \*\*Start the development server:\*\*

&nbsp;   ```bash

&nbsp;   python manage.py runserver

&nbsp;   ```



---



\### ⚙️ \*\*API Endpoints\*\*



All API endpoints are prefixed with `/api/`.



\#### \*\*1. Authentication\*\*



\* \*\*`POST /api/register/`\*\*

&nbsp;   \* \*\*Description:\*\* Creates a new user account.

&nbsp;   \* \*\*Required Data (JSON):\*\* `username`, `email`, `password`.



\* \*\*`POST /api/login/`\*\*

&nbsp;   \* \*\*Description:\*\* Logs in a user and returns a unique authentication token.

&nbsp;   \* \*\*Required Data (JSON):\*\* `username`, `password`.

&nbsp;   \* \*\*Response:\*\* `{"token": "a03640b6bad5f79f76903ae39f60c3fd4ef38068"}`



\#### \*\*2. Posts\*\*



\* \*\*`GET /api/posts/`\*\*

&nbsp;   \* \*\*Description:\*\* Retrieves a list of all posts.

&nbsp;   \* \*\*Permissions:\*\* Read-only for unauthenticated users.



\* \*\*`POST /api/posts/`\*\*

&nbsp;   \* \*\*Description:\*\* Creates a new post.

&nbsp;   \* \*\*Required Headers:\*\* `Authorization: Token <your\_token\_here>`

&nbsp;   \* \*\*Required Data (JSON):\*\* `title`, `content`.



\* \*\*`GET /api/posts/<int:pk>/`\*\*

&nbsp;   \* \*\*Description:\*\* Retrieves details for a single post.



\* \*\*`PUT/PATCH /api/posts/<int:pk>/`\*\*

&nbsp;   \* \*\*Description:\*\* Updates a post.

&nbsp;   \* \*\*Permissions:\*\* `IsAuthenticatedOrReadOnly`. Only the post author can update it.



\* \*\*`DELETE /api/posts/<int:pk>/`\*\*

&nbsp;   \* \*\*Description:\*\* Deletes a post.

&nbsp;   \* \*\*Permissions:\*\* `IsAuthenticatedOrReadOnly`. Only the post author can delete it.



\#### \*\*3. User Follows and Feed\*\*



\* \*\*`POST /api/follow/<int:user\_id>/`\*\*

&nbsp;   \* \*\*Description:\*\* Allows the authenticated user to follow a user with the specified ID.

&nbsp;   \* \*\*Required Headers:\*\* `Authorization: Token <your\_token\_here>`

&nbsp;   \* \*\*Example Request:\*\*

&nbsp;       ```bash

&nbsp;       curl -X POST -H "Authorization: Token <your\_token\_here>" \[http://127.0.0.1:8000/api/follow/1/](http://127.0.0.1:8000/api/follow/1/)

&nbsp;       ```

&nbsp;   \* \*\*Example Response:\*\*

&nbsp;       ```json

&nbsp;       {"detail": "You are now following Alie"}

&nbsp;       ```



\* \*\*`DELETE /api/follow/<int:user\_id>/`\*\*

&nbsp;   \* \*\*Description:\*\* Allows the authenticated user to unfollow a user with the specified ID.

&nbsp;   \* \*\*Required Headers:\*\* `Authorization: Token <your\_token\_here>`

&nbsp;   \* \*\*Example Request:\*\*

&nbsp;       ```bash

&nbsp;       curl -X DELETE -H "Authorization: Token <your\_token\_here>" \[http://127.0.0.1:8000/api/follow/1/](http://127.0.0.1:8000/api/follow/1/)

&nbsp;       ```

&nbsp;   \* \*\*Example Response:\*\*

&nbsp;       ```json

&nbsp;       {"detail": "You have unfollowed Alie"}

&nbsp;       ```



\* \*\*`GET /api/feed/`\*\*

&nbsp;   \* \*\*Description:\*\* Retrieves a personalized feed of posts from users the authenticated user is following.

&nbsp;   \* \*\*Required Headers:\*\* `Authorization: Token <your\_token\_here>`

&nbsp;   \* \*\*Example Request:\*\*

&nbsp;       ```bash

&nbsp;       curl -X GET -H "Authorization: Token <your\_token\_here>" \[http://127.0.0.1:8000/api/feed/](http://127.0.0.1:8000/api/feed/)

&nbsp;       ```

&nbsp;   \* \*\*Example Response:\*\*

&nbsp;       ```json

&nbsp;       \[{"id":2,"author":"Alie","title":"My Newest Post",...}]

&nbsp;       ```

