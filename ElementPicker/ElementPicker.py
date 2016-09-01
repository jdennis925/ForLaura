import random
import sys

pythonVersion = sys.version_info

def inputWrapper(message = ''):
    if pythonVersion < (3,0):
        return raw_input(message)
    else:
        return input(message)

periodicTable = [
    'Hydrogen',
    'Helium',
    'Lithium',
    'Beryllium',
    'Boron',
    'Carbon',
    'Nitrogen',
    'Oxygen',
    'Fluorine',
    'Neon',
    'Sodium',
    'Magnesium',
    'Aluminium',
    'Silicon',
    'Phosphorus',
    'Sulfur',
    'Chlorine',
    'Argon',
    'Potassium',
    'Calcium',
    'Scandium',
    'Titanium',
    'Vanadium',
    'Chromium',
    'Manganese',
    'Iron',
    'Cobalt',
    'Nickel',
    'Copper',
    'Zinc',
    'Gallium',
    'Germanium',
    'Arsenic',
    'Selenium',
    'Bromine',
    'Krypton',
    'Rubidium',
    'Strontium',
    'Yttrium',
    'Zirconium',
    'Niobium',
    'Molybdenum',
    'Technetium',
    'Ruthenium',
    'Rhodium',
    'Palladium',
    'Silver',
    'Cadmium',
    'Indium',
    'Tin',
    'Antimony',
    'Tellurium',
    'Iodine',
    'Xenon',
    'Caesium',
    'Barium',
    'Lanthanum',
    'Cerium',
    'Praseodymium',
    'Neodymium',
    'Promethium',
    'Samarium',
    'Europium',
    'Gadolinium',
    'Terbium',
    'Dysprosium',
    'Holmium',
    'Erbium',
    'Thulium',
    'Ytterbium',
    'Lutetium',
    'Hafnium',
    'Tantalum',
    'Tungsten',
    'Rhenium',
    'Osmium',
    'Iridium',
    'Platinum',
    'Gold',
    'Mercury',
    'Thallium',
    'Lead',
    'Bismuth',
    'Polonium',
    'Astatine',
    'Radon',
    'Francium',
    'Radium',
    'Actinium',
    'Thorium',
    'Protactinium',
    'Uranium',
    'Neptunium',
    'Plutonium',
    'Americium',
    'Curium',
    'Berkelium',
    'Californium',
    'Einsteinium',
    'Fermium',
    'Mendelevium',
    'Nobelium',
    'Lawrencium',
    'Rutherfordium',
    'Dubnium',
    'Seaborgium',
    'Bohrium',
    'Hassium',
    'Meitnerium',
    'Darmstadtium',
    'Roentgenium',
    'Copernicium',
    'Ununtrium',
    'Flerovium',
    'Ununpentium',
    'Livermorium',
    'Ununseptium',
    'Ununoctium'
]

print('Element Picker! (Laura Fox is the coolest!)')
includeFBlock = inputWrapper('include f-block? (y/n)')
print('hit ENTER for the next element!')
inputWrapper()

while(True):

    inFblock = False
    atomicIndex = random.randint(0, len(periodicTable) - 1)
    if(atomicIndex > 56 and atomicIndex < 71) or (atomicIndex > 88 and atomicIndex < 103):
        inFblock = True
    if(not inFblock or includeFBlock == 'y'):
        print("[{0}] - {1}".format(atomicIndex + 1, periodicTable[atomicIndex]))
        inputWrapper()
