#!/usr/bin/env python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


char_name = input("Which charater do you want to know about? (Starlord, Mystique, Hulk) ")

char_stat = input("What stat do you waant to know about? (Real name, powers, archenemy) ")

value = marvelchars.get(char_name).get(char_stat)

print(f"{char_name}'s {char_stat} is: {value}")



