import threading
import queue
from django.test import TestCase
from .tools.getUrl import get_url


class testParallelRequestTime(TestCase):
    def testParallelRequestTime(self):
        theurl = "http://127.0.0.1:8000/repositories/MikusRy/Django_school"
        q = queue.Queue()

        for u in range(20):
            t = threading.Thread(target=get_url, args=(q, theurl))
            t.daemon = False
            t.start()
            q.put(t)

        while q.empty() is False:
            q.get().join()
