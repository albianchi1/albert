# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 09:27:36 2024

@author: alber
"""

import numpy as np

"""converto un file PNG in una matrice"""

from PIL import Image

def my_load_image(filename: str) -> (np.ndarray,dict):
    img = Image.open(filename)
    arr=np.array(img)
    print(arr)
    ret={"rows": 0, "cols": 0,"food":[],"blocks":[]}
    ret["rows"]=arr.shape[0]
    ret["cols"]=arr.shape[1]
    for x in range(ret["rows"]):
        for y in range(ret["cols"]):         
            if arr[x,y]==(255,128,0):           #chiedere se arr è una matrice con già tutto impostato con colori dei rispettivi
                ret["food"].append([x,y])       #elementi necessari
            elif arr[x,y]==(255,0,0):
                ret["blocks"].append([x,y])
    return arr, ret


""" fine conversione file PNG in una matrice """


""" converto un file JSON in una matrice """

import json

def my_load_json(filename: str) -> (np.ndarray,dict):
  
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
          
  return field, json_data

""" fine conversione file JSON in una matrice """


#esempio di come viene se richiamo la funzione con un dei file json
print(my_load_json("data/field_02.json"))


"""creo la classe snake"""

class snake:
    def __init__(self,start,field,json_data):
        
        self.testa=start
        
        self.field=field
        
        self.json_data=json_data
        
        self.coda=[]
        
        self.scia=[]
    
        self.len_serpente=0
    
    def spostamento(self, nuovaTesta):
        #contrallare che la testa sia uscita dal campo di gioco
        
        #la x della nuovaTesta deve essere maggiore di 0 e minore di row
        
        #se la x della nuovaTesta se è maggiore di rows la riporto a zero
        
        #se la x della nuovaTesta è minore di zero la riporto a rows -1
        
        #la y della nuovaTesta deve essere maggiore di 0 e minore di cols
        
        #se la y della nuovaTesta se è maggiore di cols la riporto a zero
        
        #se la y della nuovaTesta è minore di zero la riporto a cols -1
        
        
        if nuovaTesta[0]> (self.json_data["rows"]): #si può effettuare questo passaggio se la variabile field è contenuta nel costruttore?
                nuovaTesta[0]=0
                
        elif nuovaTesta[0]< 0:
            nuovaTesta[0]= (self.json_data["rows"]) -1
            
        if nuovaTesta[1]> (self.json_data["cols"]):
            nuovaTesta[1]=0
            
        elif nuovaTesta[1]< 0:
            nuovaTesta[1]= (self.json_data["cols"]) -1
            
        
        
        

    
        #controllare se la testa ha incontrato un blocco if [x,y] in json_data["blocks"]
        
        if nuovaTesta in self.json_data["blocks"]:
            return False


        
        #controllare se la testa ha incontrato del cibo if [x,y] in json_data["food"]
        
        if nuovaTesta in self.json_data["food"]:
            self.len_serpente+=1
                
        #controllare se la testa ha incontrato il corpo del serpente primo controllo, [x,y] sono dentro la coda  
        
        if nuovaTesta in self.coda:
            return False
            
        #secondo controllo, [x,y] hanno attraversato la coda del serpente  
        
        collo= self.testa
        
        controllo1= [nuovaTesta[0], collo[1]]
        controllo2= [collo[0],nuovaTesta[1]]
        
        if controllo1 in self.coda and controllo2 in self.coda:
            return False
        
        self.coda.append(self.testa)
                 
        
        if len(self.coda)> self.len_serpente:
            
            self.scia.append(self.coda[0])
            
            self.coda.pop(0)    #chiedere a che serve questa condizione
        
        self.testa=nuovaTesta
        
        return True
        
    
    """"il metodo go restituisce un metodo booleano che indica se il serpente è ancora in gioco"""
      
    
    
    def go(self, move):
        
        if move == "N" :
               
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=[self.testa[0]-1, self.testa[1]]
                   
           
        elif move == "S":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]+1, self.testa[1])
            
           
        elif move == "E":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0], self.testa[1]+1)
            
                   
        elif move == "W":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0], self.testa[1]-1)
           
            
        elif move == "NW":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]-1,self.testa[1]-1)
            
           
        elif move == "NE":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]-1,self.testa[1]+1) 
            
           
        elif move == "SW":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]+1,self.testa[1]-1)
            
           
        elif move == "SE":
            
            """aggiorno nuovaTesta del serpente (ovvero la nuova "casella" dove si è spostato il serpente)"""
            
            nuovaTesta=(self.testa[0]+1, self.testa[1]+1)
            
           
        else:
            
            return False
        
        codice_uscita=self.spostamento(nuovaTesta)
        
        
        return codice_uscita
            
    def disegna_field(self):
        
        for [x,y] in self.scia:
            
            self.field[x][y]=(128,128,128)
            
        for [x,y] in self.coda:
            
            self.field[x][y]=(0,255,0)
        
        self.field[self.testa[0]][self.testa[1]]=(0,255,0)
        
        
        return self.field
           

              

             

def play(game_file: str) -> int:
    with open(game_file) as gamefile:
        game_data = json.load(gamefile)
        print(game_data)
        
        field_in = game_data["field_in"]
        start = game_data["start"]
        moves = game_data["moves"]
        field_out = game_data["field_out"]


        #vedo l'estensione del file field_in se PNG o JSON
    
        if field_in.endswith('.png'):
            
            field, json_data=my_load_image(field_in) #richiamo la funzione my_load_image
            
            
            
        elif field_in.endswith('.json'):
            
            field, json_data=my_load_json(field_in) #richiamo la funzione my_load_json
            
        
       
        serpente= snake(start,field,json_data)
        
        for move in moves:
            
            stato=serpente.go(move)    #da rivedere (passo le mosse al metodo go della classe snake)
        
            if not stato:
                
                break
            
        nuovo_field=serpente.disegna_field()
        
        
        return field



        










gioco2=play("data/gamefile_02.json")
print(gioco2)













