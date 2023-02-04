#!/usr/bin/env python3

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
    if "retweeted_status" in raw_json.keys(): # if retweet, skip to the next one
        continue

    line = raw_json["text"]
    line = line.strip()
    line = re.sub(f"[^{ALLOWED_CHARS}]+", "", line)
    line = re.sub(f"[{string.whitespace}]+", " ", line)
    line = line.lower()
    words = line.split()

    for p in PRONOUNS:
        if p in words:
            print(f"{p} 1")

# ~/hadoop*/bin/hadoop jar ~/hadoop*/share/hadoop/tools/lib/hadoop*streaming*jar -files ~/hadoop_streaming/ -mapper "/usr/bin/python3 mapper.py" -reducer "/usr/bin/python3 reducer.py" -input /user/ubuntu/tweets_data/head.txt -output /user/ubuntu/non_retweets_output
