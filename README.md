# Demo for django-q - issue 434

This demo project is to help debugging [issue #434](https://github.com/Koed00/django-q/issues/434)

The app contains only the minimum required to reproduce the error.

You must have Docker installed to run a disposable Postgres server.

## Steps

Here are the steps to follow to reproduce the error.

1. Check the source code, to ensure that the app won't do anything you judge inapropriate.

2. Install dependencies: `pip install -r requirements.txt`
2. Run the script `./setup-database.sh`

    You will have a Postgres 11 server listening on port 15432, with the databases needed for the app to run.

3. Run migrations: `./app/manage.py migrate` and `./app/manage.py migrate --database=django_q`

4. Run the debug webserver: `./app/manage.py runserver`

5. In another terminal window, run a `qluster`: `./app/manage.py qcluster`

    **Check the logs in this terminal, this is where the error will pop up.**

6. Open a browser a go to `http://localhost:8000/schedule-task`

Wait for a few seconds, and you should see the error in the `qcluster` process logs.
