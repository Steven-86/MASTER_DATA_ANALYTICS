from veg_functions import *

if __name__=="__main__":
	import csv
	import os.path

	if os.path.isfile("database_vegan_shop.csv")==False:
		print("Magazzino non presente, procedo alla creazione di un nuovo deposito")
		with open("database_vegan_shop.csv","w",encoding="utf-8",newline="") as writeFile:
			writer = csv.writer(writeFile)
			csv_header=("PRODOTTO","QUANTITA'","PREZZO_ACQUISTO","PREZZO","SPESE_ACQUISTO","RICAVI_VENDITA")
			writer.writerow(csv_header)
				 
			
	selection=None
	help_options=["aggiungi: aggiungi un prodotto al magazzino","elenca: elenca i prodotto in magazzino","vendita: registra una vendita effettuata","profitti: mostra i profitti totali","aiuto: mostra i possibili comandi","chiudi: esci dal programma"]

	while selection!="chiudi":
		
		selection=input("Inserisci un comando:")
		selection=selection.lower()
		
		if selection=="aggiungi":selection_add()
		elif selection=="elenca":selection_elements()        
		elif selection=="vendita":selection_sales()
		elif selection=="profitti":financial_gain()
		elif selection=="aiuto":
			print("I comandi disponibili sono i seguenti:\n")
			for member in help_options:
				print(f" ● {member} ")
			print("\n")
		elif selection=="chiudi":
			print("Bye bye")           
		else:
			print("Comando non valido\nI comandi disponibili sono i seguenti:")
			for member in help_options:
				print(f" - {member} ")
			
			