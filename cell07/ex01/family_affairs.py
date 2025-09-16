

def find_the_redheads(family_dict):
    redheads = []

    def is_red(name):
        return family_dict[name] == "red"

    for name in family_dict.keys():
        if is_red(name):
            redheads.append(name)

    return redheads

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
