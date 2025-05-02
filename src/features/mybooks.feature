Feature: Lägga till böcker och hantera favoriter i läslistan

#Som en användare vill jag se "katalog"-sidan vid inloggning och vid klick på "katqlog", så att jag ser alla böcker i listan
Scenario: "katalog"-sidan visas vid inloggning och vid klick på "katqlog"
Given användaren är inloggad på startsidan
Then Katalog"-sidan visas
When användaren klickar på "Katalog"
Then "Katalog"-sidan visas


#Som en användare vill jag se "lägg till bok"-sidan vid klick på "Lägg till bok", så att jag har möjlighet att addera nya böcker
Scenario:  "lägg till bok"-sidan vid klick på "Lägg till bok"
Given användaren är inloggad på startsidan
When användaren klickar på "Lägg till bok"
Then "Lägg till bok"-sidan visas


#Som en användare vill jag se "Mina böcker"-sidan vid klick på "Mina böcker", så att jag kan se mina favoriter
Scenario: "Mina böcker"-sidan vid klick på "Mina böcker"
Given användaren är inloggad på startsidan
When användaren klickar på "Mina böcker"
Then "Mina böcker"-sidan visas


#Som en användare vill jag kunna välja (och välja bort) favoriter ur listan, så att jag ser vad jag ska läsa som nästa bok
Scenario: välja (och välja bort) favoriter ur boklistan
Given användaren är igen inloggad på "Lägg till bok"-sidan
When användaren favoritmarkerar boken "Min katt är min chef"
Then Den valda boken blir markerad med hjärta
When användaren avmarkerar boken "Min katt är min chef"
Then Den valda boken blir inte längre markerad med hjärta


#Som en användare vill jag kunna se valda favoriter i listan "mina favoriter", så att jag har lättare kan se mina favoritböcker
Scenario: se valda favoriter i favoritlistan
Given användaren är återigen inloggad på "Katalog"-sidan"
When användaren favoritmarkerar boken "100 sätt att undvika måndagar"
Then den valda boken hamnar i listan på "mina böcker-sidan"


#Som en användare vill jag kunna lägga till nya böcker, så att jag kan komplettera listan med fler intressanta böcker
Scenario: lägga till nya böcker
Given användaren är återigen inloggad på "Lägg till bok"-sidan
When användaren adderar en ny bok. Titel: "Allt du vilat veta om godståg, men inte vågat fråga" Författare: Anna Signal
Then Ny bok skapas och listas på sidan "Katalog"