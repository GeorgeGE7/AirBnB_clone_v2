#!/usr/bin/python3
"""Test unit - test cases for the console module
"""
import unittest
import os
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """_summary_

    isadl:
        unittest (_type_): _description_
    """

    def setUpClass(test_t_cls_c):
        """setting up the class

        isadl:
            test_t_cls_c (Class): The class
        """
        try:
            os.rename("file.json", "ephe")
        except IOError:
            pass
        except Exception:
            pass
        test_t_cls_c.HBNB = HBNBCommand()

    def tearDownClass(test_t_cls_c):
        """_summary_

        isadl:
            test_t_cls_c (_type_): _description_
        """
        try:
            os.rename("ephe", "file.json")
        except IOError:
            pass
        del test_t_cls_c.HBNB

    def setUp(self):
        """Reset FileStorage objects dictionary."""
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Delete any created file.json."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        except Exception:
            pass

    def test_the_create_invalied(self):
        """Testing the create
        """
        with patch("sys.stdout", new=StringIO()) as new_f:
            self.HBNB.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", new_f.getvalue())
        with patch("sys.stdout", new=StringIO()) as new_f:
            self.HBNB.onecmd("create awtip")
            self.assertEqual(
                "** class doesn't exist **\n", new_f.getvalue())

    def test_create_command_validity(self):
        """Test create command."""
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create BaseModel")
            bm = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create User")
            us = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create State")
            st = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Place")
            pl = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create City")
            ct = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Review")
            rv = f.getvalue().strip()

        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("create Amenity")
            am = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all BaseModel")
            self.assertIn(bm, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all User")
            self.assertIn(us, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all State")
            self.assertIn(st, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all Place")
            self.assertIn(pl, f.getvalue())
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all City")
            self.assertIn(ct, f.getvalue())

    def test_create_command_with_all_isadl(self):
        """Test create command with all_isadl."""
        with patch("sys.stdout", new=StringIO()) as f:
            cr_usr = (f'create User name="Ahmed"')
            self.HBNB.onecmd(cr_usr)
            usrr = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("all User")
            mokhrag = f.getvalue()
            self.assertIn(usrr, mokhrag)
            self.assertIn("'name': 'Ahmed'", mokhrag)


if __name__ == "__main__":
    unittest.main()
