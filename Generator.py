import random


names = ["Adel", "Adonis", "Ajaz", "Akos", "Aldo", "Amets", "Amaro", "Aquiles", "Algimantas", "Alpidio", "Amrane", "Anish", "Arián", "Ayun", "Azariel", "Bagrat", "Bencomo", "Bertino", "Candi", "Cesc", "Cirino", "Crisólogo", "Cruz", "Danilo", "Dareck", "Dariel", "Darin", "Delmiro", "Damen", "Dilan", "Dipa", "Doménico", "Drago", "Edivaldo", "Elvis", "Elyan", "Emeric", "Engracio", "Ensa", "Eñaut", "Eleazar", "Eros", "Eufemio", "Feiyang", "Fiorenzo", "Foudil", "Galo", "Gastón", "Giulio", "Gautam", "Gentil", "Gianni", "Gianluca", "Giorgio", "Gourav", "Grober", "Guido", "Guifre", "Guim", "Hermes", "Inge", "Irai", "Iraitz", "Iyad", "Iyán", "Jeremías", "Joao", "Jun", "Khaled", "Leónidas", "Lier", "Lionel", "Lisandro", "Lucián", "Mael", "Misael", "Moad", "Munir", "Nael", "Najim", "Neo", "Neil", "Nikita", "Nilo", "Otto", "Pep", "Policarpo", "Radu", "Ramsés", "Rómulo", "Roy", "Severo", "Sidi", "Simeón", "Taha", "Tao", "Vadim", "Vincenzo", "Zaid", "Zigor", "Zouhair"]

last_name = ["Adel", "Adonis", "Ajaz", "Akos", "Aldo", "Amets", "Amaro", "Aquiles", "Algimantas", "Alpidio", "Amrane", "Anish", "Arián", "Ayun", "Azariel", "Bagrat", "Bencomo", "Bertino", "Candi", "Cesc", "Cirino", "Crisólogo", "Cruz", "Danilo", "Dareck", "Dariel", "Darin", "Delmiro", "Damen", "Dilan", "Dipa", "Doménico", "Drago", "Edivaldo", "Elvis", "Elyan", "Emeric", "Engracio", "Ensa", "Eñaut", "Eleazar", "Eros", "Eufemio", "Feiyang", "Fiorenzo", "Foudil", "Galo", "Gastón", "Giulio", "Gautam", "Gentil", "Gianni", "Gianluca", "Giorgio", "Gourav", "Grober", "Guido", "Guifre", "Guim", "Hermes", "Inge", "Irai", "Iraitz", "Iyad", "Iyán", "Jeremías", "Joao", "Jun", "Khaled", "Leónidas", "Lier", "Lionel", "Lisandro", "Lucián", "Mael", "Misael", "Moad", "Munir", "Nael", "Najim", "Neo", "Neil", "Nikita", "Nilo", "Otto", "Pep", "Policarpo", "Radu", "Ramsés", "Rómulo", "Roy", "Severo", "Sidi", "Simeón", "Taha", "Tao", "Vadim", "Vincenzo", "Zaid", "Zigor", "Zouhair"]

chair_letters = ['A', 'B', 'C', 'H', 'J', 'K']

def random_name():
  name_passenger = f'{random.choice(names)} {random.choice(last_name)}'
  return name_passenger

def assignment():
  row = random.randint(5, 27)
  col = random.choice(chair_letters)
  return (row, col)

def location(row, col):
  diC = {"A":0, "B":1, "C":2, "H":3, "J":4, "K":5}
  y = diC[col]
  x = row - 5
  return (x,y)  


