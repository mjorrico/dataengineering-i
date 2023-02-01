import fileinput
import string
import json
import re

ALLOWED_CHARS = string.ascii_letters + "ÅÄÖåäö" + " "
PRONOUNS = ["han", "hon", "den", "det", "denna", "denne", "hen"]

for raw_json in fileinput.input():
    if raw_json == "\n":
        continue
    
    raw_json = json.loads(raw_json)
    
    line = raw_json["text"]
    line = line.strip()
    line = re.sub(f"[^{ALLOWED_CHARS}]+", "", line)
    line = re.sub(f"[{string.whitespace}]+", " ", line)
    line = line.lower()
    words = line.split()

    for p in PRONOUNS:
        if p in words:
            print(f"{p} 1")
