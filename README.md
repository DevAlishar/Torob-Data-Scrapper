# Torob Data Scrapper

This project is a Python script designed to fetch product information from Torob.com, a Persian e-commerce platform. The script makes HTTP requests to retrieve product details based on a specified URL and stores the data in JSON format.

## Project Structure

- `Fetcher` class: Manages the session, sets up headers and proxies, and handles data fetching.
- `get(prk, prname)`: Retrieves product details from the API.
- `save_to_file(data)`: Saves the retrieved data to `sellers_info.json`.
- `update_file(new_data)`: Updates the existing JSON file with new data.
  
## Prerequisites

- Python 3.x
- `requests` library

To install the requests library, run:
```bash
pip install requests
