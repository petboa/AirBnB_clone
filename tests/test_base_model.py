import unittest
import uuid
from models.base_model import BaseModel

"""
Test Base Model Class
======================

Parent Test Class for all models
"""


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """
        Creates Instances of BaseModel for testing

        Args:
            None

        Returns:
            None
        """
        self.raw_bm = BaseModel("", "", "")
        self.bm_with_timestamp = BaseModel("")
        self.generic_bm = BaseModel()

    def test_base_model_id_has_type_str(self):
        """
        Tests for the correct type for id of BaseModel

        Args:
            None

        Returns:
            None
        """

        self.assertIsInstance(self.raw_bm.id, str)

    def test_base_model_created_at_has_type_str(self):
        """
        Tests for the correct type for created_at of BaseModel

        Args:
            None

        Returns:
            None
        """
        self.assertIsInstance(
            self.bm_with_timestamp.created_at, str)

    def test_base_model_updated_at_has_type_str(self):
        """
        Tests for the correct type for updated_at of BaseModel

        Args:
            None

        Returns:
            None
        """
        self.assertIsInstance(
            self.bm_with_timestamp.updated_at, str)

    def test_base_model_has_valid_uuid(self):
        """
        Tests for the validity of an BaseModel instance's uuid

        Args:
            None

        Returns:
            None
        """
        uuid_obj = uuid.UUID(self.generic_bm.id)
        uuid_str = str(uuid_obj)
        self.assertEqual(uuid_obj.hex, uuid_str.replace('-', ''))
