

from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Helsd, World!'

app.run(host='0.0.0.0', port=8080)

#Python 3.6.1 (default, Dec 2015, 13:05:11)
#[GCC 4.8.2] on linux  
# * Serving Flask app "app" (lazy loading)
# * Environment: production
#   WARNING: Do not use the development server in a production environment.
#   Use a production WSGI server instead.
# * Debug mode: off
# * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
#FAK.EI.P.1 - - [26/Jul/2018 13:27:20] "GET / HTTP/1.1" 200 -
 
