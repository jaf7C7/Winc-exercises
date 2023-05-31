# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line


class Player:
    def __init__(self, name, speed, endurance, accuracy):
        if any(i < 0 or i > 1 for i in (speed, endurance, accuracy)):
            raise ValueError
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        stats = {
            'speed': self.speed,
            'endurance': self.endurance,
            'accuracy': self.accuracy
        }
        attr = max(stats, key=stats.get)
        return (attr, stats[attr])


class Commentator:
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return sum(
            getattr(player, attr) for attr in (
                'speed',
                'endurance',
                'accuracy'
            )
        )

    def compare_players(self, p1, p2, attr):
        a1 = getattr(p1, attr)
        a2 = getattr(p2, attr)
        if a1 == a2:
            s1 = p1.strength()
            s2 = p2.strength()
            if s1 == s2:
                sum1 = self.sum_player(p1)
                sum2 = self.sum_player(p2)
                if sum1 == sum2:
                    return "These two players might as well be twins!"
                if sum1 > sum2:
                    return p1.name
                else:
                    return p2.name
            elif s1 > s2:
                return p1.name
            else:
                return p2.name
        elif a1 > a2:
            return p1.name
        else:
            return p2.name


alice = Player('Alice', 0.8, 0.2, 0.6)
bob = Player('Bob', 0.9, 0.2, 0.6)
