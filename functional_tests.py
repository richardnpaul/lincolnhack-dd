from selenium import webdriver
import unittest

class ProfileUserTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # User visits the site and sees a Login link
    def test_can_login_and_be_redirected_to_the_profile_page(self):
        self.browser.get('http://localhost:8000')
        # Let's have a look at the title, yes, that looks correct
        self.assertIn('LincolnHack 2016', self.browser.title)
        self.fail('Complete writing the tests')


    # User experiences the above and clicks on the login link is and sees login
    # form

    # User experiences the above and logs in with login details, is redirected to
    # profile page

    # User experiences the above and the profile page shows the account information
    # in a bar to the right

    # User experiences the above and sees a top bar with links to My Voting
    # History, New Votes, My MP

    # User experiences the above and sees a list of previous bills which are linked
    # to

    # User experiences the above and sees how they voted on each bill

    # User experiences the above and sees how the constituency voted on each bill

    # User experiences the above and sees how the MP voted on each bill

    # User experiences the above and sees whether the bill passed, not or hasn’t
    # been voted on yet

    # User visits the site and logs in using the login link

    # User is redirected to their profile page and sees the My MP link in the top
    # bar

    # User experiences the above and clicks on the My MP link and is redirected to
    # the page for their MP

    # User experiences the above and sees their MP information in the centre column

    # User experiences the above and can see a list of previous bills and how their
    # MP voted

    # User experiences the above and can see how the vote ended

    # User experiences the above and can see how they voted

    # User experiences the above and can see how the constituency voted


if __name__ == '__main__':
    unittest.main(warnings='ignore')