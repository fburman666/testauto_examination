Feature: Addera bok
#Som en användare vill jag se "lägg till bok"-sidan vid klick på "Lägg till bok", så att jag har möjlighet att addera nya böcker
Scenario:  "lägg till bok"-sidan vid klick på "Lägg till bok"
Given användaren är inloggad på startsidan igen
When användaren klickar på "Lägg till bok"
Then "Lägg till bok"-sidan visas

