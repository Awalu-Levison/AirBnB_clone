#!/usr/bin/python3
"""Test file for task 3"""
import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    """Test class constructor of basemodel"""
    def test_init(self):
        model1 = BaseModel()

        self.assertIsNotNone(model1.id)
        self.assertIsNotNone(model1.ctreated_at)
        self.assertIsNotNone(model1.updated_at)

    def test_save(self):
        my_model = BaseModel

        first_updated_at = model1.updated_at
        current_updated_at = model1.save()
        self.assertNotEqual(first_updated_at, current_updated_at)

    def test_to_dict(self):
        model1 = BaseModel()

        my_dict = model1.to_dict()
        self.assertIsInstance(my_dict, dict)

        self.assertEqual(my_dict["__class__"], 'BaseModel')
        self.assertEqual(my_dict['id'], model1.id)
        self.assertEqual(my_dict["created_at"], model1.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], model1.created_at.isoformat())

    def test_str(self):
        model1 = BaseModel()
        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(str(model1.__dict__), str(model1))


if __name__ == "__main__":
    unittest.main()
