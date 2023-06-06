# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, template="Hello, <name>!"):
    return (
        template[:template.find("<name>")]
        + name
        + template[template.find("<name>") + len("<name>"):]
    )


def force(mass, body="earth"):
    # Acceleration due to gravity (m/s**2)
    gravity = {
        "mercury": 3.7,
        "venus": 8.9,
        "earth": 9.8,
        "moon": 1.6,
        "mars": 3.7,
        "jupiter": 23.1,
        "saturn": 9.0,
        "uranus": 8.7,
        "neptune": 11.0,
        "pluto": 0.7
    }
    # Force given by F = ma (N)
    return mass * gravity[body.lower()]


def pull(m1, m2, d):
    # Gravitational constant (Nm^2/kg^2)
    g = 6.674e-11
    return g * ((m1 * m2) / d ** 2)


if __name__ == "__main__":
    print(greet('Doc'))
    print(greet('Bob', "What's up, <name>!"))
    print('force on earth: ', force(5.97))
    print('force on saturn: ', force(568, 'saturn'))
