from flask import Flask, request

app = Flask('bootcamp')

@app.route('/sms', methods=['GET', 'POST'])
def sms():
  count = request.values["Body"]

  print(request.values['From'])

  if int(count) > 50:
    return """<?xml version="1.0" encoding="UTF-8"?>
  <Response>
    <Message>Deng, please enter a number between 1-50 :/</Message>
  </Response>"""

  return """<?xml version="1.0" encoding="UTF-8"?>
  <Response>
    <Message>""" + createMessage(count) + """</Message>
  </Response>"""

def createMessage(count):
  return "🌭 " * int(count)


app.run(debug=True, host='0.0.0.0', port=8080)
