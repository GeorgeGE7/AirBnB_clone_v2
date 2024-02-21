#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *isadl, **all_isadl):
        """ """
        super().__init__(*isadl, **all_isadl)
        self.name = "Place"
        self.value = Place

    def test_id_of_the_city(self):
        """ """
        the_clss_l = self.value()
        self.assertEqual(type(the_clss_l.city_id), str)

    def test_user_id(self):
        """ """
        the_clss_l = self.value()
        self.assertEqual(type(the_clss_l.user_id), str)

    def test_asm(self):
        """ """
        the_clss_l = self.value()
        self.assertNotEqual(type(the_clss_l.name), int)
        self.assertEqual(type(the_clss_l.name), str)

    def test_info(self):
        """_summary_
        """
        the_clss_l = self.value()
        self.assertEqual(type(the_clss_l.description), str)

    def test_number_rooms(self):
        """ """
        the_clss_l = self.value()
        self.assertNotEqual(type(the_clss_l.number_rooms), str)
        self.assertEqual(type(the_clss_l.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        the_clss_l = self.value()
        self.assertNotEqual(type(the_clss_l.number_bathrooms), str)
        self.assertEqual(type(the_clss_l.number_bathrooms), int)

    def test_the_guts(self):
        """ """
        the_clss_l = self.value()
        self.assertNotEqual(type(the_clss_l.max_guest), str)
        self.assertEqual(type(the_clss_l.max_guest), int)

    def test_ppn(self):
        """ """
        the_clss_l = self.value()
        self.assertNotEqual(type(the_clss_l.price_by_night), float)
        self.assertEqual(type(the_clss_l.price_by_night), int)

    def test_le(self):
        """_summary_
        """
        the_clss_l = self.value()
        self.assertNotEqual(type(the_clss_l.latitude), int)
        self.assertEqual(type(the_clss_l.latitude), float)

    def test_the_ltde(self):
        """_summary_
        """
        the_clss_l = self.value()
        self.assertNotEqual(type(the_clss_l.latitude), str)
        self.assertEqual(type(the_clss_l.latitude), float)

    def test_amenity_ids(self):
        """_summary_
        """
        the_clss_l = self.value()
        self.assertNotEqual(type(the_clss_l.amenity_ids), str)
        self.assertEqual(type(the_clss_l.amenity_ids), list)
