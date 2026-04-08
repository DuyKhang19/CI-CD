import json
import os
import unittest


class TestStringMethods(unittest.TestCase):
    def test_login(self):
        with open("../data/account.json", encoding="utf-8") as file:
            data = json.load(file)
        self.assertEqual(data[0]["password"], "12345")

if __name__=="__main__":
    unittest.main()