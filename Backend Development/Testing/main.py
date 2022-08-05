def Get_none():
    return None

def flatten_dict(dict):
    listdict = []
    listdict.append(dict)
    dict = listdict
    return dict

Get_none()

flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14})
