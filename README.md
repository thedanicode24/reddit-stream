# Real-Time Sentiment Analysis (Reddit Edition)

## Overview
This project performs **real-time sentiment analysis** of comments on Reddit.  
Originally, it was designed to analyze tweets in real-time using Spark, but after Twitter/X restricted free API access in February 2023, the project was adapted to work with Reddit.

The project is still ongoing and uses Python in Jupyter Notebook for data collection, analysis, and visualization.

## Features
- Real-time streaming of Reddit comments using **PRAW**.
- Sentiment classification of comments into five categories:
  - `strongly_negative`
  - `negative`
  - `neutral`
  - `positive`
  - `strongly_positive`
- Visualization of sentiment trends over time with:
  - **Stacked bar charts** for total sentiment counts.
  - **Stacked line plots** to highlight cumulative trends.
- Time aggregation at configurable intervals (e.g., per minute).

## Technologies
The project uses the following Python libraries:

- `matplotlib==3.10.5` – plotting and visualization  
- `numpy==2.3.2` – numerical computations  
- `pandas==2.3.1` – data manipulation  
- `praw==7.8.1` – Reddit API access and comment streaming  
- `nltk==3.9.1` – natural language processing, including sentiment analysis  

## Usage
1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Configure your Reddit API credentials in PRAW. You will need:
   - `client_id`
   - `client_secret`
   - `user_agent`

   Example configuration in your notebook:

   ```python
   import praw

   reddit = praw.Reddit(
       client_id="YOUR_CLIENT_ID",
       client_secret="YOUR_CLIENT_SECRET",
       user_agent="YOUR_USER_AGENT"
   )
Run the Jupyter Notebook to start streaming comments and analyzing sentiment data in real-time.
Customize parameters such as:
Subreddit(s) to track
Time aggregation intervals
Sentiment categories or analysis method

## Notes
- The project is designed for educational and research purposes.
- Since Reddit is the data source, an API account is required to fetch comments in real-time.
- The sentiment analysis module can be customized or replaced with more advanced models if needed.


## Future Work
- Extend sentiment analysis with pre-trained NLP models (e.g., transformers).
- Support multiple subreddits simultaneously.
- Implement a live dashboard that updates in real-time.