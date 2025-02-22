def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter

def count_charakters(text):
    characters = {
        "a" : 0 ,
        "b" : 0 ,
        "c" : 0 ,
        "d" : 0 ,
        "e" : 0 ,
        "f" : 0 ,
        "g" : 0 ,
        "h" : 0 ,
        "i" : 0 ,
        "j" : 0 ,
        "k" : 0 ,
        "l" : 0 ,
        "m" : 0 ,
        "n" : 0 ,
        "o" : 0 ,
        "p" : 0 ,
        "q" : 0 ,
        "r" : 0 ,
        "s" : 0 ,
        "t" : 0 ,
        "u" : 0 ,
        "v" : 0 ,
        "w" : 0 ,
        "x" : 0 ,
        "y" : 0 ,
        "z" : 0 ,
        "ô" : 0 ,
        "ë" : 0 ,
        "ê" : 0 ,
        "â" : 0 ,
        "æ" : 0 ,
    }
    text = text.lower()
    for character in text:
        if character == "a":
            characters["a"] += 1
        elif character == "b":
            characters["b"] += 1
        elif character == "c":
            characters["c"] += 1
        elif character == "d":
            characters["d"] += 1
        elif character == "e":
            characters["e"] += 1
        elif character == "f":
            characters["f"] += 1
        elif character == "g":
            characters["g"] += 1
        elif character == "h":
            characters["h"] += 1
        elif character == "i":
            characters["i"] += 1
        elif character == "j":
            characters["j"] += 1
        elif character == "k":
            characters["k"] += 1
        elif character == "l":
            characters["l"] += 1
        elif character == "m":
            characters["m"] += 1
        elif character == "n":
            characters["n"] += 1
        elif character == "o":
            characters["o"] += 1
        elif character == "p":
            characters["p"] += 1
        elif character == "q":
            characters["q"] += 1
        elif character == "r":
            characters["r"] += 1
        elif character == "s":
            characters["s"] += 1
        elif character == "t":
            characters["t"] += 1
        elif character == "u":
            characters["u"] += 1
        elif character == "v":
            characters["v"] += 1
        elif character == "w":
            characters["w"] += 1
        elif character == "x":
            characters["x"] += 1
        elif character == "y":
            characters["y"] += 1
        elif character == "z":
            characters["z"] += 1
        elif character == "ô":
            characters["ô"] += 1
        elif character == "ë":
            characters["ë"] += 1
        elif character == "ê":
            characters["ê"] += 1
        elif character == "â":
            characters["â"] += 1
        elif character == "æ":
            characters["æ"] += 1
    return characters

def sorted_charakters(charakters):
    #dict wird durch sorted zu einem tuple
    sorted_list = sorted(charakters.items(), key =lambda x : x[1], reverse=True)
    #dict() benutzen um es einfach wieder in ein dict umzuwandeln
    sorted_list = dict(sorted_list)
    return sorted_list