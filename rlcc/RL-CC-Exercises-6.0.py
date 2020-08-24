"""# Turn shoe-data.txt into a list of dicts

# Iterate over that list and print each of the dicts out

[
    {'brand': 'Adidas',
     'color':'orange',
     'size':'43'},
    {'brand': 'Adidas',
     'color':'orange',
     'size':'43'},
    ]
    
"""


def line_to_dict(a_line):
    fields = a_line.strip().split()
    output = {"brand": fields[0], "color": fields[1], "size": fields[2]}
    return output


shoe_catalog = [
    line_to_dict(one_line) for one_line in open("samplefiles/shoe-data.txt")
]

print(shoe_catalog)
