     PRE-REQUIREMENTS:

          Per visualizzare i dati AIS si necessita di un software free: Quantum GIS
               1. Scaricare ed installare QGIS: https://qgis.org/downloads/QGIS-OSGeo4W-3.22.6-1.msi
                    Software cartografico per la gestione dei dati GIS. Free-to-play, GO!
               2. Se non si ha già una distribuzione python, installare anaconda: https://www.anaconda.com/products/distribution
               3. installare VS code: https://code.visualstudio.com/download
                    Questo serve per aprire i jupyter notebook (quelli che finora hai conosciuto come COLAB, ebbene si, la grande menzogna..)
               
     INSTALLATION:
          
          - Rechiamoci alla repository github del santo robs (https://github.com/UninaLabs-EO/ClaudioParserAIS).
          - Bottone Verde (Code) > Download ZIP
          - Estraiamo ed apriamo la cartella con VS Code:
                    Si puo fare in tanti modi: 1) Apri VS Code > File (Tab) > Apri cartella
          - Apro il terminale di comando:
                    Da VS Code: Visualizza (Tab) > Terminale          
          - Da linea di comando invio questo comando:
                    conda env create -f environment.yml
          - Attivo l'environment appena creato, da linea di comando:
                    conda activate ais decoder

          Se tutto è andato a dovere, il setting è completato!

     USAGE:
          - Aprire il jupyter: due click su Parser.ipynb e ti apre un colabbino.
          - Questo è il notebook che vedemmo insieme. Ti basta seguire le istruzioni nel notebook per filtrare i dati ais.

          - Una volta ottenuti i files (nb: il file che ti serve è .shp ma gli altri non vanno cancellati assolutamente, sono collegati ad esso)
          - Apri QGIS > Nuovo Progetto > trascino il file shp da finestra windows a qgis (drag e drop secco)
                              NB: Dovresti vedere i dati ais ora come pallini
          - Drag e drop immagine geotiff in qgis e selezionando nella barra dei livelli quello dei dati ais lo vado a portare sopra in alto
          - Tasto destro su layer dato ais (chiamato navi) e vado in proprieta layer > etichette > Etichette Singole (Da: Non Mostrare Etichette)
                    NB: Assicurare che Valore = label

          - Individuate le navi presenti in scena tramite il loro identificativo MMSI, mi porto di nuovo in VS code.
          - Riapro Parser > Filtro tramite l'ultima cella con numero MMSI e ottengo le informazioni magiche che ci servono.
          NB: puoi esportare questa ricerca già in un file excel usando il metodo di classe:   .to_excel()

               