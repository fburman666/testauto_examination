from playwright.sync_api import sync_playwright, expect
from behave import given, when, then
import re
#from time import sleep

#1. Som en användare vill jag se "katalog"-sidan vid inloggning, så att jag ser alla böcker i listan
@given(u'användaren är inloggad på startsidan')
def step_given_user_at_start_page(context):
    context.page.goto(context.base_url)

@then(u'"Katalog"-sidan visas')
def step_check_catalog_page(context):
    expect(context.page.get_by_text("Hur man tappar bort sin TV-fjärr 10 gånger om dagen")).to_have_count(1, timeout=200)

#Som en användare vill jag se "lägg till bok"-sidan vid klick på "Lägg till bok", så att jag har möjlighet att addera nya böcker
@given(u'användaren är inloggad på startsidan igen')
def step_given_user_at_start_page(context):
    context.page.goto(context.base_url)

@when(u'användaren klickar på "Lägg till bok"')
def step_when_user_clicks_addbook(context):
    button = context.page.get_by_test_id("add-book")
    button.click()

@then(u'"Lägg till bok"-sidan visas')
def step_check_addbook_page(context):
    expect(context.page.get_by_text("Titel")).to_have_count(1, timeout=200)

#Som en användare vill jag se "Mina böcker"-sidan vid klick på "Mina böcker", så att jag kan se mina favoriter
@given(u'användaren är inloggad på startsidan återigen')
def step_given_user_at_start_page(context):
    context.page.goto(context.base_url)

@when(u'användaren klickar på "Mina böcker"')
def step_when_user_clicks_favorites(context):
    button = context.page.get_by_test_id("favorites")
    button.click()

@then(u'"Mina böcker"-sidan visas')
def step_check_default_favorites_page(context):
    expect(context.page.get_by_text("När du valt, kommer dina")).to_have_count(1, timeout=200)

#Som en användare vill jag kunna välja (och välja bort) favoriter ur listan, så att jag ser vad jag ska läsa som nästa bok
@given(u'användaren är igen inloggad på "katalog"-sidan')
def step_given_user_at_start_page(context):
    context.page.goto(context.base_url)

@when(u'användaren favoritmarkerar boken "Min katt är min chef"')
def step_when_heart_marking_book(context):
    button = context.page.get_by_test_id("star-Min katt är min chef")
    button.click()


@then(u'Den valda boken blir markerad med hjärta')
def step_check_favorite(context):
    #button = context.page.get_by_test_id("star-Min katt är min chef")
    expect(context.page.locator(".star.selected")).to_have_count(1, timeout=200)

@when(u'användaren avmarkerar boken "Min katt är min chef"')
def step_when_unmarking_book(context):
    button = context.page.get_by_test_id("star-Min katt är min chef")
    button.click()


@then(u'Den valda boken blir inte längre markerad med hjärta')
def step_uncheck_favorite(context):
    button = context.page.get_by_test_id("star-Min katt är min chef")
    #expect(button.locator(".star.selected")).to_have_count(0, timeout=200)
    expect(context.page.locator(".star.selected")).to_have_count(0, timeout=200)

#Som en användare vill jag kunna se valda favoriter i listan "mina favoriter", så att jag har lättare kan se mina favoritböcker
@given(u'användaren är återigen inloggad på "Katalog"-sidan"')
def step_given_user_at_start_page(context):
    context.page.goto(context.base_url)

@when(u'användaren favoritmarkerar boken "100 sätt att undvika måndagar"')
def step_when_heart_marking_new_book(context):
    button = context.page.get_by_test_id("star-100 sätt att undvika måndagar")
    button.click()


@then(u'den valda boken hamnar i listan på "mina böcker-sidan"')
def step_check_favorite_list(context):
    button =  context.page.get_by_test_id("favorites")
    button.click()
    expect(context.page.get_by_test_id("fav-100 sätt att undvika måndagar")).to_have_count(1,timeout=200)


#Som en användare vill jag kunna lägga till nya böcker, så att jag kan komplettera listan med fler intressanta böcker
@given(u'användaren är inloggad på "Lägg till bok"-sidan')
def step_given_user_at_start_page(context):
    context.page.goto(context.base_url)
    context.page.get_by_test_id("add-book").click()


@when(u'användaren adderar en ny bok. Titel: "Allt du velat veta om godståg, men inte vågat fråga" Författare: Anna Signal')
def step_when_user_adds_new_book(context):
    title = context.page.get_by_test_id("add-input-title")
    title.fill("Allt du velat veta om godståg, men inte vågat fråga")
    author = context.page.get_by_test_id("add-input-author")
    author.fill("Anna Signal")
    button = context.page.get_by_test_id("add-submit")
    button.click()


@then(u'Ny bok skapas och listas på sidan "Katalog"')
def step_check_catalog_list(context):
    button = context.page.get_by_test_id("catalog")
    button.click()
    expect(context.page.get_by_test_id("star-Allt du velat veta om godståg, men inte vågat fråga")).to_have_count(1,timeout=200)


#som en användare vill jag inte kunna addera ny bok utan att jag angett både titel och författare, så att inga felaktiga böcker hamnar i listan
@given(u'Användaren är igen inloggad på "lägg till bok"-sidan')
def step_given_user_at_start_page(context):
    context.page.goto(context.base_url)
    context.page.get_by_test_id("add-book").click()


@when(u'Tomma rader anges som titel och författare')
#gör inget

@then(u'Det går ej att lägga till ny bok')
def step_check_gray_addbutton(context):
    button = context.page.get_by_role("button").get_by_text(re.compile("ny bok"))
    #print(f"button={button}")
    expect(button).to_be_disabled()
