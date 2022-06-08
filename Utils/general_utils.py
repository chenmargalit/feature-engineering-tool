def remove_from_dict(dictionary, keys):
    for key in keys:
        if key in dictionary:
            dictionary.pop(key)
