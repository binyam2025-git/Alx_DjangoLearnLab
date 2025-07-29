\# Recipe Management API



\## Description

A RESTful API for managing cooking recipes, including categories, ingredients, cooking instructions, and user-specific ownership. This project serves as a capstone for learning Django and Django REST Framework.



\## Features

\* \*\*Recipe and Category Management (CRUD):\*\* Full Create, Retrieve, Update, and Delete operations for both Recipe and Category models.

\* \*\*User Authentication:\*\* Secure token-based authentication for API access.

\* \*\*Object-Level Permissions:\*\* Users can only edit or delete recipes they own, while all users can view recipes. Categories require authentication for any modification.

\* \*\*Filtering:\*\* Filter recipes by `category` ID and `owner` ID.

\* \*\*Searching:\*\* Perform text-based searches on recipe `title`, `description`, and `ingredients`.

\* \*\*Ordering:\*\* Order lists of recipes by `created\_at` (default), `title`, or `cooking\_time\_minutes`.



\## Setup/Installation



\### Prerequisites

\* Python 3.7+

\* pip (Python package installer)



\### Steps

1\.  \*\*Clone the repository:\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/binyam2025-git/Alx\_DjangoLearnLab.git](https://github.com/binyam2025-git/Alx\_DjangoLearnLab.git)

&nbsp;   ```

2\.  \*\*Navigate to the project directory:\*\*

&nbsp;   ```bash

&nbsp;   cd Alx\_DjangoLearnLab

&nbsp;   ```

3\.  \*\*Create and activate a virtual environment:\*\*

&nbsp;   ```bash

&nbsp;   python -m venv venv

&nbsp;   # On Windows:

&nbsp;   .\\venv\\Scripts\\activate

&nbsp;   # On Linux/macOS:

&nbsp;   # source venv/bin/activate

&nbsp;   ```

4\.  \*\*Install dependencies:\*\*

&nbsp;   ```bash

&nbsp;   pip install Django djangorestframework django-filter # Or pip install -r requirements.txt if you have one

&nbsp;   ```

5\.  \*\*Apply database migrations:\*\*

&nbsp;   ```bash

&nbsp;   python manage.py migrate

&nbsp;   ```

6\.  \*\*Create a superuser\*\* (for admin access and initial API testing):

&nbsp;   ```bash

&nbsp;   python manage.py createsuperuser

&nbsp;   ```

7\.  \*\*Run the development server:\*\*

&nbsp;   ```bash

&nbsp;   python manage.py runserver

&nbsp;   ```

&nbsp;   The API will be accessible at `http://127.0.0.1:8000/api/` and the Django Admin at `http://127.0.0.1:8000/admin/`.



\## API Endpoints



All API endpoints are prefixed with `/api/`.



\### Categories

\* `GET /api/categories/`: List all categories.

\* `GET /api/categories/<id>/`: Retrieve a specific category by ID.

\* `POST /api/categories/`: Create a new category. \*\*(Authentication Required)\*\*

\* `PUT /api/categories/<id>/`: Update a category by ID. \*\*(Authentication Required)\*\*

\* `PATCH /api/categories/<id>/`: Partially update a category by ID. \*\*(Authentication Required)\*\*

\* `DELETE /api/categories/<id>/`: Delete a category by ID. \*\*(Authentication Required)\*\*



\### Recipes

\* `GET /api/recipes/`: List all recipes.

\* `GET /api/recipes/<id>/`: Retrieve a specific recipe by ID.

\* `POST /api/recipes/`: Create a new recipe. \*\*(Authentication Required)\*\* (Owner is automatically set to the authenticated user).

\* `PUT /api/recipes/<id>/`: Update a recipe by ID. \*\*(Owner Permission Required)\*\*

\* `PATCH /api/recipes/<id>/`: Partially update a recipe by ID. \*\*(Owner Permission Required)\*\*

\* `DELETE /api/recipes/<id>/`: Delete a recipe by ID. \*\*(Owner Permission Required)\*\*



\## Authentication



The API uses token-based authentication.



1\.  \*\*Obtain a token:\*\*

&nbsp;   Send a POST request to `/api-token-auth/` with your username and password:

&nbsp;   ```bash

&nbsp;   curl -X POST -H "Content-Type: application/json" -d '{"username":"your\_username", "password":"your\_password"}' \[http://127.0.0.1:8000/api-token-auth/](http://127.0.0.1:8000/api-token-auth/)

&nbsp;   ```

&nbsp;   You will receive a token in the response: `{"token":"YOUR\_ACTUAL\_TOKEN\_STRING\_HERE"}`.



2\.  \*\*Use the token:\*\*

&nbsp;   Include the token in the `Authorization` header of your subsequent API requests:

&nbsp;   ```

&nbsp;   Authorization: Token YOUR\_ACTUAL\_TOKEN\_STRING\_HERE

&nbsp;   ```

&nbsp;   Example for creating a recipe:

&nbsp;   ```bash

&nbsp;   curl -X POST -H "Content-Type: application/json" -H "Authorization: Token YOUR\_ACTUAL\_TOKEN\_STRING\_HERE" -d '{"title":"Spicy Chicken","description":"Quick and tasty","ingredients":"Chicken, Chili, Garlic","cooking\_time\_minutes":30,"category":1}' \[http://127.0.0.1:8000/api/recipes/](http://127.0.0.1:8000/api/recipes/)

&nbsp;   ```



\## Filtering, Searching, Ordering Examples



You can combine these parameters in your GET requests to `/api/recipes/`.



\* \*\*Filter by Category:\*\*

&nbsp;   `GET /api/recipes/?category=1` (where `1` is the category ID)

\* \*\*Filter by Owner:\*\*

&nbsp;   `GET /api/recipes/?owner=1` (where `1` is the owner's user ID)

\* \*\*Search by Text:\*\*

&nbsp;   `GET /api/recipes/?search=chicken` (searches title, description, ingredients)

\* \*\*Order by Title (Ascending):\*\*

&nbsp;   `GET /api/recipes/?ordering=title`

\* \*\*Order by Cooking Time (Descending):\*\*

&nbsp;   `GET /api/recipes/?ordering=-cooking\_time\_minutes`



\## Contact/Author

\[Binyam Assefa](https://github.com/binyam2025-git)



\## License

\[MIT License](https://opensource.org/licenses/MIT)

