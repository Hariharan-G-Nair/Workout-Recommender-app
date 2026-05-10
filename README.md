# 💪 Workout Recommendation System

An NLP-powered workout recommendation web application built using Flask, NLTK, and scikit-learn.

The application recommends similar workouts using Natural Language Processing techniques and cosine similarity based content filtering.

---

# 🚀 Features

- NLP-based workout recommendation engine
- Content-based filtering using cosine similarity
- Flask web application
- Smart workout search with autocomplete
- Text preprocessing using NLTK
- Vectorization using CountVectorizer
- Responsive modern UI

---

# 🛠️ Technologies Used

## Backend
- Python
- Flask

## NLP & Machine Learning
- NLTK
- scikit-learn
- CountVectorizer
- Cosine Similarity

## Data Processing
- pandas
- numpy

## Frontend
- HTML
- CSS

---

# 📚 NLP Pipeline

The recommendation system follows this NLP workflow:

```text
Raw Workout Data
       ↓
Data Cleaning
       ↓
Text Preprocessing
       ↓
Tokenization
       ↓
Stopword Removal
       ↓
Stemming
       ↓
Lemmatization
       ↓
Count Vectorization
       ↓
Cosine Similarity
       ↓
Workout Recommendation
```

---

# 🔍 NLP Techniques Used

## 1. Tokenization
Splits workout descriptions into smaller tokens/words.

Example:

```python
"I love workouts"
↓
["I", "love", "workouts"]
```

---

## 2. Stopword Removal

Removes common English words such as:

- the
- is
- and
- are

---

## 3. Stemming

Reduces words into root form.

Example:

```text
running → run
lifting → lift
```

---

## 4. Lemmatization

Converts words into meaningful base words.

Example:

```text
better → good
mice → mouse
```

---

## 5. Count Vectorization

Converts text data into numerical vectors using:

```python
CountVectorizer()
```

---

## 6. Cosine Similarity

Measures similarity between workout vectors to recommend related exercises.

---

# 📂 Project Structure

```text
Workout-Recommender/
│
├── app.py
├── requirements.txt
├── README.md
├── workout.pkl
├── similarity.pkl
├── vectorizer.pkl
├── vectors.pkl
├── megaGymDataset.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│
└── Workout_suggester.ipynb
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Workout-Recommender.git
```

---

## 2. Navigate to Project Folder

```bash
cd Workout-Recommender
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📒 IMPORTANT — Run Notebook First

Before starting the Flask app, you MUST run:

```text
Workout_suggester.ipynb
```

The notebook:

- preprocesses the dataset
- builds the NLP pipeline
- generates vectors
- computes cosine similarity
- creates all required `.pkl` files

---

# 📦 Generated Pickle Files

Running the notebook generates:

```text
workout.pkl
vectorizer.pkl
vectors.pkl
similarity.pkl
```

These files are required for the Flask application to work.

---

# ▶️ Run Flask Application

After generating the pickle files:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# 🧠 Recommendation Logic

The recommendation system works by:

1. Selecting a workout
2. Converting workout descriptions into vectors
3. Calculating cosine similarity scores
4. Finding the most similar workouts
5. Returning top workout recommendations

---

# 📈 Future Improvements

- Workout image support
- User authentication
- Personalized recommendations
- Deep learning embeddings
- BERT/Sentence Transformers
- BMI-based recommendations
- Fitness goal filtering

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository and submit pull requests.

---

# 📄 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

### Hariharan G Nair

Built using Flask, NLP, and Machine Learning.
