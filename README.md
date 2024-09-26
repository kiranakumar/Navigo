# Navigo - API Endpoint Analyzer
Navigo is a professional tool designed to analyze API specifications in JSON format. It automatically parses API paths, identifies HTTP methods, and provides a detailed overview of each endpoint, including descriptions, tags, and responses. With smart filtering, it excludes unnecessary methods like "OPTIONS" to give you accurate metrics on your API structure. Whether you’re a developer or API architect, Endpoint Explorer helps streamline your API documentation and provides a clear, concise summary of your endpoints and their functionalities. Perfect for quick insights and comprehensive API analysis.
# Key Features:
1. API Endpoint Discovery: Automatically parses and extracts all API endpoints from JSON-based API specifications, providing a clear overview of paths and methods.
2. Method Analysis (Excludes OPTIONS): Identifies and lists supported HTTP methods (like GET, POST, etc.), excluding unnecessary methods like OPTIONS for a cleaner, more relevant report.
3. Detailed Endpoint Information: Displays essential details for each endpoint, such as summaries, descriptions, associated tags, and possible response codes.
4. Endpoint & Method Counting: Calculates and reports the total number of unique API endpoints and methods, helping you understand the scope of your API.
5. Easy-to-Use Interface: A command-line tool with simple usage and clear output. Just provide the path to your JSON file, and Pathify does the rest.

# Installation
https://github.com/padayali-JD/Navigo.git

cd navigo
## Usage
python navigo.py <path_to_json_file>
