# WhatsApp Chat Scraper

A Python script using Selenium to automatically scroll through WhatsApp Web's chat list and extract chat names.

## Features
- Smooth auto-scrolling of WhatsApp Web side panel
- Extraction of all chat names
- Duplicate removal
- Configurable scroll speed and pause time

## Requirements
- Python 3.x
- Selenium WebDriver
- Chrome Browser
- ChromeDriver

## Installation
```bash
pip install selenium
```

## Usage
1. Run the script:
```bash
python whatsapp_scraper.py
```

2. Scan the WhatsApp Web QR code when prompted
3. Press Enter after login
4. Wait for the script to complete scrolling and extracting names
5. View results in console output

## Configuration
Adjust these parameters in the script:
- `pixels_per_scroll`: Controls scroll speed (default: 50)
- `scroll_pause_time`: Controls pause between scrolls (default: 0.1s)

## Notes
- Requires active WhatsApp Web session
- May need stable internet connection
- Respects WhatsApp's rate limits
