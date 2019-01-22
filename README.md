# Worklist Tool
The Worklist Tool is a tool for creating lists of Wikimedia pages which users can then assign themselves to for claiming and tracking work during editing events and programs.

The tool was first developed with Wikimedia during Google Summer of Code 2018.

## Usage
The Worklist Tool is hosted on Toolforge at https://tools.wmflabs.org/worklist-tool/.

Currently, the easiest way to create a Worklist is to first create a PetScan (https://petscan.wmflabs.org/) query. PetScan allows you to easily create complex lists of Wikimedia pages, such as all pages from multiple categories, or that contain particular templates, or link to specific other pages. These lists can then be imported directly into the Worklist tool.

To create a new worklist:

* Login via OAuth
* Click the Create Worklist button
* Fill out the Name and Description fields (you can leave Tags blank)
    * Description - this should be an overview of the purpose of this worklist. What kinds of articles does it include? Will it be worked on by a particular group of editors, or at a particular event?
    * Tags - These are descriptive terms for this worklist, to aid in searching.
* Enter either a PetScan Query ID or individual articles to get your list started.
* Click Submit

You can now navigate to 'See Worklists' > 'See My Worklists' in the top bar to see a list of your created worklists.

Opening a worklist will show a list of articles contained in that worklist, and allows users to claim each page. More articles can be added with the 'Add articles' button.

## Future
The vision for this tool is that it will be able to integrate with other tools, such as Citation Hunt (https://meta.wikimedia.org/wiki/Citation_Hunt). This would allow program and event organisers to create worklists of articles, assign users to them, and then import the worklist to other tools to support participants' work.

## Setup
If you want to contribute to Worklist tool follow the below given steps to set it up on your local machine.

#### Cloning repository - 
```
$ git clone https://github.com/MeghaSharma21/WorklistTool-GSoC-2018.git
$ cd WorklistTool-GSoC-2018
```

#### Setting up virtual env -
[virtualenv](https://pypi.python.org/pypi/virtualenv) will help in keeping the dependencies required for this tool local to it's virtualenv only. It'll prevent version collisions of dependencies among projects. For installing virtualenv and python3 refer to [this](https://gist.github.com/pandafulmanda/730a9355e088a9970b18275cb9eadef3) setup guide.
```
$ virtualenv venv
$ source venv/bin/activate
```

#### Installing dependencies -
Dependencies are managed via a `requirements.txt` file:
```
$ pip install -r requirements.txt
```

#### Registering consumer for OAuth -
Worklist tool uses Mediawiki OAuth to authenticate the users. For setting it up for your local workspace you need to register a consumer using a form available [here](https://www.mediawiki.org/wiki/OAuth/For_Developers#Registration). For details on how this is incorporated in a Django project please read through [this](https://wikitech.wikimedia.org/wiki/Help:Toolforge/My_first_Django_OAuth_tool#Local_development_and_testing).


#### Modifying wsgi.py
Place the OAuth keys and callback URL in the placeholders based on the wiki mentioned above. Put in the secret key also.


#### Using settings-development.py
settings-development.py contains settings required while setting the project on local machine for development purposes.Rename settings-development.py to settings.py. 


#### Database setup
Sqlite is the default database engine for Django. But in worklist tool Mysql is used. Since Django is agnostic of the database you can set either of them.
* Option 1: MySql - You can set it up using this [tutorial](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database#step-3-%E2%80%94-install-mysql-database-connector). Modify the database.cnf by putting in your database name, username and password. Hostname will be localhost. Also, create a database in MySql of the same name as mentioned in database.cnf.
* Option 2: Sqlite - For this you need to modify DATABASES section in settings.py in [this](https://gist.github.com/drivard/3417970) way.

### Final Steps!
You're almost done, yaya! Just run these commands -
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 127.0.0.1:8000
```
