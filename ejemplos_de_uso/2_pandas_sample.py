#Statistical Data Analysis with pandas

import pandas as pd

def create_dataframe():
    id0 = 1
    score0 = 75.5
    passed0 = True
    name0 = "Alice"

    id1 = 2
    score1 = 62.0
    passed1 = False
    name1 = "Bob"

    id2 = 3
    score2 = 88.0
    passed2 = True
    name2 = "Carol"

    id3 = 4
    score3 = 49.5
    passed3 = False
    name3 = "Dave"

    id4 = 5
    score4 = 95.0
    passed4 = True
    name4 = "Eve"

    df = pd.DataFrame({
        "id": (id0, id1, id2, id3, id4),
        "score": (score0, score1, score2, score3, score4),
        "passed": (passed0, passed1, passed2, passed3, passed4),
        "name": (name0, name1, name2, name3, name4)
    })
    return df

def analyze_dataframe(df):
    mean_score = df["score"].mean()
    max_score = df["score"].max()
    min_score = df["score"].min()

    max_name = ""
    min_name = ""

    i = 0
    passed_count = 0

    while i < 5:
        score = float(df["score"].iloc[i])
        name = str(df["name"].iloc[i])
        passed = bool(df["passed"].iloc[i])

        if score == max_score:
            max_name = name
        if score == min_score:
            min_name = name
        if passed:
            passed_count = passed_count + 1

        i = i + 1

    print(f"Average score: {mean_score}")
    print(f"Maximum score: {max_score} (by {max_name})")
    print(f"Minimum score: {min_score} (by {min_name})")
    print(f"Number of students who passed: {passed_count}")

df = create_dataframe()

print(df)
analyze_dataframe(df)

