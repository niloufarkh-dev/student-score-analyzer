import numpy as np

student_name = input("Student name: ")

num_scores = int(input("How many scores? "))

scores = []

for i in range(num_scores):

    while True:
        score = float(input(f"Score {i + 1}: "))

        if 0 <= score <= 20:
            scores.append(score)
            break
        else:
            print("Error: score must be between 0 and 20.")

print("\n----- Results -----")

for score in scores:

    if score >= 18:
        status = "Excellent"

    elif score >= 15:
        status = "Good"

    else:
        status = "Needs Improvement"

    print(f"{student_name}: {score} --> {status}")

scores_array = np.array(scores)

print("\n----- Statistics -----")
print(f"Student: {student_name}")
print(f"Average: {scores_array.mean():.2f}")
print(f"Highest: {scores_array.max()}")
print(f"Lowest: {scores_array.min()}")