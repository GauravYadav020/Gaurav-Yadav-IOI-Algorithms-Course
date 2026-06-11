# Module 4 Lesson 4: After-Class Project
# Project Name: High-Performance DNS Routing Cache Address Translator

class DNSResolutionCache:
    def __init__(self):
        self.forward_lookup_cache = {}

    def commit_dns_binding(self, web_domain_url, target_resolved_ip):
        self.forward_lookup_cache[web_domain_url] = target_resolved_ip

    def fetch_ip_resolution(self, domain_url):
        return self.forward_lookup_cache.get(domain_url, "EXCEPT: Domain host address resolution mapping untracked.")

if __name__ == "__main__":
    dns = DNSResolutionCache()
    dns.commit_dns_binding("ioi.algorithms.edu", "10.240.12.99")
    print(f"Resolved Virtual Network Server Host Destination: {dns.fetch_ip_resolution('ioi.algorithms.edu')}")