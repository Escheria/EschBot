# https://docs.google.com/document/d/1wdNS7nJMHRih_Wj55LhTkZOhISqxOODmN2aRvM-OCBM/edit
import numpy as num

monsters = {
  'dahrenmohran': {
    'shot': {
      'hornBackFin': 0.18,
      'torso':       0.20,
      'frontLegs':   0.30,
      'abdominal':   0.38,
      'frontFin':    0.40,
      'mouth':       0.60,
      'blowhole':    0.40
    },
    
    'element': {
      'fire': {
        'hornBackFin': 0,
        'torso':       0,
        'frontLegs':   0,
        'abdominal':   0,
        'frontFin':    0,
        'mouth':       0,
        'blowhole':    0
      },
      'water': {
        'hornBackFin': 0.03,
        'torso':       0.03,
        'frontLegs':   0.05,
        'abdominal':   0.05,
        'frontFin':    0.05,
        'mouth':       0.10,
        'blowhole':    0.05
      },
      'ice': {
        'hornBackFin': 0,
        'torso':       0,
        'frontLegs':   0,
        'abdominal':   0,
        'frontFin':    0,
        'mouth':       0,
        'blowhole':    0
      },
      'thunder': {
        'hornBackFin': 0.15,
        'torso':       0.08,
        'frontLegs':   0.15,
        'abdominal':   0.22,
        'frontFin':    0.22,
        'mouth':       0.20,
        'blowhole':    0.10
      },
      'dragon': {
        'hornBackFin': 0.15,
        'torso':       0.08,
        'frontLegs':   0.15,
        'abdominal':   0.22,
        'frontFin':    0.22,
        'mouth':       0.20,
        'blowhole':    0.10
      },
    }
  },

  'kushaladaora': {
    'shot': {
      'head':      0.40,
      'neck':      0.30,
      'belly':     0.25,
      'back':      0.30,
      'tail':      0.40,
      'frontLegs': 0.20,
      'backLegs':  0.25,
      'wing':      0.20
    },
    
    'element': {
      'fire': {
        'head':      0.10,
        'neck':      0.10,
        'belly':     0.10,
        'back':      0.10,
        'tail':      0.10,
        'frontLegs': 0.10,
        'backLegs':  0.10,
        'wing':      0.10
      },
      'water': {
        'head':      0.5,
        'neck':      0.5,
        'belly':     0.5,
        'back':      0.5,
        'tail':      0.5,
        'frontLegs': 0.5,
        'backLegs':  0.5,
        'wing':      0.5
      },
      'ice': {
        'head':      0,
        'neck':      0,
        'belly':     0,
        'back':      0,
        'tail':      0,
        'frontLegs': 0,
        'backLegs':  0,
        'wing':      0
      },
      'thunder': {
        'head':      0.30,
        'neck':      0.20,
        'belly':     0.15,
        'back':      0.15,
        'tail':      0.30,
        'frontLegs': 0.20,
        'backLegs':  0.15,
        'wing':      0.15
      },
      'dragon': {
        'head':      0.35,
        'neck':      0.25,
        'belly':     0.20,
        'back':      0.20,
        'tail':      0.30,
        'frontLegs': 0.20,
        'backLegs':  0.20,
        'wing':      0.20
      },
    }
  }
}

bow = {
  'charges': {
    'lvl1': [0.4, 0.7,   0.5], #Raw / Element / Status
    'lvl2': [1.0, 0.85,  1.0], #Raw / Element / Status
    'lvl3': [1.5, 1.0,   1.5], #Raw / Element / Status
    'lvl4': [1.7, 1.125, 1.5], #Raw / Element / Status
  },
  'pierce': {
    'lvl1': [6],
    'lvl2': [6],
    'lvl3': [6],
    'lvl4': [6],
    'lvl5': [6]
  },
  'rapid': {
    'lvl1': [12],
    'lvl2': [12, 4],
    'lvl3': [12, 4, 3],
    'lvl4': [12, 4, 3, 2],
    'lvl5': [12, 4, 3, 3]
  },
  'spread': {
    'lvl1': [4, 5, 4],
    'lvl2': [5, 6, 5],
    'lvl3': [4, 5, 5, 5, 4],
    'lvl4': [4, 5, 6, 5, 4],
    'lvl5': [5, 5, 6, 5, 5]
  }
}

statusMod = {
  'sleep':     [2.0, 3.0],  #Blademaster mod, item mod
  'paralysis': [1.1, 1.05], #Village/Low Rank mons, High Rank monsters
}


#bow: monster, raw atk, element atk, element, shot type
def damagecalc(args):
  monster = args[0]
  ATTACK = int(args[1])
  ELEMENT = int(args[2])
  ele = args[3]
  shot = args[4]
  shotType = shot[:-1].lower() #removes the last number
  shotLevel = shot[-1] #level
  ARROW = num.sum(bow[shotType]['lvl'+shotLevel])
  RCHARGE = bow['charges']['lvl3'][0] #assume third charge
  ECHARGE = bow['charges']['lvl3'][1] #again, assume third charge

  DEFENSE = 75 #Village: 100%, Guild *1-2 - 100%, Guild *3-5 - 95%, Guild *6 - 80% Guild *7-8 -  75%

  sumRaw = 0
  sumEle = 0
  returnstring =  'Rough damage values: '
  for zone in monsters[monster]['shot'].keys():
    # full formulas:
    # rawDmg =  (ATTACK * ARROW * HITZONE * AFFIN * RCHARGE * DIST * SKILL * SPECIAL) / (DEFENSE * RAGE * STATUS)
    # elementDmg = (ELEMENT * EHITZONE * ECHARGE * ESKILLS * ESPECIAL) / (DEFENSE * RAGE * STATUS)
    HITZONE = monsters[monster]['shot'][zone]
    EHITZONE = monsters[monster]['element'][ele][zone]
    rawDmg =  ATTACK * ARROW * HITZONE * RCHARGE / DEFENSE
    sumRaw += rawDmg
    eleDmg = ELEMENT * EHITZONE * ECHARGE / DEFENSE
    sumEle += eleDmg
    returnstring += zone + '[' + str(rawDmg) + '/' + str(eleDmg) + '] '
  returnstring += 'Sum Raw: ' + str(sumRaw) + ', Sum Element: ' + str(sumEle)
  return returnstring


#print damagecalc(['kushaladaora', 180, 360, 'thunder', 'rapid4'])