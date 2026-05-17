# Fake_News_Detector
A Machine Learning project that classifies news articles and headlines as Real or Fake. Built using Python, Scikit-Learn, and NLP techniques like TF-IDF vectorization.

# Technologies & Libraries Used
* Language: Python
* Data Manipulation: Pandas, NumPy
* Data Visualization: Matplotlib, Seaborn
* Natural Language Processing (NLP):** NLTK (Stopwords), Regular Expressions (regex)
* Machine Learning: Scikit-Learn (TF-IDF Vectorizer, Logistic Regression, Decision Tree Classifier)

1. Data Preprocessing: The text data is cleaned by removing punctuation, converting all text to lowercase, and filtering out common English stopwords (e.g., "the", "and", "is") to focus on the most important words.
2. Exploratory Data Analysis (EDA): Generates bar charts using `CountVectorizer` to visualize the most frequent words in the dataset.
3. Vectorization: Converts the cleaned text into numerical format using `TfidfVectorizer` so the Machine Learning models can understand it.
4. Model Training: The vectorized data is fed into both a **Logistic Regression** model and a **Decision Tree Classifier** to learn the patterns of real vs. fake news.
5. Evaluation: The models are evaluated using accuracy scores on both training and testing datasets.
6. Prediction: A custom script allows users to input their own news headlines to test the model's prediction in real-time.
