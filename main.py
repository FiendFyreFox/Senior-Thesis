from Entities.Entity import Entity
from Environments.OpenWorld import *
from Environments.EncryptedOpen import *

import string


def demo_1():
    world = OpenWorld()
    messages = {"greeting": "Hi, my name is %name!", "goodbye": "Bye, see you later!"}

    Alice = Entity("Alice", messages)
    Bob = Entity("Alice", messages)
    Charles = Entity("Charles", messages)
    Eve = Entity("Alice", messages)
    world.add_member(Alice)
    world.add_member(Bob)
    world.add_member(Charles)
    world.add_member(Eve)

    Alice.broadcast(world, "greeting")
    print(Charles.log)
    print("\nEve's managed to intercept the following:")
    print(Eve.log)


def demo_2():

    world = EncryptedOpen("substitution")
    messages = {"greeting": "Hi, my name is %name!", "goodbye": "Bye, see you later!"}

    Alice = Entity("Alice", messages)
    Bob = Entity("Alice", messages)
    Charles = Entity("Charles", messages)
    Eve = Entity("Alice", messages)
    world.add_member(Alice)
    world.add_member(Bob)
    world.add_member(Charles)
    world.add_member(Eve)

    Alice.broadcast(world, "greeting", 69284)
    print(Charles.log)
    print(Charles.decode_message(Charles.log[0]["message"], "substitution", 69284))
    print("\nEve's managed to intercept the following:")
    print(Eve.log)

    print("Eve tried to brute force the message and got:")
    print(Eve.brute_force_message(Eve.log[0]['message']))


if __name__ == '__main__':

    demo_2()
