# Standard Library Imports
import unittest

# 3rd Party Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ProfileUserTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    # User visits the site and sees a Login link
    def test_can_login_and_be_redirected_to_the_profile_page(self):
        self.browser.get("http://localhost:8000")
        # Let's have a look at the title, yes, that looks correct
        self.assertIn("LincolnHack 2016", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("Login", header_text)

        # User experiences the above and logs in with login details
        username_box = self.browser.find_element_by_id("id_username")
        self.assertEqual(username_box.get_attribute("placeholder"), "Enter Your Username")
        password_box = self.browser.find_element_by_id("id_password")
        self.assertEqual(password_box.get_attribute("type"), "password")

        username_box.send_keys("test_user")
        password_box.send_keys("PPPa$$wordZ1234567890")
        password_box.send_keys(Keys.ENTER)

        # and is redirected to the profile page

        # User experiences the above and the profile page shows the account
        # information in a bar to the right
        sidebar = self.browser.find_element_by_id("sidebar")
        elements = sidebar.find_elements_by_tag_name("span")
        self.assertTrue(any(element.text == "test_user" for element in elements))

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #    any(row.text == '1: Bill No.1' for row in rows)
        # )

        self.fail("Finish the test!")

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


if __name__ == "__main__":
    unittest.main(warnings="ignore")
