#Paulers und Jans Restaurant
import os
import time

#Speisekarte
Speise1 = '1x Döner'
Speise2 = '1 Scheibe Brot'
Speise3 = '20x Tortenstücke'
KostenSpeise1 = 5
KostenSpeise2 = 2.5
KostenSpeise3 = 2000
error = 0

print ('Willkommen in Paulinchens und Jannis Café! \n')
time.sleep(0.5)
Name = input ('Wie heißt du? \n>')
time.sleep(0.5)

def errorcount():
	global error
	error = error + 1
	if error >= 3 :
		print('RAUS AUS MEINEM RESTAURANT, DU TROLL!')
		quit()
	print('Das habe ich nicht verstanden, bitte wiederhole deine Bestellung :)')

def Bestellsystem():
	global Rechnung
	global Gesamtbestellung
	Rechnung = 0
	Gesamtbestellung = []
	while True:
		global Bestellung
		Bestellung = input ('\nWas möchtest du bestellen?\n>')
		Gesamtbestellung.append(Bestellung)
		if Bestellung == Speise1 :
			Rechnung = Rechnung + KostenSpeise1
			Nachfrage = input ('\nAlles klar, willst du noch etwas bestellen?\n>')
			if Nachfrage == 'Ja' :
				continue
			elif Nachfrage == 'Nein' :
				break
			else:
				errorcount()
		elif Bestellung == Speise2 :
			Rechnung = Rechnung + KostenSpeise2
			Nachfrage = input ('\nAlles klar, willst du noch etwas bestellen?\n>')
			if Nachfrage == 'Ja' :
				continue
			elif Nachfrage == 'Nein' :
				break
			else:
				errorcount()
		elif Bestellung == Speise3 :
			Rechnung = Rechnung + KostenSpeise3
			Nachfrage = input ('\nAlles klar, willst du noch etwas bestellen?\n>')
			if Nachfrage == 'Ja' :
				continue
			elif Nachfrage == 'Nein' :
				break
			else:
				errorcount()
		else :
			errorcount()

def Kellner():
	print('\nHallo ' + Name + ', \nWir haben heute folgende Speisen im Angebot: \n- ' + Speise1 + '   ' + str(KostenSpeise1) + '€\n\n- ' + Speise2 + '   ' + str(KostenSpeise2) + '€\n\n- ' + Speise3 + '   ' + str(KostenSpeise3) + '€')
	Bestellsystem()
	clearConsole()
	print ('Hallo ' + Name + ', hier haben wir deine bestellten Speisen: \n')
	print(*Gesamtbestellung, sep = ", ")
	print ('\nDie Rechnung beträgt: ' + str(Rechnung) + '€')
	print ('Wir buchen den Betrag von deinem hinterlegten Konto ab... wir kennen dich ja ;)')
	print ('Danke für deinen Besuch! Auf Wiedersehen!')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
Kellner()

