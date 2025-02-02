# LanguageTranslatorPython

In today’s interconnected world, language should never be a barrier. Whether you're working on multilingual software testing, automating localization checks, or just need quick translations, Python has you covered!

This Python script translates text into a specified target language using the Google Translate API. It’s a simple yet powerful tool for localization testing, multilingual automation, and everyday translation needs
Features

✅ Accepts user input for text and target language

✅ Returns translated text instantly

✅ Handles exceptions to avoid crashes

✅ Lightweight and easy to integrate into automation scripts

----------------------------------------------------------------------------------------------
from googletrans import Translator
def translate_text(text, target_language):
    try:
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return text  # Return original text if translation fails
def main():
    # Get user input
    user_text = input("Enter text to translate: ").strip()
    if not user_text:
        print("No input provided. Exiting.")
        return
    # Display language options
    languages = {
        '1': ('French', 'fr'),
        '2': ('German', 'de'),
        '3': ('Spanish', 'es'),
          }
    print("\nSelect languages for translation:")
    for key, (lang_name, _) in languages.items():
        print(f"{key}. {lang_name}")
    # Get user selection
    selected_keys = input("\nEnter numbers (comma-separated) for translation (e.g., 1,3,5): ").split(",")
    # Translate text into selected languages
    for key in selected_keys:
        key = key.strip()
        if key in languages:
            lang_name, lang_code = languages[key]
            translated_text = translate_text(user_text, lang_code)
            print(f"\nTranslation in {lang_name}: {translated_text}")
if __name__ == "__main__":
    main()
    -----------------------------------------------------------------------------------------



