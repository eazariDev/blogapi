# BlogAPI - Django Blog API

## Description

BlogAPI is a simple, Django-based API designed to manage blog posts. It provides standard CRUD (Create, Read, Update, Delete) functionality for blog posts, with basic user authentication support. The API follows the principles of REST and is built to scale for future features and integrations.

This project is intended to be a foundational backend for any blog platform, enabling developers to quickly set up a working API and easily extend it with additional functionality. It uses Django REST Framework to handle the API endpoints and includes simple user authentication and post management systems.

## Core Features
This project provides a RESTful API for managing blog posts.
- Posts Management: Create, read, update, and delete blog posts.
- User Authentication: Manage user registrations and logins.
- API Endpoints: Accessible endpoints for interacting with blog posts.

## Project Structure
The project's structure is as follows:

```bash
blogapi/
├── accounts/                  # Contains user authentication views and serializers
├── django_project/             # Main Django settings and configurations
├── posts/                      # Contains models, views, and serializers for blog posts
├── .gitignore                  # Git ignore file
├── manage.py                   # Django project management utility
├── requirements.txt            # Python dependencies
```

## Key Techniques Used

1. **Django REST Framework**: The project leverages [Django REST Framework](https://www.django-rest-framework.org/) for building robust APIs in Django. This library simplifies working with serializers and viewsets to handle CRUD operations and create endpoint routing.

2. **Authentication and Permissions**: The project uses Django’s built-in [authentication system](https://docs.djangoproject.com/en/stable/topics/auth/) for user management. It utilizes JWT (JSON Web Tokens) for API token-based authentication, making it ideal for secure, stateless requests.

3. **Model-View-Template (MVT)**: This is the architectural pattern employed by Django, similar to MVC. In this project, it handles the structuring of the application, ensuring proper separation of concerns between database models, views, and templates.

4. **DRF Serializers**: We are using [Django REST Framework serializers](https://www.django-rest-framework.org/api-guide/serializers/) to convert complex data types like querysets and model instances into native Python datatypes. This allows the API to send data in a JSON format.

5. **Django Migrations**: The project uses Django’s migration system for database schema management. Learn more about [migrations here](https://docs.djangoproject.com/en/stable/topics/migrations/).

6. **Class-based Views (CBVs)**: Django's [class-based views](https://docs.djangoproject.com/en/stable/topics/class-based-views/) are utilized for handling API views. This technique helps organize code in a modular, reusable way, allowing developers to easily extend views.

## Setup Instruction
1. Clone the repository:
   ```bash
   git clone https://github.com/eazariDev/blogapi.git
   cd blogapi 
    ```
2. Set Up a Virtual Environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install Dependencies:
   ```bash
   pip install -r requirements.txt 
    ```
4. Apply Migrations:
   ```bash
   python manage.py migrate
    ```
5. Run the Development Server:
   ```bash
   python manage.py runserver
    ```

The API should now be accessible at http://127.0.0.1:8000/.

## Testing the API

You can interact with the API using tools like Postman or Insomnia. Common endpoints might include:

- GET /api/v1/posts/: Retrieve a list of all blog posts.
- POST /api/v1/posts/: Create a new blog post.
- GET /api/v1/posts/{id}/: Retrieve a specific blog post by ID.
- PUT /api/v1/posts/{id}/: Update a specific blog post by ID.
- DELETE /api/v1/posts/{id}/: Delete a specific blog post by ID.

For user authentication, endpoints might include:
- POST /api/v1/register/: Register a new user.
- POST /api/v1/login/: Log in an existing user.

## Contributing
This project serves as a foundational backend for a blogging platform, focusing on API development with Django. It's a great starting point for developers looking to build or extend a blog application.
Feel free to contribute or extend this project to fit your needs.
If you have a problem, it is better to open a issue in the issue tracker at github. Please state the problem clearly, and if possible, provide a document sample to reproduce it.



