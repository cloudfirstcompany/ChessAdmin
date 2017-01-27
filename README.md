# club-suite

## Getting started with development
### Setting up dependencies
We'll use python3 exclusively in this project.
```
$ sudo apt-get install python3 python3-pip
$ sudo pip3 install virtualenv
```
First, set up a virtualenv,
```
$ cd [code-folder]/
$ virtualenv cse-env
$ cd cse-env
$ source bin/activate
$ git clone git@github.com:fsxfreak/club-suite.git
$ cd club-suite
$ pip install -r requirements.txt
```

### Other required setup
django requires a ```SECRET = ``` parameter in settings.py. But, we
can't distribute the secret key freely on github, so instead we generate
our own.
```
$ cd clubsuite/clubsuite
$ vim settings_secret.py
```
Generate a key from this 
[generator](http://www.miniwebtool.com/django-secret-key-generator/)
and fill ```SECRET = [key]``` in ```settings_secret.py```.
