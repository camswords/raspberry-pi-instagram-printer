
from job import Job

class Jobs:

    def __init__(self, connection):
        self.connection = connection

    def __str__(self):
        return "%s" % self.connection.getJobs().keys()
