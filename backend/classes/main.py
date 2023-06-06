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

    def compare_players(self, player_1, player_2, attr):
        def get_stats(player):
            return (
                getattr(player, attr),
                player.strength(),
                self.sum_player(player)
            )
        p1 = get_stats(player_1)
        p2 = get_stats(player_2)
        if p1 > p2:
            return player_1.name
        if p1 < p2:
            return player_2.name
        return "These two players might as well be twins!"

if __name__ == "__main__":
    alice = Player('Alice', 0.8, 0.2, 0.6)
    bob = Player('Bob', 0.9, 0.2, 0.6)
    Commentator.compare_players(alice, bob, 'speed')
