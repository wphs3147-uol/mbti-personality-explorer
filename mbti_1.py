import sys

def ask_question(question, option_a, option_b):
    """
    Ask a question with two possible answers and return the user's choice.
    """
    while True:
        print(f"{question}\nA: {option_a}\nB: {option_b}")
        answer = input("Choose A or B: ").strip().upper()
        if answer in ('A', 'B'):
            return answer
        print("Invalid choice. Please enter A or B.")

def determine_mbti():
    """
    Determines a user's MBTI type based on their responses.
    """
    print("Answer the following questions to determine your MBTI personality type.\n")
    
    # E vs. I
    e_i = ask_question(
        "Do you feel more energised after socialising with a group of people, or do you prefer to recharge alone?",
        "Socialising energises me (Extraversion - E)",
        "I prefer to recharge alone (Introversion - I)"
    )
    
    # S vs. N
    s_n = ask_question(
        "Do you focus more on concrete facts and details, or do you enjoy abstract ideas and possibilities?",
        "I focus on concrete facts and details (Sensing - S)",
        "I enjoy abstract ideas and possibilities (Intuition - N)"
    )
    
    # T vs. F
    t_f = ask_question(
        "When making decisions, do you prioritise logic and objectivity, or personal values and emotions?",
        "I prioritise logic and objectivity (Thinking - T)",
        "I prioritise personal values and emotions (Feeling - F)"
    )
    
    # J vs. P
    j_p = ask_question(
        "Do you prefer a planned and organised lifestyle, or a more spontaneous and flexible one?",
        "I prefer a planned and organised lifestyle (Judging - J)",
        "I prefer a spontaneous and flexible lifestyle (Perceiving - P)"
    )
    
    # Determine MBTI Type
    mbti = "".join([
        "E" if e_i == "A" else "I",
        "S" if s_n == "A" else "N",
        "T" if t_f == "A" else "F",
        "J" if j_p == "A" else "P"
    ])
    
    print(f"\nYour MBTI personality type is: {mbti}")
    return mbti

if __name__ == "__main__":
    determine_mbti()
