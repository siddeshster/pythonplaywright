import pytest
from pages.LeavePage import LeavePage
from pages.LogoutPage import LogoutPage
from utils.excel_reader import get_leave_data
from playwright.sync_api import expect

leave_data = get_leave_data("testdata/leave_data.xlsx")

@pytest.mark.parametrize("data", leave_data)
def test_leave_request(page, data):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    page.get_by_placeholder("Username").fill(data["username"])
    page.get_by_placeholder("Password").fill(data["password"])
    page.locator("button[type='submit']").click()
    expect(page.locator("h6")).to_have_text("Dashboard")

    # Apply Leave
    leave_page = LeavePage(page)
    leave_page.navigate_to_leave_request()
    leave_page.apply_leave(data["leave_type"], data["from_date"], data["to_date"], data["comment"])

    # Logout
    logout_page = LogoutPage(page)
    logout_page.logout()
