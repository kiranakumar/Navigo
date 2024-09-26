import json
import sys
import os

def print_header():
   
    header = """
    ==============================================
             Navigo Tool by Kiran
    ==============================================
    A professional tool to calculate API endpoints
    ==============================================
    """
    print(header)

def calculate_api_endpoints(json_file):
    
    if not os.path.exists(json_file):
        print(f"Error: The file '{json_file}' does not exist.")
        return
    

    print(f"Reading JSON data from: {json_file}\n")

   
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            # Debug print: Show raw data loaded from JSON
            print(f"Loaded JSON data: {data.keys()}\n")
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON. {e}")
        return
    
    
    paths = data.get('paths', {})
    if not paths:
        print("No paths found in the JSON file.")
        return
    
    print("\nAPI Endpoints and Methods:")
    print("------------------------------------------------")

    
    endpoint_count = 0
    method_count = 0

   
    for path, methods in paths.items():
        print(f"Endpoint: {path}")
        endpoint_count += 1  # Count the number of paths (endpoints)
        # For each method (e.g., GET, POST)
        for method, details in methods.items():
            if method.lower() == "options":
                continue  # Skip OPTIONS method
            method_count += 1  # Count each method (excluding OPTIONS)
            print(f"  Method: {method.upper()}")
            print(f"    Summary: {details.get('summary', 'No summary')}")
            print(f"    Description: {details.get('description', 'No description')}")
            print(f"    Tags: {', '.join(details.get('tags', []))}")
            print(f"    Responses: {', '.join(details.get('responses', {}).keys())}")
            print("------------------------------------------------")
    
    
    print(f"\nTotal Endpoints: {endpoint_count}")
    print(f"Total Methods (excluding OPTIONS): {method_count}")
    print("\n*** Process completed successfully! ***")

def main():
    print_header()
    
    
    if len(sys.argv) < 2:
        print("Usage: python api_tool.py <path_to_json_file>")
        return
    
    json_file = sys.argv[1]
    
  
    calculate_api_endpoints(json_file)

if __name__ == "__main__":
    main()
