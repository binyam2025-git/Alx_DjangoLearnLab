\# ALX Django Library Project

\# LibraryProject: Advanced Features and Security



This project demonstrates advanced Django features, including:



\## Custom User Model

A custom user model (`CustomUser` in `bookshelf/models.py`) is implemented to extend default user functionalities with fields like `date\_of\_birth` and `profile\_photo`.



\## Permissions and Groups

Access control is managed using Django's built-in permissions and groups.



\### Custom Permissions

Custom permissions are defined on the `Book` model in `bookshelf/models.py`:

\- `can\_view`: Allows viewing of book data.

\- `can\_create`: Allows creating new books.

\- `can\_edit`: Allows editing existing books.

\- `can\_delete`: Allows deleting books.



\### User Groups

The following groups are configured in the Django admin:

\- \*\*Admins:\*\* Have all `can\_view`, `can\_create`, `can\_edit`, `can\_delete` permissions for books (and typically other admin privileges).

\- \*\*Editors:\*\* Have `can\_view`, `can\_create`, and `can\_edit` permissions for books.

\- \*\*Viewers:\*\* Have `can\_view` permission for books.



\### Permission Enforcement in Views

Views in `relationship\_app/views.py` (e.g., `book\_add\_view`, `book\_edit\_view`, `book\_delete\_view`, `list\_books`) use the `@permission\_required` decorator to enforce these access controls. For example:

\- `@permission\_required('bookshelf.can\_create', raise\_exception=True)` protects the book creation view.



\## Setup Instructions (for local development)



1\.  \*\*Clone the repository:\*\*

&nbsp;   `git clone https://github.com/your-username/Alx\_DjangoLearnLab.git`

2\.  \*\*Navigate to the project directory:\*\*

&nbsp;   `cd Alx\_DjangoLearnLab/advanced\_features\_and\_security/LibraryProject`

3\.  \*\*Create a virtual environment (optional but recommended):\*\*

&nbsp;   `python -m venv venv`

&nbsp;   `source venv/Scripts/activate` (Windows PowerShell) or `source venv/bin/activate` (Linux/Git Bash)

4\.  \*\*Install dependencies:\*\*

&nbsp;   `pip install Django` (and any other dependencies)

5\.  \*\*Apply migrations (after model changes):\*\*

&nbsp;   `python manage.py makemigrations`

&nbsp;   `python manage.py migrate`

6\.  \*\*Create a superuser:\*\*

&nbsp;   `python manage.py createsuperuser`

7\.  \*\*Run the development server:\*\*

&nbsp;   `python manage.py runserver`

8\.  \*\*Configure Groups and Users:\*\* Access the Django admin (`/admin/`), log in as superuser, create the "Admins", "Editors", and "Viewers" groups, and assign the relevant `bookshelf | book` permissions. Create test users and assign them to these groups to test permissions.

