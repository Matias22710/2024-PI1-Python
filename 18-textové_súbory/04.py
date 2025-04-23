import random

# Zoznamy mien a priezvisk
names = [
    "Adam", "Adolf", "Adrián", "Alan", "Albert", "Albín", "Aleš", "Alex", "Alexander", "Alexej",
    "Alfonz", "Alfréd", "Alojz", "Ambróz", "Andrej", "Anton", "Ariel", "Arnold", "Áron", "Arpád",
    "Atila", "Augustín", "Aurel", "Bartolomej", "Belo", "Beňadik", "Benedikt", "Benjamín", "Bernard",
    "Blahoslav", "Blažej", "Bohdan", "Bohumil", "Bohumír", "Bohuslav", "Bohuš", "Boleslav", "Bonifác",
    "Boris", "Branislav", "Bruno", "Bystrík", "Ctibor", "Cyprián", "Cyril", "Dalibor", "Daniel", "Dávid",
    "Demeter", "Denis", "Dezider", "Dionýz", "Dobroslav", "Dominik", "Drahomír", "Drahoslav", "Dušan",
    "Eder", "Edmund", "Eduard", "Eliáš", "Emanuel", "Emil", "Erik", "Ernest", "Ervín", "Eugen", "Fedor",
    "Félix", "Ferdinand", "Filip", "Florián", "František", "Frederik", "Fridrich", "Gabriel", "Gašpar",
    "Gejza", "Gregor", "Gustáv", "Henrich", "Herbert", "Hubert", "Hugo", "Ignác", "Igor", "Iľja", "Imrich",
    "Ivan", "Izidor", "Jakub", "Ján", "Jarolím", "Jaromír", "Jaroslav", "Jerguš", "Jerry", "Jonáš", "Jozef",
    "Július", "Juraj", "Kamil", "Karol", "Kazimír", "Klement", "Kliment", "Koloman", "Konštantín", "Kornel",
    "Kristián", "Krištof", "Kvetoslav", "Ladislav", "Leonard", "Leopold", "Levoslav", "Libor", "Ľubomír",
    "Ľubor", "Ľuboslav", "Ľuboš", "Ludolf", "Ľudomil", "Ľudovít", "Lukáš", "Marcel", "Marek", "Marián", "Mário",
    "Maroš", "Martin", "Matej", "Matúš", "Maximilián", "Medard", "Melichar", "Metod", "Michal", "Mikuláš",
    "Milan", "Miloslav", "Miloš", "Miroslav", "Mojmír", "Móric", "Nathan", "Nikola", "Norbert", "Odin", "Oldrich",
    "Oliver", "Ondrej", "Oskár", "Oto", "Pankrác", "Paolo", "Patrik", "Pavol", "Peter", "Pravoslav", "Prokop",
    "Radomír", "Radoslav", "Radovan", "Radúz", "Rastislav", "René", "Richard", "Rishi", "Róbert", "Roland",
    "Roman", "Rudolf", "Samuel", "Sebastián", "Sergej", "Servác", "Seth", "Severín", "Silvester", "Slavomír",
    "Stanislav", "Svätopluk", "Svetozár", "Šimon", "Štefan", "Tadeáš", "Tarzícius", "Teodor", "Tibor", "Tichomír",
    "Timotej", "Tobiáš", "Tomáš", "Urban", "Václav", "Valentín", "Valér", "Vasil"
]

surnames = [
    "Adam", "Achberger", "Andráš", "Andrašík", "Andrášik", "Antal", "Babjak", "Babka", "Bača", "Bahna", 
    "Bahno", "Baláž", "Bán", "Baňa", "Baňas", "Baňo", "Baran", "Baranka", "Barbora", "Barok", "Bárta", 
    "Bartoš", "Bartošík", "Bartovič", "Baša", "Baška", "Baško", "Bašo", "Bednár", "Bednárik", "Beka", 
    "Beňa", "Beňo", "Beňuš", "Beňuška", "Bernard", "Bernolák", "Bezák", "Bicek", "Bielik", "Bilek", "Bilka", 
    "Bilko", "Blaha", "Blaho", "Blažej", "Bobula", "Bobuľa", "Bondra", "Borek", "Borík", "Bórik", "Borik", 
    "Boris", "Boriš", "Borka", "Borko", "Borovský", "Borový", "Bosák", "Boška", "Bošňák", "Bôrik", "Brezina",
    "Brunovský", "Bruška", "Bruško", "Bukovský", "Capek", "Capka", "Capko", "Centek", "Cesnak", "Cibula", 
    "Cibuľa", "Cibulka", "Cibuľka", "Cigán", "Cigáň", "Cigánik", "Cíger", "Cyprich", "Čapka", "Čapko", "Čapkovič", 
    "Čapla", "Čapľa", "Čaplovič", "Čarnogurský", "Čekovský", "Černík", "Černoch", "Červeň", "Červený", 
    "Česnek", "Čiernik", "Čierny", "Čobrda", "Ďaďo", "Dán", "Daňa", "Dancák", "Dančák", "Dančiak", "Danek", 
    "Danko", "Daňko", "Dano", "Daňo", "Dávid", "Deák", "Debnár", "Dej", "Dekýš", "Devečka", "Dobšinský", 
    "Dočolomanský", "Doležal", "Dora", "Dorka", "Dorko", "Ďorko", "Dorot", "Dorota", "Drajna", "Drobný", 
    "Droppa", "Drotár", "Dubnička", "Dubovský", "Duda", "Dudek", "Dudik", "Dudík", "Dudka", "Dudko", "Dudo", 
    "Dudok", "Dula", "Dulla", "Ďurča", "Ďurčo", "Durdík", "Ďurek", "Ďurica", "Ďuriš", "Ďurka", "Ďurko", 
    "Ďurkovič", "Ďurkovský", "Ďuro", "Ďurovič", "Ďurovský", "Dusík", "Duska", "Dusko", "Duša", "Dušek", 
    "Dušička", "Duška", "Dúška", "Duško", "Ďuško", "Dutka", "Ďutka", "Dutko", "Dvonč", "Dvorský", "Dzurjanin"
]

# Funkcia, ktorá náhodne priradí meno a priezvisko
def generate_random_name():
    first_name = random.choice(names)
    last_name = random.choice(surnames)
    return f"{first_name} {last_name}"

# Generovanie a zobrazenie náhodného mena
print(generate_random_name())