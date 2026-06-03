import random


def load_question_bank(file_path):
    """Load questions and answers from the question bank file."""
    questions = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Each question is on one line, answer on the next
            for i in range(0, len(lines) - 1, 2):
                question = lines[i].strip()
                answer = lines[i + 1].strip()
                if question and answer:
                    questions.append((question, answer))
        return questions
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def create_exam(questions, num_questions, output_file):
    """Randomly select questions and save them to the output file."""
    # Make sure we don't ask for more questions than available
    if num_questions > len(questions):
        print(f"Warning: Only {len(questions)} questions available. Using all of them.")
        num_questions = len(questions)

    selected = random.sample(questions, num_questions)

    try:
        with open(output_file, 'w') as file:
            for i, (question, answer) in enumerate(selected, 1):
                file.write(f"Q{i}: {question}\n")
                file.write(f"A{i}: {answer}\n\n")
        return True
    except Exception as e:
        print(f"Error saving exam: {e}")
        return False


def get_valid_int(prompt):
    """Keep asking until the user enters a valid integer."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("Welcome to professor assistant version 1.0.")

    professor_name = input("Please Enter Your Name: ").strip()

    print(f"Hello Professor. {professor_name}, I am here to help you create exams from a question bank.")

    while True:
        choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ").strip().lower()

        if choice == 'no':
            print(f"Thank you professor {professor_name}. Have a good day!")
            break

        elif choice == 'yes':
            # Get and validate question bank path
            while True:
                bank_path = input("Please Enter the Path to the Question Bank. ").strip()
                questions = load_question_bank(bank_path)
                if questions is not None:
                    print("Yes, indeed the path you provided includes questions and answers.")
                    break
                else:
                    print("Please try again with a valid file path.")

            # Get number of questions
            num_questions = get_valid_int("How many question-answer pairs do you want to include in your exam? ")

            # Get output file name
            output_file = input("Where do you want to save your exam? ").strip()

            # Create the exam
            success = create_exam(questions, num_questions, output_file)

            if success:
                print(f"Congratulations Professor {professor_name}. Your exam is created and saved in {output_file}.")

        else:
            print("Please enter 'Yes' or 'No'.")


if __name__ == "__main__":
    main()