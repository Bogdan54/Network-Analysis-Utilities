import requests

def test_proxy():
    # Read input from the user for proxy domain, IP, and credentials
    proxy_domain = input("Enter the proxy domain: ")
    proxy_ip = input("Enter the proxy IP: ")
    proxy_user = input("Enter the proxy username: ")
    proxy_password = input("Enter the proxy password: ")

    # Construct the proxy URL
    proxy_url = f"http://{proxy_domain}:{proxy_ip}/"

    # Read input from the user for the URL to test
    url = input("Enter the URL to test: ")

    # Set up the proxy configuration
    proxy_config = {
        'http': proxy_url,
        'https': proxy_url,
    }

    # Set up proxy authentication
    proxy_auth = requests.auth.HTTPProxyAuth(proxy_user, proxy_password)

    try:
        # Use requests to check the proxy
        response = requests.get(url, proxies=proxy_config, auth=proxy_auth, timeout=5)

        # Check the response status code
        if response.status_code == 200:
            status = "Proxy is working."
        else:
            status = "Proxy isn't working"
    except requests.exceptions.RequestException:
        status = "Proxy isn't working"

    # Print the result
    print(status)

if __name__ == "__main__":
    test_proxy()
