# Binance API C2C Ads Detail Fetcher

This script interacts with the Binance API to fetch the details of a specific C2C (customer-to-customer) ad by its ad number. It uses HMAC SHA-256 for signing the request, ensuring secure communication with the API.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- `requests` library installed (for making HTTP requests).

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/robigoh/binance_api_sample.git
   cd repositoryname

2. **Install the Required Python Packages:**

   Use `pip` to install the `requests` library.

    ```bash
    pip install requests
    ```
   `certifi` is included with `requests`, and `time`, `hashlib`, and `hmac` are part of the standard Python library, so no additional installation is required for them.

## Configuration

1. **API Keys:**
   - You need to obtain an API key and API secret from Binance. This can be done via the Binance API Management section.
   - Replace `"your_api_key"` with your actual Binance API key.
   - Replace `"your_api_secret"` with your actual Binance API secret.
  
2. **Ad Number:**
   - Replace `"your_20_digit_ads_no"` with the 20-digit ad number you wish to query.

## Usage

1. **Running the Script:**

   Once you've configured the script with your API credentials and ad number, run the script:

   ```bash
   python get_ads_det_by_ads_no.py

3. **Expected Output:**

   The script will output the JSON response from Binance, which contains the details of the specified ad.
