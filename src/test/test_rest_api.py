from unittest import TestCase
from unittest.mock import patch
from http_status import *
from app import app

class APITest(TestCase):

  def setUp(self):
    self.client = app.test_client()

  def test_get_request(self):
    """ Test a simple GET request """
    result = self.client.get('/')
    self.assertEqual(result.status_code, HTTP_200_OK)

  def test_post_request(self):
    """ Test a simple POST request """
    result = self.client.post('/')
    self.assertEqual(result.status_code, HTTP_200_OK)

  def test_create_email_template(self):
    """ Test the creation of an email template """
    pass

  def test_handle_name_collisions(self):
    """ Test the email template name collision handling """
    pass

  def test_upload_email_template(self):
    """ Test the /upload API route """
    pass