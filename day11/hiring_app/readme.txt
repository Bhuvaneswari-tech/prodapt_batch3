To create the virtual environment

python -m venv venv


To active the virtual environment

venv\Scripts\activate

To run the requirements.txt

pip install -r requirements.txt

to check the pip
pip list

To run the application

uvicorn app.main:app --reload

uvicorn

Starts the server.

app.main

app → folder name
main → Python file

--reload -> Automatically restarts the server whenever you save changes


URL - Check the swagger

http://127.0.0.1:8000/docs