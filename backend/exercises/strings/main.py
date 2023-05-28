# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


# 1st goal - Ruud Gullit @ 33min
# 2nd goal - Marco van Basten @ 53min
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

# <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)

# <scorer_name> scored in the <when_they_scored>nd minute
# <scorer_name> scored in the <when_they_scored>th minute
report = (
    f'{scorer_0} scored in the {goal_0}nd minute\n'
    f'{scorer_1} scored in the {goal_1}th minute'
)

player = 'Vagiz Khidiyatullin'

# 'Vagiz'
first_name = player[:player.find(' ')]

# 'Khidiyatullin'
last_name = player[player.find(' ') + 1:]
last_name_len = len(last_name)

# 'V. Khidiyatullin'
name_short = first_name[0] + '. ' + last_name

# 'Vagiz! Vagiz! Vagiz! Vagiz! Vagiz!'
chant = f'{(first_name + "! ") * len(first_name)}'.rstrip()

# Does the chant have trailing spaces? True => no, False => yes
good_chant = chant[-1] != ' '
