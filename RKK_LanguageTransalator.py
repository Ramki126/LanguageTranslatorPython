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