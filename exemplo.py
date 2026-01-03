"""
Teste manual de integração:
- Selenium
- selenium-nanowait
- nano-wait

Rode com:
python tests/manual/test_basic_flow.py
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_nanowait import wait_for


def main():
    print("\n=== Selenium NanoWait – Manual Integration Test ===\n")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        # Site simples e confiável para testes
        driver.get("https://example.com")

        print("Page loaded. Waiting for <h1> element...\n")

        # Espera adaptativa real (NanoWait ativo)
        wait_for(
            driver,
            "h1",
            smart=True,
            verbose=True
        ).click()

        print("\nClick executed successfully.")

        # Teste de leitura + Selenium puro
        text = driver.find_element(By.TAG_NAME, "h1").text
        print(f"Text read from page: {text}")

        print("\n✅ Test finished without flaky waits.")

    finally:
        input("\nPress ENTER to close the browser...")
        driver.quit()


if __name__ == "__main__":
    main()
