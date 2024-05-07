import whois
import logging
from models.RequestModel import DomainDetails
from datetime import datetime


logging.basicConfig(level=logging.INFO)

def get_domain_details(domain: str) -> DomainDetails:
    try:
        whois_info = whois.whois(domain)
        print(whois_info)
        domain_details = DomainDetails(
            domain=domain,
            registrar=whois_info.registrar_name,
            creation_date=whois_info.creation_date,
            expiration_date=whois_info.expiration_date,
            last_updated=whois_info.updated_date,
            status=whois_info.domain_status,
            dnssec = whois_info.dnssec
        )
        logging.info(f"Retrieved domain details for {domain}")
        return domain_details
    except Exception as e:
        logging.warning(f"Failed to retrieve domain details for {domain}: {str(e)}")
        return None