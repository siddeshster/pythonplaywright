import pytest
import allure
from utils.excel_reader import read_test_cases
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.LeavePage import LeavePage
from utils.logger import get_logger
logger = get_logger("test_data_driven")


test_data = read_test_cases("testdata/test_cases.xlsx")

@pytest.mark.parametrize("test_case", test_data)
def test_orangehrm_data_driven(page, test_case):
    login = LoginPage(page)
    dashboard = DashboardPage(page)
    pim = PIMPage(page)
    leave = LeavePage(page)

    login.load()
    login.login(test_case["username"], test_case["password"])

    action = test_case["action"]
    expected = test_case["expected"]
    extra = test_case["extra_data"]
    module = test_case["module"]

    if action == "login":
        if expected == "Dashboard":
            assert dashboard.verify_login_successful()
        else:
            assert page.locator("p:has-text('Invalid credentials')").is_visible()

    elif action == "open_menu":
        dashboard.go_to_menu(module)
        assert page.locator(f"h6:has-text('{expected}')").is_visible()

    elif action == "add_employee":
        dashboard.go_to_menu("PIM")
        first, last = extra.split(',')
        pim.add_employee(first, last)
        assert page.locator("h6:has-text('Personal Details')").is_visible()

    elif action == "apply_leave":
        dashboard.go_to_menu("Leave")
        date, leave_type = extra.split(',')
        leave.apply_leave(leave_type, date)
        assert leave.verify_leave_list()
