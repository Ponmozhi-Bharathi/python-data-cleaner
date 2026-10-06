import unittest

from validators import is_valid_email, is_valid_phone


class TestEmailValidator(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(
            is_valid_email("john@gmail.com")
        )

    def test_invalid_email_without_domain(self):
        self.assertFalse(
            is_valid_email("john@gmail")
        )

    def test_invalid_email_without_at_symbol(self):
        self.assertFalse(
            is_valid_email("john.com")
        )


class TestPhoneValidator(unittest.TestCase):

    def test_valid_phone(self):
        self.assertTrue(
            is_valid_phone("9876543210")
        )

    def test_invalid_phone_starting_with_one(self):
        self.assertFalse(
            is_valid_phone("1234567890")
        )

    def test_invalid_short_phone(self):
        self.assertFalse(
            is_valid_phone("987654321")
        )


if __name__ == "__main__":
    unittest.main()