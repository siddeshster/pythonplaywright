from playwright.sync_api import Page, expect

class LogoutPage:
    def __init__(self, page: Page):
        self.page = page

    def logout(self):
        # Click user profile icon
        self.page.locator("span.oxd-userdropdown-tab").click()

        # Click logout
        logout_option = self.page.get_by_role("menuitem", name="Logout")
        expect(logout_option).to_be_visible()
        logout_option.click()

        # ✅ Confirm we're back at login
        expect(self.page.get_by_placeholder("Username")).to_be_visible()
