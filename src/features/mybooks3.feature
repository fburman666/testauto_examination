Feature: klicka på "mina böcker"
#Som en användare vill jag se "Mina böcker"-sidan vid klick på "Mina böcker", så att jag kan se mina favoriter
Scenario: "Mina böcker"-sidan vid klick på "Mina böcker"
Given användaren är inloggad på startsidan återigen
When användaren klickar på "Mina böcker"
Then "Mina böcker"-sidan visas

