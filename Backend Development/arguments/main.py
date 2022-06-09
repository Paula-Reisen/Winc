# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, template='Hello, <name>!'):
    if name != '':
        new_greeting = template.replace('<name>', name)
        return new_greeting


def force(mass, body='earth'):
    arguments = {'sun': round(274),
                         'jupiter': 24.92,
                         'neptune': 11.15,
                         'saturn': 10.44,
                         'earth': 9.798,
                         'uranus': 8.87,
                         'venus': 8.87,
                         'mars': 3.71,
                         'mercury': 3.7,
                         'moon': 1.62,
                         'pluto': 0.58
                         }
    body = arguments[body]
    return round(body, 1) * mass

def pull(m1, m2, d):
    G = 6.674 * (10**-11)
    F = (G * m1*m2)/(d**2)
    return(F)

pull(800, 1500, 3)