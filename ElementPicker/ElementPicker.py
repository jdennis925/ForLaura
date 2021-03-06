import random
import sys

pythonVersion = sys.version_info

def inputWrapper(message = ''):
    if pythonVersion < (3,0):
        return raw_input(message)
    else:
        return input(message)

table = [
    {'Symbol':'H', 'Name':'Hydrogen', 'origin':'composed of the Greek elements hydro- and -gen meaning water-forming',	'mass':'1.008'},
    {'Symbol':'He', 'Name':'Helium', 'origin':'the Greek helios, sun',	'mass':'4.002602(2)'},
{'Symbol':'Li', 'Name':'Lithium', 'origin':'the Greek lithos, stone','mass':'6.94'},
{'Symbol':'Be', 'Name':'Beryllium', 'origin':'beryl, a mineral','mass':'9.0121831(5)'},
{'Symbol':'B', 'Name':'Boron', 'origin':'borax, a mineral','mass':'10.81'},
{'Symbol':'C', 'Name':'Carbon', 'origin':'the Latin carbo, coal','mass':'12.011'},
{'Symbol':'N', 'Name':'Nitrogen', 'origin':'the Greek nitron and -gen meaning niter-forming','mass':'14.007'},
{'Symbol':'O', 'Name':'Oxygen', 'origin':'from the Greek oxy-, both sharp and acid, and -gen, meaning acid-forming','mass':'15.999'},
{'Symbol':'F', 'Name':'Fluorine', 'origin':'the Latin fluere, to flow','mass':'18.998403163(6)'},
{'Symbol':'Ne', 'Name':'Neon', 'origin':'the Greek neos, meaning new','mass':'20.1797(6)'},
{'Symbol':'Na', 'Name':'Sodium', 'origin':'the English word soda (natrium in Latin)[3]','mass':'22.98976928(2)'},
{'Symbol':'Mg', 'Name':'Magnesium', 'origin':'Magnesia, a district of Eastern Thessaly in Greece','mass':'24.3059'},
{'Symbol':'Al', 'Name':'Aluminium', 'origin':'from alumina, a compound (originally aluminum)','mass':'26.9815385(7)'},
{'Symbol':'Si', 'Name':'Silicon', 'origin':'from the Latin silex, flint (originally silicium)','mass':'28.085'},
{'Symbol':'P', 'Name':'Phosphorus', 'origin':'the Greek phoosphoros, carrying light','mass':'30.973761998(5)'},
{'Symbol':'S', 'Name':'Sulfur', 'origin':'the Latin sulphur, fire and brimstone[5]','mass':'32.06'},
{'Symbol':'Cl', 'Name':'Chlorine', 'origin':'the Greek chloros, greenish yellow','mass':'35.45'},
{'Symbol':'Ar', 'Name':'Argon', 'origin':'the Greek argos, idle','mass':'39.948(1)'},
{'Symbol':'K', 'Name':'Potassium', 'origin':'New Latin potassa, potash (kalium in Latin)[3]','mass':'39.0983(1)'},
{'Symbol':'Ca', 'Name':'Calcium', 'origin':'the Latin calx, lime','mass':'40.078(4)'},
{'Symbol':'Sc', 'Name':'Scandium', 'origin':'Scandia, the Latin name for Scandinavia','mass':'44.955908(5)'},
{'Symbol':'Ti', 'Name':'Titanium', 'origin':'Titans, the sons of the Earth goddess of Greek mythology','mass':'47.867(1)'},
{'Symbol':'V', 'Name':'Vanadium', 'origin':'Vanadis, an Old Norse name for the Scandinavian goddess Freyja','mass':'50.9415(1)'},
{'Symbol':'Cr', 'Name':'Chromium', 'origin':'the Greek chroma, color','mass':'51.9961(6)'},
{'Symbol':'Mn', 'Name':'Manganese', 'origin':'corrupted from magnesia negra, see Magnesium','mass':'54.938044(3)'},
{'Symbol':'Fe', 'Name':'Iron', 'origin':'English word (ferrum in Latin)','mass':'55.845(2)'},
{'Symbol':'Co', 'Name':'Cobalt', 'origin':'the German word Kobold, goblin','mass':'58.933194(4)'},
{'Symbol':'Ni', 'Name':'Nickel', 'origin':'from Swedish kopparnickel, containing the German word Nickel, goblin','mass':'58.6934(4)'},
{'Symbol':'Cu', 'Name':'Copper', 'origin':'English word (Latin cuprum)','mass':'63.546(3)'},
{'Symbol':'Zn', 'Name':'Zinc', 'origin':'the German Zink','mass':'65.38(2)'},
{'Symbol':'Ga', 'Name':'Gallium', 'origin':'Gallia, the Latin name for France','mass':'69.723(1)'},
{'Symbol':'Ge', 'Name':'Germanium', 'origin':'Germania, the Latin name for Germany','mass':'72.630(8)'},
{'Symbol':'As', 'Name':'Arsenic', 'origin':'English word (Latin arsenicum)','mass':'74.921595(6)'},
{'Symbol':'Se', 'Name':'Selenium', 'origin':'the Greek selene, moon','mass':'78.971(8)'},
{'Symbol':'Br', 'Name':'Bromine', 'origin':'the Greek bromos, stench','mass':'79.9049'},
{'Symbol':'Kr', 'Name':'Krypton', 'origin':'the Greek kryptos, hidden','mass':'83.798(2)'},
{'Symbol':'Rb', 'Name':'Rubidium', 'origin':'the Latin rubidus, deep red','mass':'85.4678(3)'},
{'Symbol':'Sr', 'Name':'Strontium', 'origin':'Strontian, a small town in Scotland','mass':'87.62(1)'},
{'Symbol':'Y', 'Name':'Yttrium', 'origin':'Ytterby, Sweden','mass':'88.90584(2)'},
{'Symbol':'Zr', 'Name':'Zirconium', 'origin':'Persian Zargun, gold-colored; German Zirkoon, jargoon','mass':'91.224(2)'},
{'Symbol':'Nb', 'Name':'Niobium', 'origin':'Niobe, daughter of king Tantalus from Greek mythology','mass':'92.90637(2)'},
{'Symbol':'Mo', 'Name':'Molybdenum', 'origin':'the Greek molybdos meaning lead','mass':'95.95(1)'},
{'Symbol':'Tc', 'Name':'Technetium', 'origin':'the Greek tekhnetos meaning artificial','mass':'98'},
{'Symbol':'Ru', 'Name':'Ruthenium', 'origin':'Ruthenia, the New Latin name for Russia','mass':'101.07(2)'},
{'Symbol':'Rh', 'Name':'Rhodium', 'origin':'the Greek rhodos, meaning rose coloured','mass':'102.90550(2)'},
{'Symbol':'Pd', 'Name':'Palladium', 'origin':'the then recently discovered asteroid Pallas, considered a planet at the time','mass':'106.42(1)'},
{'Symbol':'Ag', 'Name':'Silver', 'origin':'English word (argentum in Latin)[3]','mass':'107.8682(2)'},
{'Symbol':'Cd', 'Name':'Cadmium', 'origin':'the New Latin cadmia, from King Kadmos','mass':'112.414(4)'},
{'Symbol':'In', 'Name':'Indium', 'origin':'indigo','mass':'114.818(1)'},
{'Symbol':'Sn', 'Name':'Tin', 'origin':'English word (stannum in Latin)','mass':'118.710(7)'},
{'Symbol':'Sb', 'Name':'Antimony', 'origin':'composed from the Greek anti, against, and monos, alone (stibium in Latin)','mass':'121.760(1)'},
{'Symbol':'Te', 'Name':'Tellurium', 'origin':'Latin tellus, earth','mass':'127.60(3)'},
{'Symbol':'I', 'Name':'Iodine', 'origin':'French iode (after the Greek ioeides, violet)','mass':'126.90447(3)'},
{'Symbol':'Xe', 'Name':'Xenon', 'origin':'the Greek xenos, strange','mass':'131.293(6)2 3'},
{'Symbol':'Cs', 'Name':'Caesium', 'origin':'the Latin caesius, sky blue','mass':'132.90545196(6)'},
{'Symbol':'Ba', 'Name':'Barium', 'origin':'the Greek barys, heavy','mass':'137.327(7)'},
{'Symbol':'La', 'Name':'Lanthanum', 'origin':'the Greek lanthanein, to lie hidden','mass':'138.90547(7)'},
{'Symbol':'Ce', 'Name':'Cerium', 'origin':'the then recently discovered asteroid Ceres, considered a planet at the time','mass':'140.116(1)'},
{'Symbol':'Pr', 'Name':'Praseodymium', 'origin':'the Greek praseios didymos meaning green twin','mass':'140.90766(2)'},
{'Symbol':'Nd', 'Name':'Neodymium', 'origin':'the Greek neos didymos meaning new twin','mass':'144.242(3)'},
{'Symbol':'Pm', 'Name':'Promethium', 'origin':'Prometheus of Greek mythology who stole fire from the Gods and gave it to humans','mass':'145'},
{'Symbol':'Sm', 'Name':'Samarium', 'origin':'Samarskite, the name of the mineral from which it was first isolated','mass':'150.36(2)'},
{'Symbol':'Eu', 'Name':'Europium', 'origin':'Europe','mass':'151.964(1)'},
{'Symbol':'Gd', 'Name':'Gadolinium', 'origin':'Johan Gadolin, chemist, physicist and mineralogist','mass':'157.25(3)'},
{'Symbol':'Tb', 'Name':'Terbium', 'origin':'Ytterby, Sweden','mass':'158.92535(2)'},
{'Symbol':'Dy', 'Name':'Dysprosium', 'origin':'the Greek dysprositos, hard to get','mass':'162.500(1)'},
{'Symbol':'Ho', 'Name':'Holmium', 'origin':'Holmia, the New Latin name for Stockholm','mass':'164.93033(2)'},
{'Symbol':'Er', 'Name':'Erbium', 'origin':'Ytterby, Sweden','mass':'167.259(3)'},
{'Symbol':'Tm', 'Name':'Thulium', 'origin':'Thule, the ancient name for Scandinavia','mass':'168.93422(2)'},
{'Symbol':'Yb', 'Name':'Ytterbium', 'origin':'Ytterby, Sweden','mass':'173.045(10)'},
{'Symbol':'Lu', 'Name':'Lutetium', 'origin':'Lutetia, the Latin name for Paris','mass':'174.9668(1)'},
{'Symbol':'Hf', 'Name':'Hafnium', 'origin':'Hafnia, the New Latin name for Copenhagen','mass':'178.49(2)'},
{'Symbol':'Ta', 'Name':'Tantalum', 'origin':'King Tantalus, father of Niobe from Greek mythology','mass':'180.94788(2)'},
{'Symbol':'W', 'Name':'Tungsten', 'origin':'the Swedish tung sten, heavy stone (W is wolfram, the old name of the tungsten mineral wolframite)[3]','mass':'183.84(1)'},
{'Symbol':'Re', 'Name':'Rhenium', 'origin':'Rhenus, the Latin name for the river Rhine','mass':'186.207(1)'},
{'Symbol':'Os', 'Name':'Osmium', 'origin':'the Greek osme, meaning smell','mass':'190.23(3)'},
{'Symbol':'Ir', 'Name':'Iridium', 'origin':'Iris, the Greek goddess of the rainbow','mass':'192.217(3)'},
{'Symbol':'Pt', 'Name':'Platinum', 'origin':'the Spanish platina, meaning little silver','mass':'195.084(9)'},
{'Symbol':'Au', 'Name':'Gold', 'origin':'English word (aurum in Latin)','mass':'196.966569(5)'},
{'Symbol':'Hg', 'Name':'Mercury', 'origin':'the New Latin name mercurius, named after the Roman god (Hg from former name hydrargyrum, from Greek hydr-, water, and argyros, silver)','mass':'200.592(3)'},
{'Symbol':'Tl', 'Name':'Thallium', 'origin':'the Greek thallos, green twig','mass':'204.389'},
{'Symbol':'Pb', 'Name':'Lead', 'origin':'English word (plumbum in Latin)[3]','mass':'207.2(1)'},
{'Symbol':'Bi', 'Name':'Bismuth', 'origin':'German word, now obsolete','mass':'208.98040(1)'},
{'Symbol':'Po', 'Name':'Polonium', 'origin':'Polonia, the New Latin name for Poland','mass':'209'},
{'Symbol':'At', 'Name':'Astatine', 'origin':'the Greek astatos, unstable','mass':'210'},
{'Symbol':'Rn', 'Name':'Radon', 'origin':'From radium, as it was first detected as an emission from radium during radioactive decay','mass':'222'},
{'Symbol':'Fr', 'Name':'Francium', 'origin':'Francia, the New Latin name for France','mass':'223'},
{'Symbol':'Ra', 'Name':'Radium', 'origin':'the Latin radius, ray','mass':'226'},
{'Symbol':'Ac', 'Name':'Actinium', 'origin':'the Greek aktis, ray','mass':'227'},
{'Symbol':'Th', 'Name':'Thorium', 'origin':'Thor, the Scandinavian god of thunder','mass':'232.0377(4)'},
{'Symbol':'Pa', 'Name':'Protactinium', 'origin':'the Greek protos, first, and actinium, which is produced through the radioactive decay of protactinium','mass':'231.03588(2)'},
{'Symbol':'U', 'Name':'Uranium', 'origin':'Uranus, the seventh planet in the Solar System','mass':'238.02891(3)'},
{'Symbol':'Np', 'Name':'Neptunium', 'origin':'Neptune, the eighth planet in the Solar System','mass':'237'},
{'Symbol':'Pu', 'Name':'Plutonium', 'origin':'Pluto, a dwarf planet in the Solar System','mass':'244'},
{'Symbol':'Am', 'Name':'Americium', 'origin':'The Americas, as the element was first synthesized on the continent, by analogy with europium','mass':'243'},
{'Symbol':'Cm', 'Name':'Curium', 'origin':'Pierre Curie, a physicist, and Marie Curie, a physicist and chemist, named after great scientists by analogy with gadolinium','mass':'247'},
{'Symbol':'Bk', 'Name':'Berkelium', 'origin':'Berkeley, California, where the element was first synthesized, by analogy with terbium','mass':'247'},
{'Symbol':'Cf', 'Name':'Californium', 'origin':'California, where the element was first synthesized','mass':'251'},
{'Symbol':'Es', 'Name':'Einsteinium', 'origin':'Albert Einstein, physicist','mass':'252'},
{'Symbol':'Fm', 'Name':'Fermium', 'origin':'Enrico Fermi, physicist','mass':'257'},
{'Symbol':'Md', 'Name':'Mendelevium', 'origin':'Dmitri Mendeleev, chemist and inventor','mass':'258'},
{'Symbol':'No', 'Name':'Nobelium', 'origin':'Alfred Nobel, chemist, engineer, innovator, and armaments manufacturer','mass':'259'},
{'Symbol':'Lr', 'Name':'Lawrencium', 'origin':'Ernest O. Lawrence, physicist','mass':'266'},
{'Symbol':'Rf', 'Name':'Rutherfordium', 'origin':'Ernest Rutherford, chemist and physicist','mass':'267'},
{'Symbol':'Db', 'Name':'Dubnium', 'origin':'Dubna, Russia','mass':'268'},
{'Symbol':'Sg', 'Name':'Seaborgium', 'origin':'Glenn T. Seaborg, scientist','mass':'269'},
{'Symbol':'Bh', 'Name':'Bohrium', 'origin':'Niels Bohr, physicist','mass':'270'},
{'Symbol':'Hs', 'Name':'Hassium', 'origin':'Hesse, Germany, where the element was first synthesized','mass':'269'},
{'Symbol':'Mt', 'Name':'Meitnerium', 'origin':'Lise Meitner, physicist','mass':'278'},
{'Symbol':'Ds', 'Name':'Darmstadtium', 'origin':'Darmstadt, Germany, where the element was first synthesized','mass':'281'},
{'Symbol':'Rg', 'Name':'Roentgenium', 'origin':'Wilhelm Conrad Rontgen, physicist','mass':'282'},
{'Symbol':'Cn', 'Name':'Copernicium', 'origin':'Nicolaus Copernicus, astronomer','mass':'285'},
{'Symbol':'Uut', 'Name':'Ununtrium', 'origin':'IUPAC systematic element name','mass':'286'},
{'Symbol':'Fl', 'Name':'Flerovium', 'origin':'Georgy Flyorov, physicist','mass':'289'},
{'Symbol':'Uup', 'Name':'Ununpentium', 'origin':'IUPAC systematic element name','mass':'289'},
{'Symbol':'Lv', 'Name':'Livermorium', 'origin':'Lawrence Livermore National Laboratory (in Livermore, California) which collaborated with JINR on its synthesis','mass':'293'},
{'Symbol':'Uus', 'Name':'Ununseptium', 'origin':'IUPAC systematic element name','mass':'294'},
{'Symbol':'Uuo', 'Name':'Ununoctium', 'origin':'IUPAC systematic element name','mass':'294'},

]

print('Element Picker! (Laura Fox is the coolest!)')
includeFBlock = inputWrapper('include f-block? (y/n)')
print('hit ENTER for the next element!')
inputWrapper()

while(True):

    inFblock = False
    atomicIndex = random.randint(0, len(table) - 1)
    if(atomicIndex > 56 and atomicIndex < 71) or (atomicIndex > 88 and atomicIndex < 103):
        inFblock = True
    if(not inFblock or includeFBlock == 'y'):
        print("[{0}] {1} {2} {3} {4}".format(atomicIndex + 1, table[atomicIndex]['Symbol'], table[atomicIndex]['Name'], table[atomicIndex]['mass'],table[atomicIndex]['origin']))
        inputWrapper()
