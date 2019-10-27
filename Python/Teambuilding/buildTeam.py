from Teambuilder import mostResistancesTeam
#Results
# Desiring guaranteed resistace is too much to ask for,
# 7 team size is still not enough for an environment of 1-10
# So instead, find with safe switch-ins as specified in TypingChart
# The number of possible guaranteed resist switch ins
# is compared to the number of possible foe typings
# as a measure of quality.

n = 6
guessQuality = 0.8
print('Desired size of team: ', n)
Teams, resistances, quality = mostResistancesTeam(n,'dual1-10','dual1-10', guessQuality)
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
