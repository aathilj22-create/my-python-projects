# Python Program to Generate Student Mark Statement

def generate_mark_sheet():
    print("=========================================")
    print("       STUDENT MARK SHEET GENERATOR      ")
    print("=========================================\n")
    
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number / Register Number: ")
    
    subjects = ["Mathematics", "Science", "English", "Social Studies", "tamil"]
    marks = {}
    total_marks = 0
    has_failed = False
    
    print("\nEnter marks obtained (out of 100):")
    
    # Step 2: Loop through each subject to get input and validate it
    for sub in subjects:
        while True:
            try:
                mark = float(input(f"  {sub}: "))
                if 0 <= mark <= 100:
                    marks[sub] = mark
                    total_marks += mark
                    # Assuming 40 is the minimum pass mark per subject
                    if mark < 40:
                        has_failed = True
                    break
                else:
                    print("  [Error] Marks must be between 0 and 100. Try again.")
            except ValueError:
                print("  [Error] Invalid input. Please enter a valid number.")

    # Step 3: Calculate calculations (assuming max 100 marks per subject)
    max_total = len(subjects) * 100
    percentage = (total_marks / max_total) * 100
    
    # Step 4: Determine Grade based on conditions
    if has_failed:
        result = "FAIL"
        grade = "F"
    else:
        result = "PASS"
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "E"

    # Step 5: Format and display the final printed Report Card / Statement
    print("\n=========================================")
    print("             MARK STATEMENT              ")
    print("=========================================")
    print(f" Student Name : {name.upper()}")
    print(f" Roll Number   : {roll_no}")
    print("-----------------------------------------")
    print(f" {'SUBJECT':<20} | {'MARKS OBTAINED':<15}")
    print("-----------------------------------------")
    for sub, mark in marks.items():
        print(f" {sub:<20} | {mark:<15}")
    print("-----------------------------------------")
    print(f" Total Marks   : {total_marks:.1f} / {max_total}")
    print(f" Percentage    : {percentage:.2f}%")
    print(f" Final Result  : {result}")
    print(f" Overall Grade : {grade}")
    print("=========================================")

if __name__ == "__main__":
    generate_mark_sheet()
