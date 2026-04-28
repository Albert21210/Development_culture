import requests
import sys

def main():
    print("--- Starting Application ---")
    print(f"Using Python interpreter: {sys.executable}")
    
    try:
        # Простая проверка работы библиотеки requests
        response = requests.get("https://api.github.com", timeout=5)
        print(f"GitHub API Status: {response.status_code}")
        print("Environment check: SUCCESS (requests is available)")
    except Exception as e:
        print(f"Environment check: FAILED. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()