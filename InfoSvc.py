'''
    This is an information API which actually is written using Falcon library.
    This would accept request and respond to that request synchronously.
'''

import json
import falcon
import time
import uuid
from wsgiref import simple_server

from Util import *

class InfoResource:

    def on_get(self, req, resp):

        requestCorrelationId = str(uuid.uuid4())
        print(Util.getLogTimeStamp(), "Received request ::[" + requestCorrelationId + "]")
        time.sleep(0)
        result = json.dumps({"result": "success","id": requestCorrelationId})
        print(Util.getLogTimeStamp(), "Sending Response ::[" + result + "]")
        resp.status = falcon.HTTP_200
        resp.body = result



app = falcon.API()
infoResouceObj = InfoResource()

app.add_route("/info", infoResouceObj)

if __name__ == "__main__":
    httpd = simple_server.make_server('0.0.0.0', 5000, app)
    print("Info service would be running as per below.")
    print(Util.getLogTimeStamp(), "Info api has been started and listening on http://0.0.0.0:5000/info")

    httpd.serve_forever()