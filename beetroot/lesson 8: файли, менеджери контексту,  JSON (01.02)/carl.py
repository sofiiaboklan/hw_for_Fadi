import json
# Create a dict of a person
cj = {}
cj ['first_name'] = "Carl"
cj ['last_name'] = "Johnson"
cj ['cars'] = [{'brand': 'Chevrolet',
                'model': '1964 Impala',
                'color': 'black'},
               {'brand': 'Ferrari',
                'model': '1987 Testarossa',
                'colour': 'white'}]
cj['has a dog'] = True
cj['money_in_pocket'] = 500

with open('cj.json', 'w') as file_object:
    json.dump(cj, file_object)