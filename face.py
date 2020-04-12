import cv2,time,os #moduli utilizzati

numeroFoto=len(os.listdir("."))-3 #per non sovrascrivere le foto fatte precedentemente contando il numero di file nella cartella -3(.py,.xml,.rar)
video=cv2.VideoCapture(0)#creo l'oggetto video 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #importo xml che riconosce le facce
volto=numeroFoto #primo nome in formato numerico delle prossime foto
tempo=int(time.time())+6 #prossimi 6 sec
tempoFaccia=int(time.time())+3#prossimi 3 sec

while True: 
    
    
    check, frame = video.read() #catturo un frame dalla fotocamera
    
    contr=cv2.waitKey(1) #mostro i frame ogni millisecondo
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #bianco e nero per facilitare il rilevamento facciale 
   
    faccia = face_cascade.detectMultiScale(gray, 1.3, 5)#salvo le facce nella foto in una lista

            
    if tempoFaccia==int(time.time()): #ogni qual volta che passano 3 secondi
        tempoFaccia=int(time.time())+3 #incremento i secondi da attendere
        if len(faccia)==0: #se non ha rilevato facce
            print("nessun volto rilevato ")
        else:  #se ha rilevato facce
            print("volti rilevati: "+str(len(faccia))) #stampa il numero di facce trovate

    if tempo==int(time.time()): #ogni 6 secondi
            tempo=int(time.time())+6 #incremento i secondi da attendere
            if len(faccia)!=0: #se ci sono facce nello schermo
                cv2.imwrite("volto_%d.jpg" % volto, frame) #cattura il frame e lo salvo
                volto+=1#devi fare in modo che la foto la faccia dopo un delay tra un volto e l'altro e non per ogni volto rilevato, senza ridurre i frame della webcam. TROPPE FOTO
                print("foto effettuate: "+str(volto)) #foto salvate  

    
    for (x,y,w,h) in faccia: # per disegnare un rettangolo sulla faccia 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(72, 254, 14),2) 
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w]
    
    
    
    cv2.imshow("premi K per interrompere la registrazione",frame) #mostro la fotocamera con il titolo 


    if contr==ord('k'): #se viene premuta k esco dal while
        break
        
            
video.release() #addio fotocamera
print("registrazione interrotta, foto effettuate: "+str(volto)) #stampo il numero di foto effettuate 
cv2.destroyAllWindows() #tutta la memoria allocata va a farsi fottere
