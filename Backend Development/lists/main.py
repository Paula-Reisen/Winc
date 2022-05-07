# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line


def alphabetical_order(film_names):
    film_names.sort()
    return(film_names)


def won_golden_globe(film_name):
    won_golden_globe = ["Jaws", "Star Wars: Episode IV  A New Hope",
                        "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]
    won_golden_globe = (map(lambda x: x.lower(), won_golden_globe))
    won_golden_globe = list(won_golden_globe)
    
    if film_name.lower() in won_golden_globe:
        return(True)
    else:
        return(False)


def remove_toto_albums(albums):
    if "Toto XX" in albums:
        albums.remove("Toto XX")
    if "Hydra" in albums:
        albums.remove("Hydra")
    if "Toto XIV" in albums:
        albums.remove("Toto XIV")
    if "Old Is New" in albums:
        albums.remove("Old Is New")
    if "The Seventh One" in albums:
        albums.remove("The Seventh One")
    if "Falling in Between" in albums:
        albums.remove("Falling in Between")
    if "Fahrenheit" in albums:
        albums.remove("Fahrenheit")
    
    albums.sort
    return(albums)


film_names = ["Tom Sawyer", "Saving Private Ryan", "Jaws", "Star Wars: Episode IV  A New Hope", "E.T. the Extra-Terrestrial"]
alphabetical_order(film_names)
film_name = "jaws"
won_golden_globe(film_name)
film_name = "JAWS"
won_golden_globe(film_name)
albums = ["Old Is New"]
remove_toto_albums(albums)
