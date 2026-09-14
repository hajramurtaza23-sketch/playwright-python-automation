# Playwright Python Automation Framework

An end-to-end UI test automation project built with **Playwright**, **Python**, and **pytest**, using the **Page Object Model (POM)** design pattern. The test covers the full user journey on [saucedemo.com](https://www.saucedemo.com) — login, adding an item to the cart, and completing checkout.

## What this project demonstrates

- Page Object Model architecture — one class per page, keeping locators and actions separate from test logic
- Data-driven testing with `@pytest.mark.parametrize`
- End-to-end flow automation: login → add to cart → checkout → order confirmation
- Assertions at every step of the flow, not just at the end
- HTML test reporting
- Visual regression testing with screenshot comparison

## Tech stack

- **Playwright** — browser automation
- **Python** — language
- **pytest** — test runner and framework
- **pytest-playwright** — Playwright/pytest integration
- **pytest-html** — HTML test reports
- **pytest-playwright-visual** — visual regression testing

## Setup

```bash
git clone https://github.com/hajramurtaza23-sketch/playwright-python-automation.git
cd playwright-python-automation
python3 -m venv venv
source venv/bin/activate
pip install pytest-playwright pytest-html pytest-playwright-visual
playwright install
playwright install-deps
```

## Running the tests

```bash
pytest checkout_flow/login_data.py -v
pytest checkout_flow/login_data.py -v --headed
pytest checkout_flow/login_data.py --html=report.html --self-contained-html
pytest checkout_flow/test_visual.py -v
```

## Author

Hajra Abbasi — QA Tester transitioning into automation testing.
