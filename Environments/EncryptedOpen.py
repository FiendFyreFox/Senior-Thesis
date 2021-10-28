import string
import timeit

from Environments.OpenWorld import OpenWorld


class EncryptedOpen(OpenWorld):

    def __init__(self, algorithm):

        super().__init__()
        self.encryption_method = algorithm

    def broadcast(self, sender, message, key):

        message = self.encrypt(message, key, self.encryption_method)

        for e in self.members:
            e.receive(sender, message)
        sender.write_to_log(message, sender, "sent")

    def encrypt(self, old_msg, key, algorithm):
        start = timeit.default_timer()
        message = ""

        if algorithm == "substitution":
            chars = list(string.printable)
            for i, char in enumerate(old_msg):
                index = chars.index(char)
                new_index = (key + index) % len(chars)
                message += chars[new_index]

        else:
            print('Error: unknown encryption algorithm')

        end = timeit.default_timer()
        print("spent ", end - start, " seconds on encryption")
        return message
