from Teambuilder import mostResistancesTeam

n = 5
guessQuality = 0.8
print('Desired size of team: ', n)
Teams, resistances, quality = mostResistancesTeam(n,'gen7','gen7', guessQuality)
print('The most resistances are found')
print('given a team size of: ', n)
print('with resistances: ', resistances)
print('corresponding to quality: ', quality)
print()
for team in Teams:
    print('-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-')
    print(team.getParty())
    print('-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-')
    print()
if not Teams: print('No parties found')
else: print('All parties checked!')

#Results
# Desiring guaranteed resistace is too much to ask for,
# 7 team size is still not enough for an environment of 1-10
# So instead, find with safe switch-ins as specified in TypingChart
# The number of possible guaranteed resist switch ins
# is compared to the number of possible foe typings
# as a measure of quality.

# For a gen 7 environment, the smallest number of members for
# always having a chance on a safe switch in is 3:
# (('water', 'flying'), ('ground', 'dark'), ('electric', 'steel'))
# with quality of 0.6
# Took 5 seconds to generate

# n = 4 takes 135 s, with quality of 0.77 as
# (('electric', 'steel'), ('water', 'flying'), ('grass', 'fairy'), ('rock', 'dark'))

# n = 5 found a decent party, 0.8, after 5 minutes
#(('ground', 'dragon'), ('steel', 'dark'), ('flying', 'steel'), ('water', 'fairy'), ('grass', 'steel'))
# some more
# (('water', 'rock'), ('water', 'flying'), ('steel', 'dark'), ('ghost', 'steel'), ('grass', 'steel'))
# this one has 0.8125
#(('water', 'rock'), ('steel', 'dark'), ('flying', 'steel'), ('water', 'fairy'), ('grass', 'steel'))
# stick to the high ones from now on
#  (('grass', 'psychic'), ('water', 'flying'), ('steel', 'dark'), ('water', 'fairy'), ('electric', 'steel'))
#   0.836
#  (('grass', 'psychic'), ('steel', 'dark'), ('water', 'fairy'), ('electric', 'steel'), ('flying', 'rock'))
# (('water', 'fighting'), ('fire', 'flying'), ('rock', 'dark'), ('electric', 'steel'), ('grass', 'fairy'))
#with quality 0.8203125
#
# 20 min and still not done
# 0.85
#(('steel', 'dark'), ('water', 'ghost'), ('electric', 'steel'), ('flying', 'rock'), ('grass', 'fairy'))
# 0.84
# (('flying', 'steel'), ('water', 'fairy'), ('rock', 'dark'), ('ghost', 'steel'), ('grass', 'steel'))
# Took 48 minutes to get this:
# Quality : 0.8515625
#
#(('steel', 'dark'), ('water', 'fairy'), ('ghost', 'steel'), ('grass', 'steel'), ('flying', 'rock'))
#
#(('steel', 'dark'), ('water', 'ghost'), ('electric', 'steel'), ('flying', 'rock'), ('grass', 'fairy'))
#
# Continue? Well, using combination complexity, the next one will take about 31 hours
#
#
#The most resistances are found
#given a team size of:  5
#with resistances:  109
#corresponding to quality:  0.8515625

#-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-
#(('steel', 'dark'), ('water', 'fairy'), ('ghost', 'steel'), ('grass', 'steel'), ('flying', 'rock'))
#-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-

#-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-
#(('steel', 'dark'), ('water', 'ghost'), ('electric', 'steel'), ('flying', 'rock'), ('grass', 'fairy'))
#-~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~--~*~-

#All parties checked!
