<A name="toc1-0" title="What's this?" />
# What's this?

This is web software for managing the relations between co-operative makers and their equipment and groups.

<A name="toc1-5" title="Dependencies" />
# Dependencies

* all the packages in `requirements.pip`
* nginx (or your own server, if you'd like to use that instead)

<A name="toc1-11" title="Do Setup" />
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

<A name="toc1-33" title="Running" />
# Running

Once the setup is complete, run uwsgi and nginx, like so (you'll need these to stay running, but how you do that is up to you):

<A name="toc2-38" title="uwsgi" />
## uwsgi

While using your virtualenv:

    ./runuwsgi

<A name="toc2-45" title="nginx" />
## nginx

In the code directory:

    ./runnginx
