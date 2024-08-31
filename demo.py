from text_to_speech.component.get_accent import get_accent_message,get_accent_tld

accent_list = get_accent_message()

print(accent_list)

accent = accent_list[3]

tld = get_accent_tld(accent)
print(tld)