from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin  # Handle relative image paths

def extract_product_data(url, max_pages=1):
    """
    Extracts product data (price, description, image URL) from the given e-commerce site URL.

    Args:
        url (str): The URL of the e-commerce site.
        max_pages (int, optional): The maximum number of pages to scrape. Defaults to 1.

    Returns:
        list: A list of dictionaries, where each dictionary represents a product with keys:
            'title': The product title (if available)
            'price': The product price (if available)
            'description': The product description (if available)
            'image_url': The URL of the product image (if available)
    """

    driver = webdriver.Chrome()
    driver.get('https://www.etsy.com/shop/HimalayasCrafts')

    product_data = []
    current_page = 1

    while current_page <= max_pages:
        # Find all product elements on the current page
        product_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, " wt-animated"))  # Adjust selector as needed
        )

        for product_element in product_elements:
            # Extract title (if available)
            title_element = product_element.find_element(By.CSS_SELECTOR, ".product-title")  # Adjust selector
            title = title_element.text if title_element else None

            # Extract price (if available)
            price_element = product_element.find_element(By.CSS_SELECTOR, ".product-price")  # Adjust selector
            price = price_element.text if price_element else None

            # Extract description (if available)
            description_element = product_element.find_element(By.CSS_SELECTOR, ".product-description")  # Adjust selector
            description = description_element.text if description_element else None

            # Extract image URL (if available)
            image_element = product_element.find_element(By.CSS_SELECTOR, ".product-image img")  # Adjust selector
            image_url = image_element.get_attribute("src") if image_element else None

            # Handle relative image paths
            if image_url and not image_url.startswith("http"):
                image_url = urljoin(url, image_url)

            product_data.append({
                'title': title,
                'price': price,
                'description': description,
                'image_url': image_url
            })

        # Check for "Next Page" button and navigate if available
        next_page_button = driver.find_element(By.CSS_SELECTOR, ".pagination .next")  # Adjust selector
        if next_page_button.is_enabled():
            next_page_button.click()
            current_page += 1
        else:
            break

    driver.quit()
    return product_data

# Example usage (replace with the actual e-commerce site URL)
url = "https://www.etsy.com/shop/HimalayasCrafts"
products = extract_product_data(url, max_pages=2)  # Adjust max_pages as needed

for product in products:
    print(product)
