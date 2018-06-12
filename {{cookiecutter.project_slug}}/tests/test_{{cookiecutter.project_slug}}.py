"""Unit tests for {{cookiecutter.project_camel_slug}}"""


import unittest
import {{cookiecutter.project_slug}}


class {{cookiecutter.project_camel_slug}}TestCase(unittest.TestCase):

    """Unit tests for {{cookiecutter.project_camel_slug}}"""

    def setUp(self):
        self.{{cookiecutter.project_slug}} = {{cookiecutter.project_slug}}.{{cookiecutter.project_camel_slug}}()

    def test_func1(self):
        """Test func1() returns None"""
        self.assertIsNone(self.{{cookiecutter.project_slug}}.func1())


if __name__ == '__main__':
    unittest.main()
