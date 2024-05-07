import logging
from models.Enum import DNSRecordType
from typing import List
import dns.resolver


logging.basicConfig(level=logging.INFO)

async def resolve_dns_records(domain: str, record_type: DNSRecordType) -> List[str]:
    print(f"Trying to resolve DNS: {domain} , for record Type: {str(record_type.value)}")
   # resolver = aiodns.DNSResolver()
    try:
        response = dns.resolver.resolve(domain, record_type.value)
        records = [record.host if record_type == DNSRecordType.NS else str(record) for record in response]
        print(f"Resolved {record_type.value} records for {domain}")
        return records
    except Exception as e:
        print(f"Error occurred while resolving IP: {str(e)}")
        logging.warning(f"Failed to resolve {record_type.value} records for {domain}: {str(e)}")
        return []