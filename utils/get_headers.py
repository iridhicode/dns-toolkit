import requests

def get_headers(domain: str):
    headers_info = {}

    try:
        # Make an HTTP request to the specified domain
        response = requests.get(f"http://{domain}")

        headers_info["domain"] = domain
        headers_info["status_code"] = response.status_code
        headers_info["headers"] = dict(response.headers)

    except requests.exceptions.RequestException as e:
        headers_info["domain"] = domain
        headers_info["error"] = "Something went wrong, please retry!"

    return headers_info