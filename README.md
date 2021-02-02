# DjangoApi
Simple API based on existent data source as a JSON file (Django + Xampp + MySQL) with sensitivity on validation the passed parameters with request

Developed a simple API by using a data sample from here : https://github.com/jdorfman/awesome-jsondatasets#tv-shows
Developing process:
1- Made python environment https://docs.djangoproject.com/en/3.1/howto/windows/
2- Created django ptoject https://docs.djangoproject.com/en/3.1/howto/windows/
3- Made Django Sync and work with localhost and MySQL phpmyadmin 
	https://medium.com/@sostomc011/https-medium-com-sostomc011-getting-started-with-django-mysql-and-react-js-backend-b962a7691486
	https://bezkoder.com/django-crud-mysql-rest-framework/
4- Converted json to MySQL file and import it to our db
6- Developed the Django side

To run and test this api, you need to:
1- Clone this repository
2- Installing Xampp or any similar program
3- Lunching MySQL on your localhost(with Xampp) and then import the Database.sql file provided in this repository (CompleteDB.sql)
4- Running the Django server by using command: python manage.py runserver
5- Ready to use different API

Three api provided which can be extended:
1-localhost:8000/episodes/count?getseason=3&format=json (return the full list of episodes of the passed season number)
2-localhost:8000/episodes/count?season=1&format=json (return the total number of episodes of the passed season number)
2-localhost:8000/episodes/title?season=1&episode=1&format=json (return the name of the requested episode, based on the season and episode number)

Here are the output of the api in different situation:
