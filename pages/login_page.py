from utils.logger import get_logger
logger = get_logger("login_page")

class LoginPage:
    def __init__(self, page):
        self.page = page

    def load(self):
        logger.info("Navigating to login page")
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, username, password):
        logger.info(f"Attempting login with: {username}")
        self.page.fill("input[name='username']", username)
        self.page.fill("input[name='password']", password)
        self.page.click("button[type='submit']")
