from googletrans import Translator

translator = Translator()

text = translator.translate('If you know you know', dest = 'mn')
print(text.text)