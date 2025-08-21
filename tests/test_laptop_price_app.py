import csv
import pytest
from playwright.sync_api import sync_playwright, expect

def load_test_cases():
    with open("docs/test-cases.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def choose_option(page, label, option_text):
    page.get_by_label(label).click()
    page.get_by_role("option", name=option_text, exact=True).click()

@pytest.mark.parametrize("case", load_test_cases())
def test_laptop_price_app(case):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=80)
        page = browser.new_page()
        page.goto("http://localhost:8501")

        # Heading appears
        expect(page.locator("h1")).to_contain_text("Laptop Price Predictor", timeout=8000)

        # Combobox/selectboxes
        choose_option(page, "Brand", case["Brand"])
        choose_option(page, "Type", case["Type"])
        choose_option(page, "RAM (in GB)", case["RAM (in GB)"])
        choose_option(page, "Touchscreen", "No")           # keep constant for demo
        choose_option(page, "IPS Display", "Yes")
        choose_option(page, "Screen Resolution", case["Screen Resolution"])
        choose_option(page, "CPU", case["CPU"])
        choose_option(page, "HDD (in GB)", case["HDD (in GB)"])
        choose_option(page, "SSD (in GB)", case["SSD (in GB)"])
        choose_option(page, "GPU", case["GPU"])
        choose_option(page, "Operating System", case["Operating System"])

        # Number inputs
        page.get_by_label("Weight of the Laptop (in kg)").fill(str(case["Weight of the Laptop (in kg)"]))
        page.get_by_label("Screen Size (in inches)").fill(str(case["Screen Size (in inches)"]))

        # Predict
        page.get_by_role("button", name="Predict Price").click()
        expect(page.locator("text=The predicted price of this configuration")).to_be_visible(timeout=8000)

        browser.close()
