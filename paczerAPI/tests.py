from django.test import TestCase
import time
from gitPaczer.settings import GitHub_credentials
from paczerAPI.tools.gitRequest import gitRequest

class testRequestsTime(TestCase):
    def testing(self):
        start = time.time()
        for i in range(0, 20):
            gitRequest("MikusRy", "Django_School")
        end = time.time()
        print("\n" + str(end - start) + " sekundy")
