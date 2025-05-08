Feature: lägga till nya böcker
#Som en användare vill jag kunna lägga till nya böcker, så att jag kan komplettera listan med fler intressanta böcker
Scenario: lägga till nya böcker
Given användaren är inloggad på "Lägg till bok"-sidan
When användaren adderar en ny bok. Titel: "Allt du velat veta om godståg, men inte vågat fråga" Författare: Anna Signal
Then Ny bok skapas och listas på sidan "Katalog"

Scenario: Tomma rader för titel och författare går ej att mata in
Given Användaren är igen inloggad på "lägg till bok"-sidan
When Tomma rader anges som titel och författare
Then Det går ej att lägga till ny bok