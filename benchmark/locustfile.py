from locust import FastHttpUser, between, task


class BaseUser(FastHttpUser):
    wait_time = between(1, 2)
    url = ""

    @task
    def api_call(self):
        self.client.get(self.url, timeout=2)


class CPUUser(BaseUser):
    url = "/api/cpu-bound/"


class IOUser(BaseUser):
    url = "/api/io-bound/"
