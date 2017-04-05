#!flask/bin/python
from app import app
import ssl
#context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
#context.load_cert_chain('/data4/SSL/fullchain.crt', '/data4/SSL/shivmevawala.key')
#app.run(host='0.0.0.0', port=443,debug=True, ssl_context=context )
app.run(host='0.0.0.0', port=80,debug=True)
