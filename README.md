
# Playwright Python Automation Framework

An end-to-end UI test automation project built with **Playwright**, **Python**, and **pytest**, using the **Page Object Model (POM)** design pattern. The test covers the full user journey on [saucedemo.com](https://www.saucedemo.com) — login, adding an item to the cart, and completing checkout.

## What this project demonstrates

- Page Object Model architecture — one class per page, keeping locators and actions separate from test logic
- Data-driven testing with `@pytest.mark.parametrize`
- End-to-end flow automation: login → add to cart → checkout → order confirmation
- Assertions at every step of the flow, not just at the end
- HTML test reporting

## Tech stack

- **Playwright** — browser automation
- **Python** — language
- **pytest** — test runner and framework
- **pytest-playwright** — Playwright/pytest integration
- **pytest-html** — HTML test reports

## Project structure


## Setup

```bash
# Clone the repo
git clone https://github.com/hajramurtaza23-sketch/playwright-python-automation.git
cd playwright-python-automation

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install pytest-playwright pytest-html
playwright install
playwright install-deps
```

## Running the tests

```bash
# Run the full checkout flow test
pytest checkout_flow/login_data.py -v

# Run with the browser visible
pytest checkout_flow/login_data.py -v --headed

# Generate an HTML report
pytest checkout_flow/login_data.py --html=report.html --self-contained-html
```

## What the test covers

The end-to-end test (`checkout_flow/login_data.py`) verifies:

1. Successful login with valid credentials
2. Landing on the correct inventory page
3. Adding an item to the cart
4. Navigating to the cart page
5. Proceeding through checkout
6. Filling in checkout information
7. Completing the order and confirming the success page

Each step includes an assertion confirming the correct page was reached — not just that a click happened.

## Author

Hajra Abbasi — QA Tester transitioning into automation testing.
