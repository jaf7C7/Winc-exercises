# Do not modify these lines
__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"

# Add your code after this line


class Homeowner:
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs
        self.contracts = []


class Specialist:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


class Electrician(Specialist):
    def __init__(self, name):
        super().__init__(name, "electrician")


class Painter(Specialist):
    def __init__(self, name):
        super().__init__(name, "painter")


class Plumber(Specialist):
    def __init__(self, name):
        super().__init__(name, "plumber")


alice = Electrician("Alice Aliceville")
bob = Painter("Bob Bobsville")
craig = Plumber("Craig Craigsville")

alfred = Homeowner(
    "Alfred Alfredson", "Alfredslane 123", ["painter", "plumber"]
)
bert = Homeowner("Bert Bertson", "Bertslane 231", ["plumber"])
candice = Homeowner(
    "Candice Candicedottir", "Candicelane 312", ["electrician", "painter"]
)

homeowners = [alfred, bert, candice]
specialists = [alice, bob, craig]

# WANT:
#
# Alfred's contracts: ['Bob Bobsville', 'Craig Craigsville']
# Bert's contracts: ['Craig Craigsville']
# Candice's contracts: ['Alice Aliceville', 'Bob Bobsville']
#
for h in homeowners:
    for n in h.needs:
        for s in specialists:
            if n == s.profession:
                h.contracts.append(s.name)
    print(f"{h.name[:h.name.find(' ')]}'s contracts: {h.contracts}")
