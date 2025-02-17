# Winners
Python-uppgift för Softhouse.

Jag har använt Python-biblioteket Pandas för att lösa uppgiften. Dockerfilen är till för att skapa en dockerbild i vilken Pandas är installerad. 
För att köra programmet:

1. Bygg Dockerbilden med kommandot: 'docker build -t winnersimage .'
2. I Windows kan programmet köras med kommandot: 'docker run -v ${pwd}:/app winnersimage winners.py aktiekurser.csv' (eller byt ut aktiekurser.csv mot önskad .csv-fil).
   
Filen Test.py innehåller enhetstester för att testa programmet. Den testar bland annat att förväntat att man får förväntad procentuell utveckling är korrekt och att några tänkbara fel hanteras (t.ex. att csv-filen är tom och att kolumnen för datum och kurs innehåller otillåtna tecken.


Min tolkning av uppgiften: Om flera aktier delar rank (det kan  till exempel inträffa om det bara finns en data punkt för dagens datum för två eller fler aktier) så tas de båda med i json-filen (med samma rank).
