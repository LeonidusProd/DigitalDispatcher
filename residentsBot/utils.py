def is_valid_integer(s):
    try:
        number = int(s)
        if number <= 3000:
            return True
        else:
            return False
    except ValueError:
        return False


def shorten_name(name, max_length=30):
    if len(name) <= max_length:
        return name

    parts = name.split()
    street_label = parts[0]
    street_name = parts[1]
    number_label = parts[2]
    number_number = parts[3]

    max_street_name_length = max_length - len(street_label) - len(number_label) - len(number_number)

    if len(street_name) > max_street_name_length:
        shorted_street_name = street_name[:max_street_name_length]
    else:
        shorted_street_name = street_name

    return f"{street_label} {shorted_street_name}., {number_label} {number_number}"
