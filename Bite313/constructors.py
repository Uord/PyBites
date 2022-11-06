import re
from urllib.parse import urlparse


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        if re.fullmatch(re.compile(r'.*\.[a-z]{2,3}$'), name):
            self.name = name
        else:
            raise DomainException
             
       

    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively        
    
    def __str__(self):
        return self.name
        
    @classmethod
    def parse_url(cls, url):
        domain = url.split('/')[2]
        return cls(domain)
        
    @classmethod    
    def parse_email(cls, email):
        domain = email.split('@')[1]
        return cls(domain)
        
domain = Domain.parse_url("https://pybit.es/get-python-source.html")
print(domain)