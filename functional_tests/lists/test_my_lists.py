from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
User = get_user_model()
from django.contrib.sessions.backends.db import SessionStore

from .lists_base import FunctionalTest



class MyListsTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        user = User.objects.create(email=email)
        session = SessionStore()

        # We create a session object in the database. The session key is
        # the primary key of the user object (which is actually their email address).
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()

        # to set a cookie we need to first visit the domain.
        # 404 pages load the quickest!
        self.browser.get(self.server_url + "/404_no_such_url/")

        # We then add a cookie to the browser that matches the session on the server—on
        # our next visit to the site, the server should recognise us as a logged-in user.
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/lists',))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@example.com'
        lists_server_url = '%s%s' % (self.server_url, '/lists')

        self.browser.get(lists_server_url)

        self.wait_to_be_logged_out(email)

        # Edith is a logged-in user
        self.create_pre_authenticated_session(email)

        self.browser.get(lists_server_url)
        self.wait_to_be_logged_in(email)

