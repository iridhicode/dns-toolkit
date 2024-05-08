import ssl
import socket

ssl_info = {}

def get_ssl_details(domain: str) :
    try:
        # Create an SSL context
        context = ssl.create_default_context()

        # Establish an SSL/TLS connection to the specified domain
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                # Retrieve SSL/TLS certificate
                cert = ssock.getpeercert()

                ssl_info["domain"] = domain
                ssl_info["is_secure"] = True

                # Retrieve SSL/TLS protocol version
                ssl_info["protocol"] = ssock.version()

                # Retrieve SSL/TLS cipher suite
                ssl_info["cipher"] = ssock.cipher()[0]

                # Retrieve SSL/TLS certificate information
                ssl_info["subject"] = cert["subject"]
                ssl_info["issuer"] = cert["issuer"]
                ssl_info["valid_from"] = cert["notBefore"]
                ssl_info["valid_to"] = cert["notAfter"]
    except Exception as e:
        ssl_info["domain"] = domain
        ssl_info["is_secure"] = False
        ssl_info["error"] = "Something went wrong, please retry!"

    return ssl_info