class Duck:
    def talk(self):
        print('Quack Quack')


class Human:
    def talk(self):
        print('Hi Hi')


def callTalk(obj):
    obj.talk()


duck = Duck()
human = Human()

callTalk(human)
callTalk(duck)
