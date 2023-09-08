import unittest
from pyredai.hello import say_hello


class TestSayHello(unittest.TestCase):
    """
    Test cases for the `say_hello` function.

    This function tests various scenarios of the `say_hello` function to ensure it
    generates the correct greeting message.

    Test Cases:
    1. Test with a regular name (e.g., "Alice").
    2. Test with an empty string as the name.
    3. Test with a name containing numbers and special characters.
    4. Test with a name containing leading and trailing spaces.
    """

    def test_regular_name(self):
        """
        Test with a regular name (e.g., "Alice").
        """
        result = say_hello("Alice")
        self.assertEqual(result, "Hello, Alice")

    def test_empty_name(self):
        """
        Test with an empty string as the name.
        """
        result = say_hello("")
        self.assertEqual(result, "Hello, ")

    def test_name_with_special_characters(self):
        """
        Test with a name containing numbers and special characters.
        """
        result = say_hello("123#@!")
        self.assertEqual(result, "Hello, 123#@!")

    def test_name_with_spaces(self):
        """
        Test with a name containing leading and trailing spaces.
        """
        result = say_hello("   Bob   ")
        self.assertEqual(result, "Hello,    Bob   ")
