#!/usr/bin/env python3


anime_list = ("cowboy bebop, psycho-pass, attack on titan, Hunter x Hunter")

anime_details = {
'cowboy bebop':
    {'general': 'space western adventure',
    'genre': 'space western',
    'length': '20 episodes'},

'psycho-pass':
    {'genre': 'action/crime',
    'length': '24 episodes'},

'attack on titan' :
    {'genre': 'thriller/drama',
    'length': '100 episodes'},

'Hunter x Hunter' :
    {'genre': 'adventure/action',
    'length': '150 episodes'}

    }

print(*anime_list)

anime_name = input("What show would you like to know about:" )

value = anime_details.get(anime_name).get('general')

print(f"{anime_name}: {value}")


