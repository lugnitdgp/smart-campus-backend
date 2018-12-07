# Smart Campus Backend


## Building from Source

1. Create a **virtual environment** with venv(install venv, if its not installed) in a directory.
    ```
    python3 -m venv django-env

    ```
    If you prefer to use **Pipenv** , then 
    ```
    git clone https://github.com/lugnitdgp/smart-campus-backend.git

    cd smart-campus-backend

    pipenv install

    pipenv shell
    ```
    Now , skip to Step 5 :smile:

2. Clone the project in the same directory.
    ```
    git clone https://github.com/lugnitdgp/smart-campus-backend.git

    ```

3. Activate the virtual environemnt.
    #### For Linux/Mac OSX   
    ```
    source django-env/bin/activate
    ```
    ### For Windows
    `I don't care, find it yourself.`
    
4. Install the requirements.
    ```
    cd smart-campus-backend
    pip install -r requirements.txt

    ```
5.  Copy the `.env.example` file and rename it to `.env`.
    Add/Edit the `.env` file as per your requirement.

6.  Migrate your database and run the Django Development Server.

    ```
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

    ```
7. Open `http://localhost:8000` in your browser.


## Features

### Structure

*   Departmets
    *   Schedule
        *   Active schedule
        *   Default schedule
    *   Courses
        *   Course details
        *   Professor details
        *   Notes
        *   Past year papers
    *   Notifications
        *   Auto
        *   Manual
    *   Students
    
#### Click [here](https://github.com/arc9693/smart-campus-backend/tree/master/wireframes) to view wireframes.
