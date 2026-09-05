import demoji

demoji.download_codes()

def emoji_cleaner(text):
    print("\nChoose an option:")
    print("1 - Remove emojis")
    print("2 - Replace emojis with description")
    print("3 - Detect emojis")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        result = demoji.replace(text, "")
        print("\nText after removal:", result)

    elif choice == "2":
        result = demoji.replace_with_desc(text)
        print("\nText after replacement:", result)

    elif choice == "3":
        result = demoji.findall(text)
        print("\nDetected emojis:", result)

    else:
        print("⚠️ Invalid choice")

text = input("Enter text with emojis: ")
emoji_cleaner(text)
