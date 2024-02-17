#!/usr/bin/python3
"""
Unit tests to check capturing of stdout for console
into a StringIO object using Mock module from python
standard library
"""

import re
import os
import sys
import unittest
import datetime
from io import StringIO
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from console import HBNBCommand
from models.base_model import BaseModel
from unittest.mock import patch
from models.engine.file_storage import FileStorage


class Test_Console(unittest.TestCase):
    """The console model unittest"""


    def setUp(self):
        """Stdin and stdout redirection
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err = ["** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    ]

        self.clss = ["BaseModel",
                     "User",
                     "City",
                     "Place",
                     "Review",
                     "Amenity"]
    """
        print("Testing the Console")

    def test_helpCreate(self):
        """Test for the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        cs = 'Handles creation of new @cls_name class instances\n'\
                  '        and prints the new ID instances\n        \n'
        self.assertEqual(cs, f.getvalue())

    def outTest(self, fnct, arg, exp):
        """Test some console commands"""
        std_out = StringIO()
        sys.stdout = std_out
        fnct(arg)
        output = std_out.getvalue()
        self.assertEqual(output, exp + '\n')
        return output

    def test_helpQuit(self):
        """Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        cs = "The 'quit' command handler\n"
        self.assertEqual(cs, f.getvalue())

    def test_helpClear(self):
        """Default test"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help clear")
            cs = 'Clears screen\n'
            self.assertEqual(cs, f.getvalue())

    def test_help_create(self):
        """Tests the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        cs = 'Handles creation of new @cls_name class instances\n'\
            '        and prints the new ID instances\n        \n'
        self.assertEqual(cs, f.getvalue())

    def test_helpShow(self):
        """Test for do show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            cs = 'To print an instance string representation\n'
            self.assertEqual(cs, f.getvalue())

    def test_help_destroy(self):
        """Tests destroy"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            s = 'Deletes an instance based on the class name and id\n'
            self.assertEqual(s, f.getvalue())



if __name__ == '__main__':
    unittest.main()
