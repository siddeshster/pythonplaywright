class PIMPage:
    def __init__(self, page):
        self.page = page

    def add_employee(self, firstname, lastname):
        self.page.click("a[href='/web/index.php/pim/addEmployee']")
        self.page.fill("input[name='firstName']", firstname)
        self.page.fill("input[name='lastName']", lastname)
        self.page.click("button[type='submit']")
        self.page.wait_for_selector("h6:has-text('Personal Details')")
