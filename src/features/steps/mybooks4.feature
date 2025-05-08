Feature: välja favoriter
#Som en användare vill jag kunna välja (och välja bort) favoriter ur listan, så att jag ser vad jag ska läsa som nästa bok
Scenario: välja (och välja bort) favoriter ur boklistan
Given användaren är igen inloggad på "katalog"-sidan
When användaren favoritmarkerar boken "Min katt är min chef"
Then Den valda boken blir markerad med hjärta
When användaren avmarkerar boken "Min katt är min chef"
Then Den valda boken blir inte längre markerad med hjärta

