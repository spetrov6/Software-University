def age_assignment(*args,**kwargs):
    dict_to_return = {}
    for name in args:
        dict_to_return[name] = kwargs.get(name[0])
    return dict_to_return