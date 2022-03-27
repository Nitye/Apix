import googletrans

sentence = str("no problem")
translator = googletrans.Translator()
# translated_sentence = translator.translate(sentence,dest='es',src='en')
# print(translated_sentence)
print(translator.detect(sentence))