# Teambuilder Environment
import random, numpy, math

# order:
# normal, grass, water, fire, ghost, ice, bug, flying, poison, electric ...
nonExistentTypings = [
('normal', 'water'), ('normal','ghost'),('normal','ice'),('normal','bug'),
('normal','poison'),
('grass','fire'),('grass','electric'),
('water','fire'),
('fire','ice'),('fire','electric'),
('ghost','bug'),('ghost','electric'),
('ice','bug'), ('ice','poison'), ('ice','electric'),
('flying','none'),
('poison','electric')
]

# (defender, attacker)
# resistance: 0, immunity: -1, neutral: 1, effective: 2
effectiveness = {
('normal','normal') : 1, ('normal','grass') : 1, ('normal', 'fire'): 1,
('normal','water') : 1, ('normal','ghost') : -1, ('normal','ice') : 1,
('normal','bug') : 1, ('normal','flying') : 1, ('normal','poison') : 1,
('normal','electric') : 1,
('grass', 'normal') : 1, ('grass','grass') : 0, ('grass','water') : 0,
('grass','fire') : 2, ('grass','ghost') : 1, ('grass','ice') : 2,
('grass','bug') : 2, ('grass','flying') : 2, ('grass','poison') : 2,
('grass','electric') : 0,
('water', 'normal') : 1, ('water','grass') : 2, ('water','water') : 0,
('water','fire') : 0, ('water','ghost') : 1, ('water','ice') : 0,
('water','bug') : 1, ('water','flying') : 1, ('water','poison') : 1,
('water','electric') : 2,
('fire', 'normal') : 1, ('fire','grass') : 0, ('fire','water') : 2,
('fire','fire') : 0, ('fire', 'ghost') : 1, ('fire', 'ice') : 0,
('fire','bug') : 0, ('fire','flying') : 1, ('fire','poison') : 1,
('fire','electric') : 1,
('ghost','normal') : -1, ('ghost','grass') : 1, ('ghost','water') : 1,
('ghost','fire') : 1, ('ghost','ghost') : 2, ('ghost','ice') : 1,
('ghost','bug') : 0, ('ghost','flying') : 1, ('ghost','poison') : 0,
('ghost','electric') : 1,
('ice','normal') : 1, ('ice','grass') : 1, ('ice','water') : 1,
('ice','fire') : 2, ('ice','ghost') : 1, ('ice','ice') : 0,
('ice','bug') : 1, ('ice','flying') : 1, ('ice','poison') : 1,
('ice','electric') : 1,
('bug','normal') : 1, ('bug','grass') : 0, ('bug','water') : 1,
('bug','fire') : 2, ('bug','ghost') : 1, ('bug','ice') : 1,
('bug','bug') : 1, ('bug','flying') : 2, ('bug','poison') : 1,
('bug','electric') : 1,
('flying','normal') : 1, ('flying','grass') : 0, ('flying','water') : 1,
('flying','fire') : 1, ('flying','ghost') : 1, ('flying','ice') : 2,
('flying','bug') : 0, ('flying','flying') : 1, ('flying','poison') : 1,
('flying','electric') : 2,
('poison','normal') : 1, ('poison','grass') : 0, ('poison','water') : 1,
('poison','fire') : 1, ('poison','ghost') : 1, ('poison','ice') : 1,
('poison','bug') : 0, ('poison','flying') : 1, ('poison','poison') : 0,
('poison','electric') : 1,
('electric','normal') : 1, ('electric','grass') : 1, ('electric','water') : 1,
('electric','fire') : 1, ('electric','ghost') : 1, ('electric','ice') : 1,
('electric','bug') : 1, ('electric','flying') : 0, ('electric','poison') : 1,
('electric','electric') : 0
}

#typings which resists itself
#normal, grass, water, fire, ghost, ice, bug, flying, poison, electric ...
sameResistances = [
('grass','none'), ('water','none'),('fire','none'),('ice','none'),
('poison','none'), ('electric','none'),
('water','ice'), ('bug','poison'),
('grass','electric'), ('fire','electric'), ('ice','electric')
]

def getEffectiveness():
    return effectiveness

def sameResist():
    return sameResistances

def getTypingList(cond):
    if cond == 'grasswaterfire':
        return makeTypings(['grass','water','fire'])
    if cond == 'normalgrasswaterfire':
        return makeTypings(['normal','water','grass','fire'])
    if cond == 'normalgrassghost':
        return makeTypings(['normal', 'grass', 'ghost'])
    if cond == 'grassfireghost':
        return makeTypings(['grass','fire','ghost'])
    if cond == 'grasswaterghost':
        return makeTypings(['grass','water','ghost'])
    if cond == 'dual1-5':
        return makeTypings(['normal','grass','water','fire','ghost'])
    if cond == 'mono1-5':
        return makeMonoTypings(['normal','grass','water','fire','ghost'])
    if cond == 'mono1-4':
        return makeMonoTypings(['normal','grass','water','fire'])
    if cond == 'mono2-4':
        return makeMonoTypings(['grass','water','fire'])
    if cond == 'dual1-10':
        return makeTypings(['normal', 'grass', 'water', 'fire', 'ghost',
        'ice', 'bug', 'flying', 'poison', 'electric'])

def makeTypings(typeList):
    typingList = []
    addDualtypes(typeList, typingList)
    addMonotypes(typeList, typingList)
    return typingList

def makeMonoTypings(typeList):
    typingList = []
    addMonotypes(typeList, typingList)
    return typingList

def addDualtypes(typeList, typingList):
    n = len(typeList)
    IJ = makeListOrder(n)
    for ij in IJ:
        typing = (typeList[ij[0]],typeList[ij[1]])
        if typingExists(typing):
            typingList.append(typing)
    return None

def addMonotypes(typeList, typingList):
    n = len(typeList)
    for i in range(n):
        typing = (typeList[i],'none')
        typingList.append(typing)
    return None

def typingExists(typing):
    return typing not in nonExistentTypings

def makeListOrder(n):
    indexing = []
    for i in range(n):
        for j in range(i,n):
            if i != j:
                indexing.append((i,j))
    random.shuffle(indexing)
    return indexing

def makeEffectivenessMatrix():
    values = [value for value in effectiveness.values()]
    numpyValues = numpy.array(values)
    n = math.sqrt(len(values))
    m = int(n)
    n = m
    return numpyValues.reshape(n,m)
