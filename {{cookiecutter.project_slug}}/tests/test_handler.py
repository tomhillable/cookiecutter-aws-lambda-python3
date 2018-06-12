"""Unit tests for the lambda handlers."""


import unittest
from {{cookiecutter.project_slug}}.lambda_handlers import handler


class HandlerTestCase(unittest.TestCase):

    """Main entrypoint tests."""

    def test_handler(self):
        """Test handler returns True."""
        self.assertEqual(handler(None, None), True)


if __name__ == '__main__':
    unittest.main()
