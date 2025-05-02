from playwright.sync_api import sync_playwright, expect
from behave import given, when, then
from time import sleep


@given(u'användaren är inloggad på startsidan')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given användaren är inloggad på startsidan')


@then(u'Katalog"-sidan visas')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Katalog"-sidan visas')


@when(u'användaren klickar på "Katalog"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren klickar på "Katalog"')


@then(u'"Katalog"-sidan visas')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Katalog"-sidan visas')


@when(u'användaren klickar på "Lägg till bok"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren klickar på "Lägg till bok"')


@then(u'"Lägg till bok"-sidan visas')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Lägg till bok"-sidan visas')


@when(u'användaren klickar på "Mina böcker"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren klickar på "Mina böcker"')


@then(u'"Mina böcker"-sidan visas')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "Mina böcker"-sidan visas')


@given(u'användaren är igen inloggad på "Lägg till bok"-sidan')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given användaren är igen inloggad på "Lägg till bok"-sidan')


@when(u'användaren favoritmarkerar boken "Min katt är min chef"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren favoritmarkerar boken "Min katt är min chef"')


@then(u'Den valda boken blir markerad med hjärta')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Den valda boken blir markerad med hjärta')


@when(u'användaren avmarkerar boken "Min katt är min chef"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren avmarkerar boken "Min katt är min chef"')


@then(u'Den valda boken blir inte längre markerad med hjärta')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Den valda boken blir inte längre markerad med hjärta')


@given(u'användaren är återigen inloggad på "Katalog"-sidan"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given användaren är återigen inloggad på "Katalog"-sidan"')


@when(u'användaren favoritmarkerar boken "100 sätt att undvika måndagar"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren favoritmarkerar boken "100 sätt att undvika måndagar"')


@then(u'den valda boken hamnar i listan på "mina böcker-sidan"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then den valda boken hamnar i listan på "mina böcker-sidan"')


@given(u'användaren är återigen inloggad på "Lägg till bok"-sidan')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given användaren är återigen inloggad på "Lägg till bok"-sidan')


@when(u'användaren adderar en ny bok. Titel: "Allt du vilat veta om godståg, men inte vågat fråga" Författare: Anna Signal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When användaren adderar en ny bok. Titel: "Allt du vilat veta om godståg, men inte vågat fråga" Författare: Anna Signal')


@then(u'Ny bok skapas och listas på sidan "Katalog"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Ny bok skapas och listas på sidan "Katalog"')

