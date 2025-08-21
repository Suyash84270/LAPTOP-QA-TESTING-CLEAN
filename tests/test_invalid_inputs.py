from playwright.sync_api import sync_playwright, expect

def test_invalid_inputs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8501")

        # Invalid screen size
        page.get_by_label("Screen Size (in inches)").fill("-15")
        page.get_by_role("button", name="Predict Price").click()

        # App should still be alive (no crash)
        expect(page.locator("h1")).to_contain_text("Laptop Price Predictor", timeout=8000)
        browser.close()
