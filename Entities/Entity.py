import time
import string
import timeit


class Entity:

    def __init__(self, name, messages:dict):
        self.log = []
        self.name = name
        self.messages = messages

    def broadcast(self, world, msg_type, key):
        if msg_type in self.messages:
            message = self.parse_message(self.messages[msg_type])

            world.broadcast(self, message, key)

    def receive(self, other, msg):
        self.write_to_log(other, msg, "received")

    def write_to_log(self, other, msg, dir):
        self.log.append({"message": msg, "sender": str(other), "direction": dir, "timecode": time.ctime(time.time())})

    def parse_message(self, msg):
        msg = msg.replace("%name", self.name)

        return msg

    def decode_message(self, msg, algorithm, key):
        message = ""

        if algorithm == "substitution":
            chars = list(string.printable)
            for i, char in enumerate(msg):
                index = chars.index(char)
                true_index = (index - key) % len(chars)
                message += chars[true_index]

        return message

    def brute_force_message(self, msg):

        start = timeit.default_timer()

        chars = string.printable
        offset = 1

        while offset < len(chars):
            attempt = ""
            for i, v in enumerate(msg):
                attempt += chars[(chars.index(v) + offset) % len(chars)]

            matches = []

            for potential_message in list(self.messages.values()):
                matches += [i for i, j in zip(potential_message.split(), attempt.split()) if i == j]

            if matches:
                t = timeit.default_timer() - start
                print(t)
                return attempt

            offset += 1
        t = timeit.default_timer() - start
        print(t)
        return None

    def __str__(self):
        return f"{type(self).__name__} named {self.name}"
