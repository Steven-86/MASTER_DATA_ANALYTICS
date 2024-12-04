def name_check(msg):
    """
    Given a string with the description of the desired input this function checks if the name is not empty.
    Particular string provide specific output
    This is a recursive function, if the requirements aren't met it keeps asking for the correct input
    """
    
    name_in=input(msg)
    if name_in.strip()=="":
        print("Attenzione inserito un input senza caratteri, riprova!")
        return name_check(msg)
    elif name_in=="0":
        print("Attenzione inserito una stringa 0, riprova!")
        return name_check(msg)
    
    elif msg=="Aggiungere un altro prodotto ? (si/no)":
        if name_in.lower()!="si" and name_in.lower()!="no":
            print("Attenzione, non hai digitato correttamente si/no")
            return name_check(msg)
        else:
            return name_in.lower()
    else:
        return name_in.lower()
    

def int_check(message):
        """
        Given a string with the description of the desired input this functions checks the following conditions:
        -input type equals to int
        -input not zero
        -input not blank
        This is a recursive function, if the requirements aren't met it keeps asking for the correct input
        """
        
        incoming=input(message)
        
        try:
            incoming=int(incoming)
        except:
            print("Attenzione inserito un numero non intero oppure una stringa di caratteri o uno spazio, riprova!")
            return int_check(message)
        
        if incoming<0:
            print("Attenzione inserito un numero negativo, riprova!")
            return int_check(message)
        elif incoming==0:
            print("Attenzione inserito un valore nullo, riprova!")
            return int_check(message)
        else:
            return incoming
        
def float_check(ms):
        """
        Given a string with the description of the desired input this functions checks the following conditions:
        -input type equals to float
        -input not zero
        -input not blank
        This is a recursive function, if the requirements aren't met it keeps asking for the correct input
        """
        
        incom=input(ms)
        
        try:
            incom=float(incom)
        except:
            print("Attenzione inserito un numero non reale oppure una stringa di caratteri o uno spazio, riprova!")
            return float_check(ms)
        
        if incom<0:
            print("Attenzione inserito un numero negativo, riprova!")
            return float_check(ms)
        elif incom==0:
            print("Attenzione inserito un valore nullo, riprova!")
            return float_check(ms)
        else:
            return incom



def product_data():
    """
    This function collects product info and returns a dictionary with the following structure:
    Dictionary_product[product_name]=[product_quantity,product_purchase_price,product_sales_price,purchase_expense,sales_revenue]
    """
        
    product_name= name_check("Nome del prodotto:")
    product_quantity=int_check("Quantità:")
    product_purchase_price=float_check("Prezzo di acquisto:")       
    product_sales_price=float_check("Prezzo di vendita:")

    product_purchase_expenses=float(product_quantity)*product_purchase_price
    product_entry={product_name:[product_quantity,product_purchase_price,product_sales_price,product_purchase_expenses,0]}

    return product_entry

    


def selection_add():
    """
    This function checks if the product has alredy been entered. In that case quantity and purchase account are updated
    Othewise it adds the product to the database
    """
    import csv
    
    product_in_stock=False      
    product_info=product_data()
    product_name, product_details = list(product_info.items())[0]
    lines = list()

    with open("database_vegan_shop.csv","r",encoding="utf-8") as read_file:
        reader = csv.reader(read_file)
        
        for i,row in enumerate(reader):
            
            for field in row:
                if field == product_name:
                    quantity_update=int(row[1])+int(product_details[0])
                    del row[1]
                    row.insert(1,quantity_update)
                    purchase_count_update=(float(row[1])*float(row[2]))+float(row[-2])
                    del row[4]
                    row.insert(4,purchase_count_update)
                    sales_count_update=float(row[-1])
                    del row[-1]
                    row.insert(5,sales_count_update)
                    product_in_stock=True
                
            lines.append(row)
        
        if product_in_stock==False:
            new_product=[]
            new_product.append(product_name)
            new_product.append(product_details[0])
            new_product.append(product_details[1])
            new_product.append(product_details[2])
            new_product.append(product_details[3])
            new_product.append(product_details[4])
            lines.append(new_product)
                        
        new_list = list(filter(None, lines))

    with open("database_vegan_shop.csv","w+",encoding="utf-8",newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(new_list)
        
        print(f"AGGIUNTO:{product_details[0]} X {product_name}")
        

def selection_elements():
    """
    This functions shows the product currently on stock
    """
    import csv
    
    with open("database_vegan_shop.csv","r",encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
        intestazione="PRODOTTO QUANTITA' PREZZO"
        print(intestazione)
        for row in csv_reader:
            prod=row["PRODOTTO"]
            quan=row["QUANTITA'"]
            pric=row["PREZZO"]
            print(f"{prod} {quan} €{float(pric):.2f}")
            
def stock_verification():
    """
    This functions check if there is still some stock available to sales, return True or False
    """
    import csv
    
    with open("database_vegan_shop.csv","r",encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            stock_for_sales=False
            for row in csv_reader:
                if row[1]!="0" and row[1]!="QUANTITA'":stock_for_sales=True
            
            if stock_for_sales==False:print("Non c'è giacenza di prodotti disponibili per la vendita")
            
            return stock_for_sales

            
            
def selection_sales():
    """
    This function records sales on the database
    """
    import csv
    shopping_fever=stock_verification()
    billed_products=[]
        
    while shopping_fever==True:
        
        with open("database_vegan_shop.csv","r",encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            
            request_verification=False
                       
            while request_verification==False:
                p_name=name_check("Nome del prodotto:")
                p_qty=int_check("Quantità:")
                sales_request=[p_name,p_qty]
                request_verification=sales_check(sales_request)
            
            lines=[]
                                                      
            for row in csv_reader:
                
                for field in row:
                    if field == p_name:
                        sales_amount=0
                        stock_row=0                        
                        sales_amount=float(row[5])
                        stock_row=int(row[1])
                        sales_amount+=p_qty*float(row[3])
                        del row[-1]
                        row.insert(5,sales_amount)
                        stock_row-=p_qty
                        del row[1]
                        row.insert(1,stock_row)
                        billed_products.append([p_name,p_qty,float(row[3])])
                        
                lines.append(row)

        with open("database_vegan_shop.csv","w+",encoding="utf-8",newline="") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

       
        choice=name_check("Aggiungere un altro prodotto ? (si/no)")
                      
        if stock_verification()==False and choice!="no":
            print("Spicenti, abbiamo esaurito tutta la giacenza dei prodotti, precediamo a registrare la vendita")            
            choice="no"
        
        if choice=="no":
            print("VENDITA REGISTRATA")
            tot_order=0.0
            for line in billed_products:
                tot_order+=float(line[1])*float(line[2])
                print(f"{line[1]} X {line[0]}: €{line[2]:.2f}")
            
            print(f"Totale:€{tot_order:.2f}")
            shopping_fever=False
        

    
def sales_check(sales_request):
    """
    This function examine the sales_request :verifies if the product is in the database, and if the quantity is enough
    """
    import csv
    article=sales_request[0]        
    count_article=sales_request[1]

    with open("database_vegan_shop.csv","r",encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            article_in_database=False
            for row in csv_reader:

                for field in row:

                    if field == article:
                        article_in_database=True
                        if int(row[1])>=count_article:
                            return True
                        else:
                            print(f"Giacenza del prodotto {article} insufficiente per soddisfare richiesta")
                            print("I prodotti attualmente in giacenza sono i seguenti")
                            selection_elements()
                            return False

            if article_in_database==False:
                print(f"Prodotto {article} non in magazzino")
                return False
        
    
def financial_gain():
    """
    This functions calulate the financial gains of our vegan shop
    """
    import csv
    
    with open("database_vegan_shop.csv","r",encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        tot_sales=0.0
        tot_purchase=0.0
        
        for row in csv_reader:
            if row[0]!="PRODOTTO":
                tot_sales+=float(row[-1])
                tot_purchase+=float(row[-2])
        
        print(f"Profitto: lordo=€{tot_sales:.2f} netto=€{(tot_sales-tot_purchase):.2f}")

