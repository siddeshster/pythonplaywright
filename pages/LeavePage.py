from playwright.sync_api import Page, expect

class LeavePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_leave_request(self):
        # Click the left sidebar menu item "Leave"
        # self.page.locator("a.oxd-main-menu-item span").filter(has_text="Leave").first.click()
        self.page.locator("xpath=//*[@class='oxd-main-menu-item active'][1]").click()
        # Click on the "Apply" button inside the submenu/page
        self.page.get_by_role("link", name="Apply").click()

    def apply_leave(self, leave_type, from_date, to_date, comment):
        self.page.select_option("select[name='leaveType']", label=leave_type)
        self.page.get_by_placeholder("yyyy-mm-dd").first.fill(from_date)
        self.page.get_by_placeholder("yyyy-mm-dd").nth(1).fill(to_date)
        self.page.locator("textarea[name='comment']").fill(comment)
        self.page.locator("button[type='submit']").click()

        # ✅ Wait for confirmation message
        expect(self.page.locator("div.oxd-toast")).to_be_visible(timeout=5000)
