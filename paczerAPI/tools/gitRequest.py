from gitPaczer.settings import GitHub_credentials
import requests


def gitRequest(owner, repositoryName):
    return requests.get("https://api.github.com/repos/" + owner + "/" + repositoryName, auth=(GitHub_credentials["Login"], GitHub_credentials["Password"]))