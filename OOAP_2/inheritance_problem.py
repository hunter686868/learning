class Plant:
    def care_instructions(self):
        raise NotImplementedError("Метод должен быть переопределён")

class Succulent(Plant):
    def care_instructions(self):
        return "Поливать раз в две недели."

class Cactus(Plant):
    def care_instructions(self):
        return "Поливать раз в месяц."

class Fern(Plant):
    def care_instructions(self):
        return "Поливать дважды в неделю."