#Feature: Lägga till böcker och hantera favoriter i läslistan

Feature: startsidan används vid inloggning
#Som en användare vill jag se "katalog"-sidan vid inloggning, så att jag ser alla böcker i listan
Scenario: "katalog"-sidan visas vid inloggning
Given användaren är inloggad på startsidan
Then "Katalog"-sidan visas
#When användaren klickar på "Katalog"
#Then "Katalog"-sidan visas igen

