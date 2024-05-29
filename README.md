# Quick Translator

🇹🇷 Quick Translator önceden tanımlı mesajlarınızı farklı dillere çevirim desteği ekleyebileceğiniz bir kütüphanedir.<br>
🇺🇸 Quick Translator is a library that supports translating your predefined messages into different languages.<br>

## Example / Örnek
```python
import quick
translator=quick.Translator()

turkish=quick.Language("Turkish","tr_TR")
turkish.messages["hello"]="Merhabalar!"
translator.add_language(turkish)

english=quick.Language("English","en_US")
english.messages["hello"]="Hello!"
translator.add_language(english)

# Get hello messaged based on your system locale settings / Sisteminizin varsayılan 'yerel' ayarına göre 'hello' mesajını gösterecektir.
print(translator.get_message("hello","locale_language"))
```

## Installing / İndirme

🇺🇸 Just Download The `quick.py` file from kerem3338/quick_translate repo.<br>
🇹🇷 Sadece kerem3338/quick_translate deposundan `quick.py` dosyasını indirin.