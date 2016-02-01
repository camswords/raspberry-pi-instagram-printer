
class Job:

    def __init__(self, job_id):
        self.job_id = job_id

    def __str__(self):
        return "job(%s)" % self.job_id
