# Winners
Python-uppgift för Softhouse.

Jag har använt Python-biblioteken Pandas och Flask för att lösa uppgiften. Dockerfilen är till för att skapa en dockerbild i vilken Pandas och Flask är installerade. 
För att köra programmet:

1. Bygg Dockerbilden med kommandot: 'docker build -t winnersimage .'
2. I Windows kan programmet köras med kommandot: 'docker run -v ${pwd}:/app -p 5000:5000 winnersimage winners.py'.
3. För att anropa API:n kan man köra 'curl.exe -X GET -F "file=@/path_to/aktiekurser.csv" http://127.0.0.1:5000/winners'.
   
Filen Test.py innehåller enhetstester för att testa programmet. Den testar bland annat att förväntat att man får förväntad procentuell utveckling är korrekt och att några tänkbara fel hanteras (t.ex. att csv-filen är tom och att kolumnen för datum och kurs innehåller otillåtna tecken. Testerna kan i Windows köras med kommandot 'docker run -v ${pwd}:/app -p 5000:5000 winnersimage Test.py'.

Min tolkning av uppgiften: Om flera aktier delar rank (det kan  till exempel inträffa om det bara finns en data punkt för dagens datum för två eller fler aktier) så tas de båda med i json-filen (med samma rank).
