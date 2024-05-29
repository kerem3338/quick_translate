"""
Quick Translate
          By Zoda.


Python İçin Hızlı Önceden Tanımlı Metin Çevirme Kütüphanesidir

Dosya Oluşturulma Tarihi: 29/05/2024 21:23
  (File Creation Date)
------------------------------------------
Example Usage / Örnek Kullanım


---
import quick

translator=quick.Translator()
turkish_lang=quick.Language("Turkish","tr_TR")
turkish_lang.messages["hello"]="Merhabalar!"
translator.add_language(turkish_lang)

print(translator.get_message("hello","tr_TR"))
------------------------------------------
TODO:
    * load languages from file.
    * load translation data from web.
    
"""
import os
import sys
import locale

version=0.1
version_tag="Module Usage"
default_language=locale.getdefaultlocale()[0]

class LanguageAlreadyExistsError(Exception):
    """Exception raised if language is already added to Translator class."""
    def __init__(self,message):
        super().__init__(message)
        
class LanguageNotExists(Exception):
    """Exception raised if language is not exists."""
    def __init__(self,lang_referance,message="Language '{lang_referance}' Not Exists"):
        super().__init__(message.format(lang_referance=lang_referance))
        
class MessageNotExists(Exception):
    """Exception raised if message not exists in language messages."""
    def __init__(self,message_key,lang_referance,message="Message '{message_key}' Not Exists In Language '{lang_referance}'."):
        super().__init__(message.format(message_key=message_key,lang_referance=lang_referance))
       

       
class Translator:
    "Translator class"
    def __init__(self):
        self.description="Standart Translator"
        self.languages={}
        
    def get_message(self,message_key:str,language_code:str) -> str:
        """Get Message From Selected Language
        
        if language_code is 'locale_language' its changed to machines default language code.
        example
            -> tr_TR
        """
        
        if language_code == "locale_language":
            language_code=default_language
            
        if language_code in self.languages:
            if message_key in self.languages[language_code]:
                return self.languages[language_code][message_key]
            else:
                raise MessageNotExists(message_key,language_code)
        else:
            raise LanguageNotExists(language_code)
            
    def add_language(self,language) -> None:
        "Add language to Translator"
        if not language.code in self.languages:
            self.languages[language.code]=language.messages
        else:
            LanguageAlreadyExistsError(f"Language Code '{language.code}' Already Added to languages.")

    def __str__(self) -> str:
        return f"<Translator()>"

class Language:
    "Language Class"
    def __init__(self,name,code,messages={}):
        self.name:str=name
        self.code:str=code
        self.messages:dict=messages
        
    def get_message(self,key):
        "Get message from Language"
        return self.messages[key]
        
    def __str__(self) -> str:
        return f"<Language({self.name},{self.code})>"

if __name__=="__main__":
    translator=Translator()
    translator.add_language(Language("Turkish[TR]","tr_TR",{"hello":"Merhabalar!"}))
    translator.add_language(Language("English[US]","en_US",{"hello":"Hello!"}))
    translator.add_language(Language("English[GB]","en_GB",{"hello":"Hello!"}))
    translator.add_language(Language("Turkish[AZ]","az_AZ",{"hello":"Salam!"}))

    print(translator.get_message("hello","locale_language"))
