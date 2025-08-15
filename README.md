# Real-Time Sentiment Analysis (Reddit Edition)

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.2.6-blue?logo=NumPy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.3.1-lightblue?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.5-orange?logo=matplotlib&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.7.1-yellow?logo=scikitlearn&logoColor=black)
![NLTK](https://img.shields.io/badge/NLTK-3.9.1-lightgrey?logo=nltk&logoColor=black)

## 📌 Overview
This project analyzes comments from a specific subreddit on Reddit. It focuses on understanding user sentiment, identifying common topics, and visualizing frequently used words. The analysis is divided into multiple tasks using Python libraries for text processing, visualization, and topic modeling.
Originally, it was designed to analyze tweets in real-time using Spark, but after Twitter/X restricted free API access in February 2023, the project was adapted to work with Reddit.

The project is still ongoing and uses Python in Jupyter Notebook for data collection, analysis, and visualization.

⚠️ **Important**: This project requires Python 3.10. Newer versions may not work correctly.

## 📫 Features
- Real-time streaming of Reddit comments using **PRAW**.
- Sentiment classification of comments into five categories using **NLTK VADER**
  - `strongly_negative`
  - `negative`
  - `neutral`
  - `positive`
  - `strongly_positive`
- Visualization of sentiment trends over time with:
  - **Stacked bar charts** for total sentiment counts.
  - **Stacked line plots** to highlight cumulative trends.
- Word Cloud Visualization
- Topic Modeling using **TF-IDF** vectorization and **Latent Dirichlet Allocation**.

## 🔜 Future Improvements
- Emotion detection using NRC Emotion Lexicon.
- Advanced sentiment models using transformer-based approaches (e.g., BERT).

## 🛠 Technologies
- **Python 3.10** – main programming language, required for compatibility  
- **Pandas & NumPy** – data manipulation and numerical computations  
- **NLTK (VADER)** – sentiment analysis  
- **scikit-learn** – TF-IDF vectorization and topic modeling  
- **Gensim** – LDA modeling  
- **PyLDAVis** – interactive topic visualization  
- **Matplotlib & Seaborn** – data visualization  
- **WordCloud** – generating word cloud visualizations  
- **PRAW** – accessing Reddit API for comment extraction  

## 📦 Usage
1. Clone the repository:
```bash
git clone https://github.com/thedanicode24/reddit-stream.git
cd reddit-stream
```

2. Create a virtual environment:
```bash
python3.10 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## ❗️ Reddit API Credentials
This project requires Reddit API credentials to work.
1. Create a Reddit app at https://www.reddit.com/prefs/apps.
2. Copy your client_id, client_secret, username, and password.
3. Create a credentials.env file with the following format:
```init
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
USERNAME=your_reddit_username
PASSWORD=your_reddit_password
```
4. Make sure the .env file is ignored by Git (included in .gitignore).

## 📜 License
This project is licensed under the MIT License.