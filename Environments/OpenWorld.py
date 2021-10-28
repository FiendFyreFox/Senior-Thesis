import timeit


class OpenWorld:

    def __init__(self):
        self.encryption_method = None
        self.members = []

    def add_member(self, member):

        self.members.append(member)

    def broadcast(self, sender, message, key):

        message = self.encrypt(message, None, self.encryption_method)

        for e in self.members:
            e.receive(sender, message)
        sender.write_to_log(message, sender, "sent")

    def encrypt(self, message, key, algorithm):
        start = timeit.default_timer()

        # encryption goes here

        end = timeit.default_timer()
        print("spent ", end - start, " seconds on encryption")
        return message
