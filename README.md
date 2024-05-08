# 🌐 Domain Insights API 🔍

An [API](https://dns-toolkit.onrender.com/docs) allows developers to retrieve information about domain names, including DNS records, WHOIS information, and more.

Check out the [swagger documentation](https://dns-toolkit.onrender.com/docs) to test and learn more about the API.

## 🚀 Features

- 🔍 **DNS Record Lookup:** Fetch DNS records (A, AAAA, MX, TXT, NS, CNAME) for a given domain name.
- 🌍 **WHOIS Information:** Get detailed WHOIS information about a domain, including registrar, creation date and expiration date.

### 🔍 DNS Record Lookup

- **Endpoint:** `/dns-records`
- **Method:** GET
- **Query Parameters:**
  - `domain` (required): The domain name to lookup DNS records for.
  - `record_type` (optional): The type of DNS record to retrieve (A, AAAA, MX, TXT, NS, CNAME). Default is 'A'.
  - `page` (optional): The page number for pagination. Default is 1.
  - `page_size` (optional): The number of results per page. Default is 10.
- **Response:** Returns a JSON object containing the domain name, record type, and a list of DNS records.

### 🌍 WHOIS Information

- **Endpoint:** `/domain-details`
- **Method:** GET
- **Query Parameters:**
  - `domain` (required): The domain name to retrieve WHOIS information for.
- **Response:** Returns a JSON object containing the domain name, registrar, creation date, expiration date, last updated date, and status.

## 📝 Example Usage

Here are a few examples of how you can use the Domain Insights API:

### DNS Record Lookup

```bash
curl -X GET "https://dns-toolkit.onrender.com/dns-records?domain=example.com&record_type=A&page=1&page_size=10"
```

### WHOIS Information

```bash
curl -X GET "https://dns-toolkit.onrender.com/domain-details?domain=example.com"
```
