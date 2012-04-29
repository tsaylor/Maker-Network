# What's this?

This is web software for managing the relations between co-operative makers and their equipment and groups.

# Dependencies

* all the packages in `requirements.pip`
* nginx (or your own server, if you'd like to use that instead)

# Do Setup

Set up virtualenv using `requirements.pip`:


    virtualenv ~/virtualenv_directory_wherever
    source ~/virtualenv_directory_wherever/bin/activate
    pip install -r requirements.pip

* set up local_settings.py based on local_settings.py.example
* configure some options... (see -h for what they are ahead of time, if you like)

Like so:

    ./configure


If that's not OK, use ./configure -h to determine what you need to do to change things.  It's suggested to run with `-d` (working directory) set to something other than the current directory, to avoid cluttering the code dir.  Next, configure the config files for nginx and the script for running uwsgi:

    make

# Running

Once the setup is complete, run uwsgi and nginx, like so (you'll need these to stay running, but how you do that is up to you):

## uwsgi

While using your virtualenv:

    ./runuwsgi

## nginx

In the code directory:

    ./runnginx
