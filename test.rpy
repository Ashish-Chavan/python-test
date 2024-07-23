import time

from twisted.web.resource import Resource


class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return ("")
              

resource = ClockPage()
