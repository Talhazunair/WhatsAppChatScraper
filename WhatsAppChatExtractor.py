from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def extract_chat_names(driver):
    """Extract all visible chat names from the side pane"""
    chat_elements = driver.find_elements(By.CSS_SELECTOR, 
        "span.x1iyjqo2.x6ikm8r.x10wlt62.x1n2onr6.xlyipyv.xuxw1ft.x1rg5ohu._ao3e")
    return [chat.get_attribute('title') for chat in chat_elements]

def scroll_and_extract(driver, pixels_per_scroll=50, scroll_pause_time=0.1):
    try:
        side_pane = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pane-side"))
        )
        
        chat_names = set()  # Using set to avoid duplicates
        total_height = driver.execute_script(
            "return arguments[0].scrollHeight", side_pane
        )
        current_position = 0
        
        while current_position < total_height:
            # Extract names at current position
            new_names = extract_chat_names(driver)
            chat_names.update(new_names)
            
            # Scroll
            driver.execute_script(
                f"arguments[0].scrollTo(0, {current_position});", 
                side_pane
            )
            
            current_position += pixels_per_scroll
            time.sleep(scroll_pause_time)
        
        # Final extraction at bottom
        chat_names.update(extract_chat_names(driver))
        return sorted(list(chat_names))
        
    except Exception as e:
        print(f"Error during scroll and extract: {str(e)}")
        return []

def main():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")
    input("Please scan the QR code and press Enter after logging in...")
    
    chat_names = scroll_and_extract(driver)
    print("\nExtracted Chat Names:")
    for name in chat_names:
        print(name)
    
    input("Press Enter to close the browser...")
    driver.quit()

if __name__ == "__main__":
    main()