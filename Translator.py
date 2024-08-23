from googletrans import Translator, LANGUAGES

def translate_text(text, src_language='auto', dest_language='en'):
    """
    Translate text from source language to destination language.

    :param text: The text to translate.
    :param src_language: The source language code (default is 'auto' which detects the language).
    :param dest_language: The destination language code (default is 'en' for English).
    :return: Translated text.
    """
    translator = Translator()
    try:
        translation = translator.translate(text, src=src_language, dest=dest_language)
        return translation.text
    except Exception as e:
        return f"Error: {e}"

def display_language_options():
    """
    Display available language options.
    """
    print("\nAvailable languages:")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

def main():
    print("Welcome to the Python Translator App!")
    
    # Display available languages
    display_language_options()
    
    # Input text to be translated
    text_to_translate = input("\nEnter the text you want to translate: ")
    
    # Input source language code (or leave empty to auto-detect)
    src_language = input("Enter the source language code (e.g., 'en' for English, 'es' for Spanish, leave empty to auto-detect): ")
    if not src_language:
        src_language = 'auto'
    
    # Input target language code
    dest_language = input("Enter the destination language code (e.g., 'en' for English, 'es' for Spanish): ")
    
    # Perform translation
    translated_text = translate_text(text_to_translate, src_language, dest_language)
    
    print("\nTranslated Text:")
    print(translated_text)

if __name__ == "__main__":
    main()
