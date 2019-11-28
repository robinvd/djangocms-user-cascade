from django.test import TestCase
from django.contrib.auth import get_user_model

class UserDeleteTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user('a', 'b', 'pass')
        self.client.login(username='a', password='pass')

    def test_all_delete(self):
        response = self.client.post('/create_user/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(get_user_model().objects.count(), 2)
        self.user.delete()
        self.assertEqual(get_user_model().objects.count(), 1)
