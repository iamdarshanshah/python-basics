from abc import abstractmethod


class TouchScreenLaptop:
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):
    def scroll(self):
        print("HP Scroll")


class DELL(TouchScreenLaptop):
    def scroll(self):
        print("DELL Scroll")


class HPNotebook(HP):
    def click(self):
        print("HP notebook click")


class DELLNotebook(DELL):
    def click(self):
        print("DELL notebook click")


hpnotebook = HPNotebook()
dellnotebook = DELLNotebook()

hpnotebook.click()
hpnotebook.scroll()

dellnotebook.click()
dellnotebook.scroll()
