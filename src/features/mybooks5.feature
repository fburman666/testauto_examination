Feature: se valda favoriter i listan
#Som en användare vill jag kunna se valda favoriter i listan "mina favoriter", så att jag har lättare kan se mina favoritböcker
Scenario: se valda favoriter i favoritlistan
Given användaren är återigen inloggad på "Katalog"-sidan"
When användaren favoritmarkerar boken "100 sätt att undvika måndagar"
Then den valda boken hamnar i listan på "mina böcker-sidan"

