import unittest

from contact_manager import save_contacts,load_contacts

# class TestSaveContacts(unittest.TestCase):
#     def test_save_and_load(self):
#         test_data={'曾国藩':'432121'}
#         save_contacts(test_data)
#         result=load_contacts()
#         self.assertEqual(result,test_data)

class TestSaveContacts():
    def test_save_and_load(self):
        test_data={'曾国藩':'432121'}
        save_contacts(test_data)
        assert load_contacts() == test_data

if __name__=='__main__':
    unittest.main()