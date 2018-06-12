# {{ cookiecutter.project_name }}

## Local testing

Run step 1.

```docker-compose build```

Now to run the tests defined in tests/

```commandline
docker-compose run tests
```

To run python

```commandline
docker-compose run python
```

To run the linter

```commandline
docker-compose run lint
```
