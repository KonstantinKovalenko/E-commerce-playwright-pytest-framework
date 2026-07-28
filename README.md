# E-Commerce Playwright + Pytest Automation Framework

Automated end-to-end testing framework for the Automation Exercise website built with **Playwright**, **Pytest**, and **Python**.

✔ Page Object Model (POM) with separated locator classes   
✔ Reusable Base Page, page objects, and fixtures  
✔ Dynamic test data generation  
✔ Environment variables with `.env` and GitHub Secrets  
✔ Cross-browser execution  
✔ Parallel test execution  
✔ Allure reporting with failure screenshots  
✔ Merged Allure Report with browser-specific results  
✔ GitHub Actions CI/CD pipeline  
✔ Automatic report publishing to GitHub Pages  
✔ Slack notifications with build status and report link

[![CI](https://github.com/KonstantinKovalenko/E-commerce-playwright-pytest-framework/actions/workflows/playwright.yml/badge.svg)](https://github.com/KonstantinKovalenko/E-commerce-playwright-pytest-framework/actions/workflows/playwright.yml)

[![GitHub Pages](https://img.shields.io/badge/View-Latest_Report-blue?logo=github)](https://konstantinkovalenko.github.io/E-commerce-playwright-pytest-framework/)

[![GitHub Slack Notification](https://img.shields.io/badge/GitHub-View_Slack_Notification-181717?logo=github&logoColor=white)](https://github.com/KonstantinKovalenko/E-commerce-playwright-pytest-framework/blob/main/assets/screenshots/slack-notifications.png)

---

## Test Coverage

- 26 official Automation Exercise test scenarios
- Chromium and Firefox execution
- 52 automated test executions per GitHub Actions workflow
- Merged Allure Report with browser-specific results

---

## Continuous Integration

GitHub Actions automatically:

- Installs dependencies and Playwright browsers
- Executes tests on Chromium and Firefox
- Merges browser test results into a single Allure Report
- Publishes reports to GitHub Pages
- Sends Slack notifications

---

## Project Structure

```
├── .github/ 
│ └── workflows/ 
│     └── playwright.yml 
│
├── assets/
│   ├── downloads/ 
│   ├── uploads/ 
│   └── screenshots/ 

│
├── config/
│   └── settings.py  
│
├── pages/ 
│   ├── account/ 
│   ├── checkout/ 
│   ├── products/  
│   ├── components/ 
│   ├── locators/ 
│   │   ├── account/  
│   │   ├── checkout/  
│   │   ├── products/  
│   │   └── components/
│   ├── base_page.py 
│   └── ... 
│
├── tests/ 
│   ├── test_01_register_and_delete_account.py 
│   ├── ... 
│   └── test_26_scroll_page.py 
│
├── utils/ 
│   ├── data_generator.py 
│   ├── test_data.py 
│   └── helpers.py 
│
├── conftest.py 
├── pytest.ini 
├── requirements.txt 
└── README.md
```

---

## Getting Started

### Installation

Clone the repository:

```bash
git clone https://github.com/KonstantinKovalenko/E-commerce-playwright-pytest-framework.git  
```

```
cd E-commerce-playwright-pytest-framework
```

Create virtual environment

```bash
python -m venv .venv
```
Activate

```bash
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Install Playwright browsers

```
python -m playwright install
```

---

### Environment Variables

Create an `.env` file in the project root.

```
TEST_USER_EMAIL=your_email  
TEST_USER_PASSWORD=your_password
```

These credentials are used for login-related test scenarios.

In GitHub Actions the values are provided securely through GitHub Secrets.

---

### Useful Commands

| Command | Description |
|---------|-------------|
| `pytest` | Run all tests with default configuration |
| `pytest --browser chromium` | Run all tests in Chromium |
| `pytest --browser firefox` | Run all tests in Firefox |
| `pytest -n 2 --browser chromium` | Run Chromium tests in parallel execution |
| `pytest -n 2 --browser firefox` | Run Firefox tests in parallel execution |
| `pytest tests/test_01_register_user.py` | Run a single test |
| `allure open allure-report` | Open the generated Allure Report |

---

## Author

Konstantin Kovalenko

* GitHub: [KonstantinKovalenko](https://github.com/KonstantinKovalenko)
* LinkedIn: [Kostyantyn Kovalenko](https://www.linkedin.com/in/kostyantyn-kovalenko/)
* Telegram: @kovakost
* Email: chvyaka.kk@gmail.com
