# ==========================================
# PART 1: SINGLE CLASS GRADE & FINAL EXAM CALCULATOR
# ==========================================

# 1. ENTER YOUR RAW SCORES HERE
# Note: Because the weights total 100, input your scores based on the max weight.
# Example: If quizzes are out of 15, and you got 12/15, enter 12.
my_quiz_score = 13.0    # Out of 15
my_assignment_score = 13.0 # Out of 15
my_midterm_score = 18.0    # Out of 20
# Final score is left blank because we are calculating what you NEED.

# 2. TEACHER'S GRADING POLICY (Weights)
WEIGHT_QUIZ = 15
WEIGHT_ASSIGNMENT = 15
WEIGHT_MIDTERM = 20
WEIGHT_FINAL = 50

# 3. GRADING SCALE DICTIONARY
def get_letter_grade(percentage):
    if percentage >= 85: return "A"
    elif percentage >= 80: return "A-"
    elif percentage >= 75: return "B+"
    elif percentage >= 71: return "B"
    elif percentage >= 68: return "B-"
    elif percentage >= 64: return "C+"
    elif percentage >= 61: return "C"
    elif percentage >= 58: return "C-"
    elif percentage >= 54: return "D+"
    elif percentage >= 50: return "D"
    else: return "F"

# 4. CALCULATE CURRENT STANDING
current_points_earned = my_quiz_score + my_assignment_score + my_midterm_score
current_max_points = WEIGHT_QUIZ + WEIGHT_ASSIGNMENT + WEIGHT_MIDTERM # 50 points total

# How are you doing right now as a percentage of the work completed so far?
current_progress_percentage = (current_points_earned / current_max_points) * 100

print("--- CURRENT CLASS STANDING ---")
print(f"Points earned so far: {current_points_earned} out of {current_max_points}")
print(f"Current percentage on completed work: {current_progress_percentage:.2f}%")
print(f"Current Letter Grade (if class ended today): {get_letter_grade(current_progress_percentage)}\n")

# 5. CALCULATE WHAT IS NEEDED FOR AN "A"
target_percentage_for_A = 85.0
target_points_needed = target_percentage_for_A # Because total weights = 100
points_needed_on_final = target_points_needed - current_points_earned

print("--- FINAL EXAM CALCULATOR ---")
if points_needed_on_final <= 0:
    print("🎉 Great news! You have already secured enough points for an A.")
    print("   You can score a 0 on the final and still get an A.")
elif points_needed_on_final <= WEIGHT_FINAL:
    required_final_percentage = (points_needed_on_final / WEIGHT_FINAL) * 100
    print(f"🎯 To get an A (85%), you need exactly {points_needed_on_final:.2f} points on the Final Exam.")
    print(f"   This means you need to score at least {required_final_percentage:.2f}% on the Final (out of {WEIGHT_FINAL} marks).")
else:
    print("❌ Unfortunately, it is mathematically impossible to get an A in this class.")
    print(f"   You would need {points_needed_on_final} points on the final, but the max is only {WEIGHT_FINAL}.")


# ==========================================
# PART 2: BONUS - YOUR TRANSCRIPT CGPA CALCULATOR
# ==========================================
print("\n" + "="*40)
print("--- TRANSCRIPT CGPA CALCULATOR ---")

# Data extracted from the table you provided
transcript = [
    {"course": "CS-412", "credits": 3, "gpa": 4.00},
    {"course": "CS-483", "credits": 3, "gpa": 3.66},
    {"course": "CS-411", "credits": 3, "gpa": 4.00},
    {"course": "CS-413", "credits": 3, "gpa": 4.00}
]

total_credits = 0
total_quality_points = 0

for course in transcript:
    quality_points = course["credits"] * course["gpa"]
    total_credits += course["credits"]
    total_quality_points += quality_points
    print(f"{course['course']}: {course['credits']} CrHrs x {course['gpa']} GPA = {quality_points:.2f} Quality Points")

calculated_cgpa = total_quality_points / total_credits
print(f"\nTotal Credits: {total_credits}")
print(f"Total Quality Points: {total_quality_points:.2f}")
print(f"🎯 Your Exact Current CGPA: {calculated_cgpa:.2f}")