import re

def extract_city(query):
    patterns = [
        r"what is the temperature in(.+)",
        r"what is temperature in(.+)",
        r"temperature of(.+)",
        r"temperature in(.+)",
        r"(.+) temperature",
        r"(.+) what city is this",
        r"tell me temperature in(.+)",
        r"tell me temperature of(.+)"
        
    ]
    
    for pattern in patterns:
        match = re.search(pattern, query, re.IGNORECASE)
        if match:
            return match.group(1).strip()    
    return None
