# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


def alphabetical_order(film_names):
    return sorted(film_names)


def won_golden_globe(film_name):
    golden_globe_winning_films = [
        'jaws', 'star wars: episode iv – a new hope'
        'e.t. the extra-terrestrial', 'memoirs of a geisha'
    ]
    return film_name.lower() in golden_globe_winning_films


def remove_toto_albums(albums):
    toto_albums = [
        'Fahrenheit', 'The Seventh One',
        'Toto XX', 'Falling in Between',
        'Toto XIV', 'Old Is New',
        'Joseph Williams', 'I Am Alive',
        '3', 'Early Years',
        'Vertigo', 'Two of Us',
        'Vertigo 2', 'Smiles',
        'Tears', 'This Fall',
        'Denizen Tenant', 'Williams/Friestedt',
        'CWF', '10 Miles',
        'CWF 2', 'Carrie'
    ]
    return [a for a in albums if a not in toto_albums]
