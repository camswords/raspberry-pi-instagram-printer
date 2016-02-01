
class Job:

    def __init__(self, connection, job_id):
        self.connection = connection
        self.job_id = job_id

    def attributes(self):
        print self.connection.getJobAttributes(self.job_id)
        return "foo"

    def __str__(self):
        return "job(%s)" % self.job_id
