Welcome to Twilio Bootcamp!

Over the next couple days we will be going over the basics of Python and Twilio in order to help you build your very own app!

We understand that this is going to be a LOT of content over the next couple days, so please don't hesitate to ask us any questions if you are stuck!

Before we get started, please follow the steps below:
1. Rename the file `.env.example` to `.env`. This file contains any secrets that your app will need.

2. Log on to the Twilio console at `www.twilio.com/console`. Here you will find your Twilio Account SID and Twilio Auth Token. Copy these values into the `.env` file, replacing `AC123` and `foobar` respectively.

3. Open `main.py`. Here you find our starter application. It should resemble...
```
from flask import Flask

app = Flask('bootcamp')



app.run(debug=True, host='0.0.0.0', port=8080)

```

4. Press the `run` button. You should see a bunch of output on the right panel. The final lines of output should resemble...
```
 * Serving Flask app "bootcamp" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 102-245-813
172.18.0.1 - - [28/May/2019 21:08:39] "GET / HTTP/1.1" 404 -
172.18.0.1 - - [28/May/2019 21:08:39] "GET / HTTP/1.1" 404 -
```

If you see this you are ready to go! We can't wait to see what you build!
