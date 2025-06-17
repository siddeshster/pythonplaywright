class DashboardPage:
    def __init__(self, page):
        self.page = page

    def verify_login_successful(self):
        self.page.wait_for_selector("h6:has-text('Dashboard')")
        return self.page.locator("h6:has-text('Dashboard')").is_visible()

    def go_to_menu(self, menu_text):
        self.page.click(f"//span[text()='{menu_text}']")
        self.page.wait_for_selector(f"h6:has-text('{menu_text}')")
