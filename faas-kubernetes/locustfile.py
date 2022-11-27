import os
import random
import time

from locust import HttpUser, between, events, task

total_ips = 0
full_url_set = []


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--ifile", default="url_list.in",
                        help="file containing urls to test on, one per line")
    # stored in environment.parsed_options.subset_size
    parser.add_argument("--subset-size", type=int, default="0",
                        help="Size of a subset per user")
    # stored in environment.parsed_options.subset_runtime
    parser.add_argument("--subset-runtime", type=int, default="-1",
                        help="Number of seconds to run each subset")


@events.init.add_listener
def on_locust_init(environment, **kwargs):

    global total_ips
    global full_url_set

    with open(environment.parsed_options.ifile) as my_file:
        full_url_set = [line.strip() for line in my_file]

    total_ips = len(full_url_set)

    # stream = os.popen('kubectl get pods | grep sb- | wc -l')
    # total_ips = int(stream.read())
    # stream.close()

    # generate url set
    # for i in range(1, total_ips):
    #     full_url_set.append("/" + str(i) + "/greeting")

    print(full_url_set)


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("test done")


class TestUser(HttpUser):

    wait_time = between(0.5, 2.5)
    subset = []
    subset_start = 0
    use_subset = False

    def get_subset(self):
        global total_ips

        # print("Using subset")
        self.subset.clear()
        for i in range(1, self.environment.parsed_options.subset_size+1):
            self.subset.append(
                full_url_set[random.randint(0, total_ips - 1)])

    def on_start(self):

        # generate subset
        # print("env subset_size=", self.environment.parsed_options.subset_size)
        if self.environment.parsed_options.subset_size > 0:
            self.use_subset = True
        else:
            print("Using full set")
            self.subset = full_url_set
        # print(self.subset)

    @ task
    def test(self):
        # print("real subset size", len(self.subset))
        c_time = time.time()
        if self.use_subset and self.subset_start + (self.environment.parsed_options.subset_runtime*1000) < c_time:
            print("Switching subset at time  : %d", c_time)
            self.get_subset()
            print(self.subset)
            self.subset_start = time .time()

        path = self.subset[random.randint(0, len(self.subset) - 1)]
        self.client.get(path)
