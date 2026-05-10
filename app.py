from flask import Flask, render_template, request
import pickle
from difflib import get_close_matches

app = Flask(__name__)

# Load pickle files
df = pickle.load(open("workout.pkl", "rb"))

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

vectors = pickle.load(open("vectors.pkl", "rb"))

similarity = pickle.load(open("similarity.pkl", "rb"))


# Convert titles to lowercase once
df["Title"] = df["Title"].str.lower()


# Recommendation Function
def pred(title):

    title = title.lower().strip()

    # Find closest matching title
    matches = get_close_matches(
        title,
        df["Title"].tolist(),
        n=1,
        cutoff=0.5
    )

    # No match found
    if not matches:
        return ["Workout not found"]

    # Best match
    matched_title = matches[0]

    # Get index
    index = df[df["Title"] == matched_title].index[0]

    # Similarity scores
    distances = list(enumerate(similarity[index]))

    # Sort scores
    sorted_list = sorted(
        distances,
        reverse=True,
        key=lambda x: x[1]
    )

    # Top 5 recommendations
    top_five = sorted_list[1:6]

    recommendations = []

    for i in top_five:

        recommendations.append(
            df.iloc[i[0]].Title.title()
        )

    return recommendations


# Home Page
@app.route("/")
def home():

    workout_list = sorted(
        df["Title"]
        .fillna("")
        .str.replace("-", " ")
        .str.title()
        .tolist()
    )

    return render_template(
        "index.html",
        workouts=workout_list
    )



# Prediction Route
@app.route("/predict", methods=["POST"])
def predict():

    workout_name = request.form["workout"]

    recommendations = pred(workout_name)

    return render_template(
        "result.html",
        recommendations=recommendations,
        workout=workout_name.title()
    )


# Run Flask App
if __name__ == "__main__":

    app.run(debug=True)