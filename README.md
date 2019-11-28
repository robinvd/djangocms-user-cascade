
# a POC app showing a possible issue in django-cms

## showing the issue
requires python3 with django and django-cms installed.

```python
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
```

The test creates 2 users (in the setUp and in the post to /create_user/).
then deletes the first user. The expected beheviour would be that there is now 1 user left, the created user.

### baseline (no issue, no cms)
```bash
git checkout ea9c2c08bd098022e8f90c062342c16de98c2e67
./manage.py test
```

```
.
----------------------------------------------------------------------
Ran 1 test in 0.274s

OK
Destroying test database for alias 'default'...
```

### with cms
```bash
git checkout 52f6753cbf181c2fc52671a1be88e5f1113e3e40
./manage.py test
# unsuccessfull test
```

```
F
======================================================================
FAIL: test_all_delete (djangotest.tests.UserDeleteTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/robin.local/prog/djangotest/djangotest/tests.py", line 16, in test_all_delete
    self.assertEqual(get_user_model().objects.count(), 1)
AssertionError: 0 != 1

----------------------------------------------------------------------
Ran 1 test in 0.284s

FAILED (failures=1)
Destroying test database for alias 'default'...
```
