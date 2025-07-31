import random

# Function to collect user information


def collect_user_info():
    # Basic questions that must be asked
    essential_questions = {
        "name": "What is your name? ",
        "age": "How old are you? "
    }

    # Extra questions to ask randomly
    extra_questions = {
        "color": "What is your favorite color? ",
        "city": "Where do you live? ",
        "school": "Which Senior High School did you attend? ",
        "team": "Which soccer team do you support? "
    }

    answers = {}

    # Ask the essential questions
    for key in essential_questions:
        question = essential_questions[key]
        user_input = input(question)
        answers[key] = user_input

    # Ask 2 to 4 random extra questions
    number_of_questions = random.randint(2, 4)
    selected_keys = random.sample(list(extra_questions), number_of_questions)

    for key in selected_keys:
        question = extra_questions[key]
        user_input = input(question)
        answers[key] = user_input

    return answers

# Function to display summary of answers


def show_summary(answers):
    print("\n=== Summary of Your Information ===")
    print("Hello " + answers.get("name", "friend") + "!")

    if "age" in answers:
        print("You are " + answers["age"] + " years old.")
    if "color" in answers:
        print("Your favorite color is " + answers["color"] + ".")
    if "city" in answers:
        print("You live in " + answers["city"] + ".")
    if "school" in answers:
        print("You went to " + answers["school"] + " SHS.")
    if "team" in answers:
        print("You support " + answers["team"] + ".")

# Function to save information in a text file


def save_to_file(answers, rating):
    file_name = answers.get("name", "summary") + ".txt"
    try:
        file = open(file_name, "w")
        file.write("User Information Summary\n")
        file.write("------------------------\n")
        for key in answers:
            file.write(key.capitalize() + ": " + answers[key] + "\n")
        file.write("Rating: " + str(rating) + "/5\n")
        file.close()
        print("Your summary has been saved in '" + file_name + "'.")
    except:
        print("There was a problem saving your file.")

# Main function to run everything


def run_assistant():
    while True:
        user_info = collect_user_info()
        show_summary(user_info)

        save_choice = input(
            "\nDo you want to save your summary? (yes/no): ").strip().lower()
        if save_choice == "yes":
            while True:
                rating_input = input("Rate this assistant from 1 to 5: ")
                if rating_input.isdigit():
                    rating = int(rating_input)
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Please enter a number between 1 and 5.")
                else:
                    print("That's not a number.")

            save_to_file(user_info, rating)

        again = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the assistant! 😊")
            break


# Start the assistant
if __name__ == "__main__":
    run_assistant()
