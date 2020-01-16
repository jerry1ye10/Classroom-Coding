# Classroom-Coding

## Purpose
This is a personal project of mine that I built to learn Django. The actual description of the project is included in the design document on github; however, this repo is also meant to serve as review for the PennApps development team and to help everyone on the team learn Django. Below, I will cover a big overview of general Django development concepts, link some helpful resources, and comment on parts of my codebase I'd heavily suggest members of the PennApps team to look at. 
## Migrations
Django does a lot of heavy lifting for us. To truly understand how databases work in Django, it's good to think about it on a high level. First of all, to explain, a database can simply be thought of a place to store a lot of information. If we were to store one big string inside a textfile in our directory, that textfile could be called a database. Of course Sqlite(our db) is a little more complicated than that. But similarly, all of our data in django is stored in a file in the core directory. Our database is defined by our models(the classes you write in model.py). When we run '''python manage.py makemigrations''' and '''python manage.py migrate''' we are taking our models, converting them into actual sqlite code (which defines the structure of the database) and running the sqlite code. To learn more about sqlite, feel free to read this: https://www.sqlitetutorial.net/what-is-sqlite/
## User Authentication 
To learn more about creating a user class, please check out this resource: https://wsvincent.com/django-tips-custom-user-model/
## Website Structure
In the django tutorial, all of our urls were defined by 'polls/INSERTSOMETHINGHERE'. In general, we want the home page to simply be '/' and other pages to look like this '/INSERTSOMETHINGHERE'. To do this, in your core/urls.py(the one that isn't a part of the app that you create), simply make sure the path has an empty string(if this is confusing just look at my code base)
