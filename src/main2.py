# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:27:36 2024

@author: alber
"""

import numpy as np

"""converto un file PNG in una matrice"""

from PIL import Image

def my_load_image(filename: str) -> np.ndarray:
    img = Image.open(filename)
    return np.array(img)

img=Image.open("data/field_01.png")
print(np.array(img))


""" fine conversione file PNG in una matrice """


""" converto un file JSON in una matrice """

import json

def my_load_json(filename: str) -> np.ndarray:
  
  with open(filename) as initial_field:
      json_data = json.load(initial_field)
      print(json_data)
      
      rows = json_data['rows']
      cols = json_data['cols']
      food = json_data['food']
      blocks = json_data['blocks']
      
      field = np.zeros((rows, cols, 3), dtype=np.uint8)
      
      
      for [x,y] in food:
          field[x][y]=(255,128,0)
          
      for [x,y] in blocks:
          field[x][y]=(255,0,0)
          
  return field

""" fine conversione file JSON in una matrice """


#esempio di come viene se richiamo la funzione con un dei file json
print(my_load_json("data/field_02.json"))


"""creo la classe snake"""

class snake:
    def __init__(self,start,field):
        
        self.testa=start
        
        self.field=field
        
        self.coda=[]
        
        self.scia=[]
        
        
    """"il metodo go restituisce un metodo booleano che indica se il serpente è ancora in gioco"""
      
    def go(self, move):
        
        if move == "N" :
               
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]-1, self.testa[1])
            
            """controllo se la nuova Testa del serpente ha incontrato un blocco in quel caso finire il gioco
            restituendo il valore booleano False"""
            
            if self.field.block_in(nuovaTesta):
                return False
            
            #altrimenti vedo se il serpente ha incontrato del cibo lungo il percorso, se si aggiornare testa, coda e scia del serpente

            elif self.field.food_in(self.testa): 
                            
                self.coda.append(self.testa)

                self.testa=nuovaTesta    
                
            #eseguo condizione tale per cui se il serpente oltrepassa la fine del campo da gioco riappare dall'altra parte del campo
                

            else:
               
               """se il serpente ha solo la testa aggiorno la scia e la testa del serpente""" 
               
               if self.coda==[]:
                
                   self.scia.append(self.testa)
                
                   self.testa=nuovaTesta
                   
               #altrimenti aggiornare coda,testa e scia del serpente
             
               else:
                
                   self.coda.append(self.testa)
                
                   self.scia.append(self.coda[0])
                
                   self.coda=self.coda[1:]
                
                   self.testa=nuovaTesta
                   
           
        elif move == "S":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]+1, self.testa[1])
            
            """controllo se la nuova Testa del serpente ha incontrato un blocco in quel caso finire il gioco
            restituendo il valore booleano False"""
            
            if self.field.block_in(nuovaTesta):
                return False
            
            #altrimenti vedo se il serpente ha incontrato del cibo lungo il percorso, se si aggiornare testa, coda e scia del serpente

            elif self.field.food_in(self.testa): 
                            
                self.coda.append(self.testa)
                            
                self.testa=nuovaTesta                 
                

            else:
               
               """se il serpente ha solo la testa aggiorno la scia e la testa del serpente""" 
               
               if self.coda==[]:
                
                   self.scia.append(self.testa)
                
                   self.testa=nuovaTesta
                   
               #altrimenti aggiornare coda,testa e scia del serpente
             
               else:
                
                   self.coda.append(self.testa)
                
                   self.scia.append(self.coda[0])
                
                   self.coda=self.coda[1:]
                
                   self.testa=nuovaTesta
                   
           
        elif move == "E":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0], self.testa[1]+1)
            
            """controllo se la nuova Testa del serpente ha incontrato un blocco in quel caso finire il gioco
            restituendo il valore booleano False"""
            
            if self.field.block_in(nuovaTesta):
                return False
            
            #altrimenti vedo se il serpente ha incontrato del cibo lungo il percorso, se si aggiornare testa, coda e scia del serpente

            elif self.field.food_in(self.testa): 
                            
                self.coda.append(self.testa)
                            
                self.testa=nuovaTesta                 
                

            else:
               
               """se il serpente ha solo la testa aggiorno la scia e la testa del serpente""" 
               
               if self.coda==[]:
                
                   self.scia.append(self.testa)
                
                   self.testa=nuovaTesta
                   
               #altrimenti aggiornare coda,testa e scia del serpente
             
               else:
                
                   self.coda.append(self.testa)
                
                   self.scia.append(self.coda[0])
                
                   self.coda=self.coda[1:]
                
                   self.testa=nuovaTesta
                   
                   
        elif move == "W":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0], self.testa[1]-1)
            
            """controllo se la nuova Testa del serpente ha incontrato un blocco in quel caso finire il gioco
            restituendo il valore booleano False"""
            
            if self.field.block_in(nuovaTesta):
                return False
            
            #altrimenti vedo se il serpente ha incontrato del cibo lungo il percorso, se si aggiornare testa, coda e scia del serpente

            elif self.field.food_in(self.testa): 
                            
                self.coda.append(self.testa)

                self.testa=nuovaTesta                 
                

            else:
               
               """se il serpente ha solo la testa aggiorno la scia e la testa del serpente""" 
               
               if self.coda==[]:
                
                   self.scia.append(self.testa)
                
                   self.testa=nuovaTesta
                   
               #altrimenti aggiornare coda,testa e scia del serpente
             
               else:
                
                   self.coda.append(self.testa)
                
                   self.scia.append(self.coda[0])
                
                   self.coda=self.coda[1:]
                
                   self.testa=nuovaTesta
            
           
        elif move == "NW":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]-1,self.testa[1]-1)
            
            """controllo se la nuova Testa del serpente ha incontrato un blocco in quel caso finire il gioco
            restituendo il valore booleano False"""
            
            if self.field.block_in(nuovaTesta):
                return False
            
            #altrimenti vedo se il serpente ha incontrato del cibo lungo il percorso, se si aggiornare testa, coda e scia del serpente

            elif self.field.food_in(self.testa): 
                            
                self.coda.append(self.testa)

                self.testa=nuovaTesta                 
                

            else:
               
               """se il serpente ha solo la testa aggiorno la scia e la testa del serpente""" 
               
               if self.coda==[]:
                
                   self.scia.append(self.testa)
                
                   self.testa=nuovaTesta
                   
               #altrimenti aggiornare coda,testa e scia del serpente
             
               else:
                
                   self.coda.append(self.testa)
                
                   self.coda.append(self.testa)
                
                   self.coda=self.coda[1:]
                
                   self.testa=nuovaTesta
                   
           
        elif move == "NE":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]-1,self.testa[1]+1) 
            
            """controllo se la nuova Testa del serpente ha incontrato un blocco in quel caso finire il gioco
            restituendo il valore booleano False"""
            
            if self.field.block_in(nuovaTesta):
                return False
            
            #altrimenti vedo se il serpente ha incontrato del cibo lungo il percorso, se si aggiornare testa, coda e scia del serpente

            elif self.field.food_in(self.testa): 
                            
                self.coda.append(self.testa)

                self.testa=nuovaTesta                 
                

            else:
               
               """se il serpente ha solo la testa aggiorno la scia e la testa del serpente""" 
               
               if self.coda==[]:
                
                   self.scia.append(self.testa)
                
                   self.testa=nuovaTesta
                   
               #altrimenti aggiornare coda,testa e scia del serpente
             
               else:
                
                   self.coda.append(self.testa)
                
                   self.scia.append(self.coda[0])
                
                   self.coda=self.coda[1:]
                
                   self.testa=nuovaTesta
                   
                   
           
        elif move == "SW":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]+1,self.testa[1]-1)
            
            """controllo se la nuova Testa del serpente ha incontrato un blocco in quel caso finire il gioco
            restituendo il valore booleano False"""
            
            if self.field.block_in(nuovaTesta):
                return False
            
            #altrimenti vedo se il serpente ha incontrato del cibo lungo il percorso, se si aggiornare testa, coda e scia del serpente

            elif self.field.food_in(self.testa): 
                            
                self.coda.append(self.testa)

                self.testa=nuovaTesta                 
                

            else:
               
               """se il serpente ha solo la testa aggiorno la scia e la testa del serpente""" 
               
               if self.coda==[]:
                
                   self.scia.append(self.testa)
                
                   self.testa=nuovaTesta
                   
               #altrimenti aggiornare coda,testa e scia del serpente
             
               else:
                
                   self.coda.append(self.testa)
                
                   self.scia.append(self.coda[0])
                
                   self.coda=self.coda[1:]
                
                   self.testa=nuovaTesta
                   
                   
           
        elif move == "SE":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]+1, self.testa[1]+1)
            
            """controllo se la nuova Testa del serpente ha incontrato un blocco in quel caso finire il gioco
            restituendo il valore booleano False"""
            
            if self.field.block_in(nuovaTesta):
                return False
            
            #altrimenti vedo se il serpente ha incontrato del cibo lungo il percorso, se si aggiornare testa, coda e scia del serpente

            elif self.field.food_in(self.testa): 
                            
                self.coda.append(self.testa)

                self.testa=nuovaTesta                 
                

            else:
               
               """se il serpente ha solo la testa aggiorno la scia e la testa del serpente""" 
               
               if self.coda==[]:
                
                   self.scia.append(self.testa)
                
                   self.testa=nuovaTesta
                   
               #altrimenti aggiornare coda,testa e scia del serpente
             
               else:
                
                   self.coda.append(self.testa)
                
                   self.scia.append(self.coda[0])
                
                   self.coda=self.coda[1:]
                
                   self.testa=nuovaTesta
                   
                   
           
        else:
            
            return False
        
        
        
            
            
           

              

             

def play(game_file: str) -> int:
    with open(game_file) as gamefile:
        jsondata = json.load(gamefile)
        print(jsondata)
        
        field_in = jsondata["field_in"]
        start = jsondata["start"]
        moves = jsondata["moves"]
        field_out = jsondata["field_out"]


        #vedo l'estensione del file field_in se PNG o JSON
    
        if field_in.endswith('.png'):
            
            field=my_load_image("data/field_01.png") #richiamo la funzione my_load_image
            
            serpente= snake(start, field)  
            
            for move in moves:
                
                serpente.go(move)  #da rivedere (passo le mosse al metodo go della classe snake)
            
            
            
            
        elif field_in.endswith('.json'):
            
            field=my_load_json("data/field_01.json") #richiamo la funzione my_load_json
            
            serpente= snake(start,field)
            
            for move in moves:
                
                serpente.go(move)  #da rivedere (passo le mosse al metodo go della classe snake)
            



















