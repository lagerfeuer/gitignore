import unittest
from giig import *

# define some languages to test for:
EXAMPLE_LIST = ["linux", "python", "c", "java", "intellij", "eclipse"]


class TestStringMethods(unittest.TestCase):

    def test_get_list(self):
        result = giig._get_list()
        for item in EXAMPLE_LIST:
            self.assertIn(item, result)

    def test_search(self):
        result = giig._search("java")
        self.assertEqual(3, len(result))
        result = giig._search("python")
        self.assertEqual(1, len(result))

    def test_gitignore(self):
        result = giig._get_gitignore(["linux", "python"])
        self.assertIn("### Linux ###", result)
        self.assertIn("### Python ###", result)


if __name__ == "__main__":
    unittest.main()
