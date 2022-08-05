__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"
from turtle import home
from xml.sax.handler import all_features


class specialist():
    instances = []
    def __init__(self, name, profession):
        self.instances.append(self)
        self.name = name
        self.profession = profession
class homeowner():
    instances = []
    def __init__(self, name, address, needs):
        self.instances.append(self)
        self.name = name
        self.address = address
        self.needs = needs

class Electrician(specialist):
    pass


class Painter(specialist):
    pass


class Plumber(specialist):
    pass

def homeowner_contracts(homeowner:homeowner):
        contracts_profession = []
        for needs in homeowner.needs:
                if needs == bob.profession:
                    contracts_profession.append(bob.name)
                elif needs == craig.profession:
                    contracts_profession.append(craig.name)
        print(contracts_profession)

bob = specialist("Bob Bobsville", 'Painter')
craig = specialist("Craig Craigsville", 'Plumber')
alfred = homeowner("Alfred Alfredson", "Alfredslane 123", ["Painter", "Plumber"])

homeowner_contracts(alfred)