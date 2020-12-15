# Name, Level, Casting Time, Duration, School, Range, Components, Text, At Higher Levels
# "Name","Level","Casting Time","Duration","School","Range","Components","Text","At Higher Levels"
# def spell_parse(spell_line):
#     spell = spell_line.split('\",\"')
#     # print(spell[0][1:].lower().replace(" ", "_").replace("\'", ""))
#     if spell[1] == 'Cantrip':
#         f_location = 'cantrip/'
#     else:
#         f_location = spell[1] + '_level/'
#     with open("../" + f_location + spell[0][1:].lower().replace(' ', '_').replace('\'', '').replace('/', '') + ".txt", 'w') as f:
#         f.write('<br><font size=5><b>' + spell[0][1:] + '</b></font>\n')
#         f.write('<br><font size=2>' + spell[1] + '-level ' + spell[4] +'</font>\n')
#         f.write('<br><b>Casting Time:</b> ' + spell[2] + '\n')
#         f.write('<br><b>Range:</b> ' + spell[5] + '\n')
#         f.write('<br><b>Components:</b> ' + spell[6] + '\n')
#         f.write('<br><b>Duration:</b> ' + spell[3] + '\n')
#         f.write('<br>\n')
#         f.write(spell[7])
#
# with open('./Spells.csv', 'r') as f:
#     for line in f:
#         spell_parse(line)
