# story_idea_generator.py

def story(genre, theme, character):
    """Generates a creative story prompt."""
    prompt = f"Generate a story idea in the {genre} genre about {theme}, featuring a {character}."
    return prompt


def main():
    print("Welcome to the Story Idea Generator!")

    while True:
        # User input
        genre = input("Enter a genre (e.g., fantasy, thriller): ").strip()
        theme = input("Enter a theme (e.g., love, war, betrayal): ").strip()
        character = input("Enter a character type (e.g., orphan hero, robot teacher): ").strip()

        # Generate prompt
        prompt = story(genre or 'unspecified', theme or 'unspecified', character or 'unspecified')

        # Display the final prompt
        print("\nYour AI Prompt:")
        print(prompt)
        print("\nUse this prompt in ChatGPT to generate a story idea!\n")

        # Ask to continue
        count = input("Do you want to generate another? (yes/no): ").strip().lower()
        if count != "yes":
            print("Thank you for using the Story Idea Generator!")
            break


if __name__ == "__main__":
    main()
