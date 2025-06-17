class LeavePage:
    def __init__(self, page):
        self.page = page

    def apply_leave(self, leave_type, start_date):
        self.page.click("a[href='/web/index.php/leave/applyLeave']")
        self.page.wait_for_selector("h6:has-text('Apply Leave')")
        self.page.locator("div.oxd-select-wrapper").click()
        self.page.locator(f"div[role='option'] >> text={leave_type.strip()}").click()
        self.page.locator("input[placeholder='yyyy-mm-dd']").first.fill(start_date.strip())
        self.page.click("button[type='submit']")
        self.page.wait_for_timeout(2000)

    def verify_leave_list(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList")
        self.page.wait_for_selector("h6:has-text('Leave List')")
        return self.page.locator("h6:has-text('Leave List')").is_visible()
