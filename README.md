# README

## WARNING

I didn't get all the features in the bookmarks project working but the modules do contain my notes on how things work.

If you want to see a working solution, go to the solution folder ~/projects/django/django2_by_example_solution/bookmarks_final..  I worked through the features there via my browser to check that everything works.

## Code

Code for this book is here:

[Django-2-by-Example](https://github.com/PacktPublishing/Django-2-by-Example)
[Errata](https://github.com/Django-By-Example-ZH/Django-By-Example-ZH/issues/6)

## Start development server

    cd ~/projects/django/django2_by_example/<project>
    workon django2_by_example
    python manage.py runserver

## URLS

[localhost:8000](http://localhost:8000)

## Accounts and passwords

See login_accounts file.

## Edit code

    Use Visual Studio Code to edit code.

## Pip requirements

See requirements-to-freeze.txt.

## Ngrok server

This server is used in the bookmarklet chapter.  It creates a tunnel to expose your localhost to the Internet through both HTTP and HTTPS.

### Install Ngrok

    brew cask install ngrok

### Run Ngrok

    # Keep your Django development server running and start the Ngrok server.
    ngrok http 8000             # Ngrok URL -> https://e6cf301d.ngrok.io

    # Add the forwarding address to your ALLOWED_HOSTS setting.  For example,
    ALLOWED_HOSTS = [
        'mysite.com',
        'localhost',
        '127.0.0.1',
        'e6cf301d.ngrok.io'     # <- New Ngrok domain name
    ]

    # Test it's working by putting this HTTPS URL in your browser:
    https://e6cf301d.ngrok.io/account/login

    # Put the updated Ngrok domain name in the bookmarklet_launcher.js and js/bookmarklet.js files.  See loc. 3232.

## Run apps

    localhost:8000/blog
    localhost:8000/account

## Redis

If you don't start the Redis server, you'll see this error:

    redis.exceptions.ConnectionError: Error 61 connecting to localhost:6379.  Connection refused.

### Install Redis server

    brew install redis

### Run Redis server

    redis-server /usr/local/etc/redis.conf &

### Install Python [bindings](https://redis-py.readthedocs.io/ for Redis

    pip install redis

## Images application

When you view the details for an image, e.g.  http://127.0.0.1:8000/images/detail/6/django-and-duke/, the image created by sorl-thumbnail, sorl thumbnail will create an image of the requested size and copy save a copy of that image in a media/cache subdirectory.
