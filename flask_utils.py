
def serialize_names(names_obj):
    name_dict = {}
    name_dict['first'] = names_obj.first
    name_dict['last'] = names_obj.last
    name_dict['email'] = names_obj.email
    return name_dict