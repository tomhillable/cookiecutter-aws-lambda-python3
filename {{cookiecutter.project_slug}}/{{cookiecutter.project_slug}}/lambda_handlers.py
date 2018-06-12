"""AWS Lambda function handlers."""


from {{cookiecutter.project_slug}} import {{cookiecutter.project_camel_slug}}


def handler(event: dict, context: dict) -> bool:
    """Receive request from AWS Lambda."""
    print(event, context)
    {{cookiecutter.project_camel_slug}}().func1()
    return True


if __name__ == '__main__':
    handler({}, {})
