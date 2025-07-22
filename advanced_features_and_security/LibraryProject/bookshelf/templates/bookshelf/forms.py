```html
<!DOCTYPE html>
<html>
<head>
    <title>Add Book (Validated)</title>
</head>
<body>
    <h1>Add New Book (with Input Validation)</h1>
    <p>{{ message }}</p>

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }} <button type="submit">Add Book</button>
    </form>

    {% if form.errors %}
        <div style="color: red; border: 1px solid red; padding: 10px; margin-top: 20px;">
            <h3>Form Submission Errors:</h3>
            <ul>
                {% for field, errors in form.errors.items %}
                    {% if field != '__all__' %}
                        <li><strong>{{ field|capfirst }}:</strong> {{ errors|join:", " }}</li>
                    {% endif %}
                {% endfor %}
                {% if form.non_field_errors %}
                    <li><strong>General Errors:</strong> {{ form.non_field_errors|join:", " }}</li>
                {% endif %}
            </ul>
        </div>
    {% endif %}
    <p><a href="{% url 'bookshelf:my_form' %}">Go to Safe Form</a></p>
    <p><a href="{% url 'bookshelf:my_form_unsafe' %}">Go to Unsafe Form</a></p>
    <p><a href="{% url 'bookshelf:xss_demo' %}">Go to XSS Demo</a></p>
</body>
</html>
```
* **Save** `book_form.html`.