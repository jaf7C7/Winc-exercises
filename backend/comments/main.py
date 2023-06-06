# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line
"""\
This is an example multiline comment
Which spans multiple lines
"""

# We need the time module to be able to pause execution between counts
import time

# The following should print '3...2...1...Go!' with a 1s pause between each
# count
num_seconds = 3
for countdown in reversed(range(num_seconds + 1)):  # 4, 3, 2, 1
    if countdown > 0:
        # Flush the print buffer so each count prints on time
        print(countdown, end='...', flush=True)
        time.sleep(1)
    else:
        print('Go!')

"""\
This is another multiline comment
This will be the last comment
"""
