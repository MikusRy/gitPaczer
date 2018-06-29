# Django Git Repository Paczer

<div align="center">

![Logo](http://s1g.wgrane.pl/video/2014/11/23/291592.jpg?st=sjkpZWgyC9JtJKdtI6qcxg&e=1530278160)

</div>

## Description

Project is a simple REST service retrieving data about given GitHub Repository.

## Installation Process

Before Service will be ready to use we need to set few things up.

#### Python 3 / Pip3 / Django 2
Service is implemented in Python 3 therefore you have to be sure it is installed on your machine before running.

Please follow these steps:

If your Linux destro works with .deb packages run:
    
    # apt install python3 python3-pip
    # pip3 install Django requests 
    
Otherwise follow instructions given in this link:

[https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7)

#### Running Application

Before first run you have to provide your GitHub credentials in `settings.py` file located in `gitPaczer/` catalog,
at the very bottom of file in `GitHub_credentials` dictionary, in order to authorize your requests to GitHub service. 

If you want to avoid authorization, please delete `auth` list from `requests.get()` function located in `paczerAPI/views.py`


After these steps we are ready to run our service. Simply change your directory to manage.py file location and type:
    
    $ python3 manage.py runserver:<PORT> <- changing port is optional, default port is 8000
    
    Request URI - http://<servername:port>/repositories/<GitHub_Username>/<Repository_name>

#### MIGRATIONS ARE UNNECESSARY SINCE SERVICE IS NOT USING DATABASES

