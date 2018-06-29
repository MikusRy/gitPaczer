
from django.http import HttpResponse
import requests
import json
from paczerAPI.tools.dictBuilder import DictBuilder
from paczerAPI.tools.gitRequest import gitRequest
from gitPaczer.settings import GitHub_credentials

def gitRead(request, owner, repositoryName):
    response = gitRequest(owner, repositoryName)
    if response.status_code == 200:
        return HttpResponse(json.dumps(DictBuilder(response.json()), indent=2, separators=(',', ': ')), content_type="application/json", status=response.status_code)
    else:
        return HttpResponse(json.dumps({"message": "Bad Credentials",
                                        "Recommended action": "Please, check whether your GitHub Login or Password is spelled correctly in gitRead() function located in /paczerAPI/views.py"},
                                        indent=2, separators=(',', ': ')), content_type="application/json", status=response.status_code)


def custom500(request):
    response = {'status_code': '500', 'error': '500 Internal Error'}
    return HttpResponse(json.dumps(response, indent=2, separators=(',', ': ')), content_type="application/json", status=501)


def custom404(request, exception):
    response = {'status_code': '404', 'error': '404 Not Found'}
    return HttpResponse(json.dumps(response, indent=2, separators=(',', ': ')), content_type="application/json", status=404)
