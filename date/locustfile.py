import socket
import time
from random import randint

from locust import Locust, TaskSet, events, task, between, User, HttpLocust, HttpUser

class DateLocust(TaskSet):
    @task(7)
    def date(self):
        start_time = time.time()
        response = ''
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((self.user.host, 49090))
                sock.sendall('what is the time now'.encode('utf-8'))
                response = sock.recv(1024).decode('utf-8')
        except Exception as e:
            total_time = int(time.time() - start_time) * 1000
            events.request_failure.fire(request_type='date',
                                        name='time',
                                        response_time=total_time,
                                        response_length=0,
                                        exception=e)
        else:
            total_time = int(time.time() - start_time) * 1000
            events.request_success.fire(request_type='date',
                                        name='time',
                                        response_time=total_time,
                                        response_length=len(response))


class SocketUser(User):
    host = 'localhost'

    tasks = {DateLocust}

    wait_time = between(1, 3)