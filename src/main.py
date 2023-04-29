#importo numpy pandas e matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

"""converto un file PNG in un matrice di tuple RGB"""
import numpy as np
from PIL import Image

def my_load_image(filename: str) -> np.ndarray:
    img = Image.open(filename)
    return np.array(img)

img=Image.open("data/field_01.png")
print(np.array(img))

"""fine conversione file PNG in una matrice PNG"""




"""converto un file JSON in una lista di liste"""

import json

def my_load_json(filename: str) -> np.ndarray:
  
  with open("filename") as initial_field:
      json_data = json.load(initial_field)
      print(json_data)
      
      rows = json_data['rows']
      cols = json_data['cols']
      food = json_data['food']
      blocks = json_data['blocks']
      
      field = np.zeros((rows, cols, 3), dtype=np.uint8)
      
      
      def stampa_stringa(s: str):
          print(s)
          
      stampa_stringa("field")

    
  pass




"""decido di creare la funzione che accetta una stringa in cui contiene
il file json con il campo da gioco"""

def play(game_file: str) -> int:
   
    #n=1; #lunghezza iniziale del serpente
    
    
    
    class Campo:
        
           "ultimo ragionamento sull'impostazione della funzione"
            #creo una funzione init
    
            def init__(self,campo,ostacoli,cibo,vuoto,serpente,scia):
                self.campo
                self.ostacoli
                self.cibo
                self.vuoto
        
                #campo=np.zeros((4,6)) ho creato la matrice campo
        
        
        
        
        
        
        
            "ragionamento iniziale sull'impostazione della funzione"     
    
            #creo la funzione ostacoli
            
            #def ostacoli(self,blocks):
                #self.blocks
                
                #b.np=([[0,2],[1,1],[3,1]])
  
                #se il serpente non incontra un ostacolo allora il gioco prosegue
                
                #while
    
            #class mossedagioco(moves,start):
        
    
            #class scia(mossedagioco, snake, scia)
    
                #if #mossa è buona 
                    #testa serpente va avanti
                    
                    #if #incontra cibo
                        #"n=n+1;"
                    
                    #else:
                        #return n
        
 pass


#come collego il file json al codice?