### REPLIQLimitedExam

------------

First, you have to create a virtual environment of python. There is a file named 'requirements.txt', install all requirements using this code,
> pip install -r requirements.txt

To run the server,

> python manage.py runserver

Goto '/docs/' to see all api documentations.

I use TokenAuthentication where you have a token to header like this
> Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

To get a token you have to register for company to go to "/auth/create/company/".
After register, you have to login using by "/auth/login/",
You will have a token, use that token to your request header and make rest of the authenticate request.