# User interaction Backend app

## Tural Alakbarov 

## Student number: 39351

## Backend Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.


## Backend local development

* Start the stack with Docker Compose:

```bash
docker-compose up -d
```

**Note**: The first time you start containers, you can see a small warning related to machine architecture type, but the container will be up anyway.

* Now you can open your browser and interact with these URLs:

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): http://localhost:8990/docs

PGAdmin, PostgreSQL web administration: http://localhost:5053

**Note**: The first time you start your stack, it might take a minute for it to be ready. While the backend waits for the database to be ready and configures everything. You can check the logs to monitor it.

To check the backend logs, run:

```bash
docker logs -f backend
```


## Pgadmin

Username:  `newuser@skeleton.com`
Password:  `changethis`

After entering first time you should add a new server:

- Name: `app`
- Host name/ address: `db`
- username: `postgres`
- password: `changethis`

Then openning databases -> app -> schemas -> tables   You can see two tables `alembic_version` and `user`. 
Right clicking on `user` table and pressiong view data, will show all users



### Migrations

As during local development your app directory is mounted as a volume inside the container, you can also run the migrations with `alembic` commands inside the container and the migration code will be in your app directory (instead of being only inside the container). So you can add it to your git repository.

Make sure you create a "revision" of your models and that you "upgrade" your database with that revision every time you change them. As this is what will update the tables in your database. Otherwise, your application will have errors.

* Start an interactive session in the backend container:

```console
$ docker-compose exec backend bash
```

* If you created a new model in `./backend/app/app/models/`, make sure to import it in `./backend/app/app/db/base.py`, that Python module (`base.py`) that imports all the models will be used by Alembic.

* After changing a model (for example, adding a column), inside the container, create a revision, e.g.:

```console
$ alembic revision --autogenerate -m "Add column last_name to User model"
```

* Commit to the git repository the files generated in the alembic directory.

* After creating the revision, run the migration in the database (this is what will actually change the database):

```console
$ alembic upgrade head
```


