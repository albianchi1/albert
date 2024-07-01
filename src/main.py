#importo numpy pandas e matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#converto un file PNG in un matrice di tuple RGB
from PIL import Image

def my_load_image(filename: str) -> np.ndarray:
    img = Image.open(filename)
    return np.array(img)

img=Image.open("data/field_01.png")
print(np.array(img))

#fine conversione file PNG in una matrice PNG




#converto un file JSON in una lista di liste

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
         
#fine conversione di un file JSON in una lista di liste

#creo la classe snake

class snake:
    def __init__(self,start,field):
        
        self.testa=start
        
        self.field=field
        
        self.coda=[]
        
        self.scia=[]
        
      #il metodo go accetta una stringa (posso eliminare il while)  
      #il metodo go restituisce un metodo booleano che indica se il serpente è andato a sbattere
    def go(move):
        if mossa is "N" :
                
            testa[0]= testa[0]-1
            
                
            if self.field.block_in(testa):
                return False
            
            
                    
            if self.field.food_in(testa):
                
                coda.append(testa[0]+1)
                
                
                
            
            
                
            elif mossa is "S" : 
                
                testa[0]= testa[0]+1
                
                if self.field.block_in(testa):
                    return False
                
                if self.field.food_in(testa):
                    #aggiorno testa,coda e scia del serpente
                    
                
            elif mossa is "E" :
                
                testa[1]= testa[1]+1
                
                if self.field.block_in(testa):
                    return False
                
                if self.field.food_in(testa):
                    #aggiorno testa, coda e scia del serpente
                    
            elif mossa is "W" :
                
                testa[1]= testa[1]-1
                
                if self.field.block_in(testa):
                    return False
                
                if self.field.food_in(testa):
                    #aggiorno testa, coda e scia del serpente
                    
            elif mossa is "NW" :
                
                
                testa[0]= testa[0]-1
                
                testa[1]= testa[1]-1
                
                if self.field.block_in(testa):
                    return False
                
                if self.field.food_in(testa):
                    #aggiorno testa coda e scia del serpente
                    
            elif mossa is "NE" :
                
                testa[0]= testa[0]-1
                
                testa[1]= testa[1]+1
                
                if self.field.block_in(testa):
                    return False
                
                if self.field.food_in(testa):
                    #aggiorno testa coda e scia del serpente
                    
            elif mossa is "SW" :
                
                testa[0]= testa[0]+1
                
                testa[1]= testa[1]-1
                
                if self.field.block_in(testa):
                    return False
                
                if self.field.food_in(testa):
                    #aggiorno testa coda e scia del serpente
                    
            elif mossa is "SE" :
                
                testa[0]= testa[0]+1
                
                testa[1]= testa[1]+1
                
                if self.field.block_in(testa):
                    return False
                
                if self.field.food_in(testa):
                    #aggiorno testa coda e scia del serpente
                    
                
            else:
                 
                 return False
             
                
             
             
            
        
    


#inizio a scrivere la funzione play


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
            my_load_image(field_in)
            
            
            
        elif field_in.endswith('.json'):
            my_load_json(field_in)


        
        
  
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
        

    
    
        
#
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

