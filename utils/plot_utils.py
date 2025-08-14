import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from io import BytesIO
from PIL import Image
from rembg import remove
from wordcloud import WordCloud

def plot_time_series(data, 
                     interval_minutes=5, 
                     figsize=(12,8), 
                     title="Time Series (stacked bar + stacked line)",
                     xlabel="Time",
                     ylabel="Count",
                     width=0.7):

    datetime_series = pd.to_datetime(data)
    
    intervals = datetime_series.dt.floor(f'{interval_minutes}min').dt.strftime('%H:%M')
    
    counts_by_interval = intervals.value_counts().sort_index()
    
    x_labels = counts_by_interval.index
    y_values = counts_by_interval.values
    
    plt.figure(figsize=figsize)
    plt.bar(x_labels, y_values, width=width, alpha=0.4, label="Counts")
    plt.plot(x_labels, y_values, marker="o", color="blue", label="Trend")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, axis='y')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_sentiment_over_time(data, 
                             interval_minutes=1, 
                             bar_labels=None, 
                             line_labels=None,
                             title="Sentiment over time (stacked bar + stacked line)",
                             xlabel="Time",
                             ylabel="Count",
                             figsize=(12,8),
                             has_legend=True):
    
    df = data.copy()
    
    default_categories = ["strongly_negative", "negative", "neutral", "positive", "strongly_positive"]
    if bar_labels is None:
        bar_labels = [f"{cat} (bar)" for cat in default_categories]
    if line_labels is None:
        line_labels = [f"{cat} (stacked line)" for cat in default_categories]

    df['datetime'] = pd.to_datetime(df['datetime'])
    df['interval'] = df['datetime'].dt.floor(f'{interval_minutes}min').dt.strftime('%H:%M')

    time_counts = df.groupby(['interval', 'sentiment']).size().unstack(fill_value=0)
    
    for cat in default_categories:
        if cat not in time_counts.columns:
            time_counts[cat] = 0
    
    time_counts = time_counts.sort_index()
    intervals = time_counts.index.tolist()
    
    values = {cat: time_counts[cat].values for cat in default_categories}

    plt.figure(figsize=figsize)

    # Stacked bar
    bottom = np.zeros(len(intervals))
    colors_bar = ["#8B0000", "#FF0000", "#808080", "#00FF00", "#006400"]
    for cat, color, label in zip(default_categories, colors_bar, bar_labels):
        plt.bar(intervals, values[cat], bottom=bottom, color=color, alpha=0.5, label=label)
        bottom += values[cat]

    # Stacked line
    cumulative = np.zeros(len(intervals))
    colors_line = ["#FF6347", "#FF4500", "#A9A9A9", "#32CD32", "#228B22"]
    for cat, color, label in zip(default_categories, colors_line, line_labels):
        cumulative += values[cat]
        plt.plot(intervals, cumulative, marker="o", color=color, label=label)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    if has_legend:
        plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def plot_wordcloud(url_img, testo, figsize=(12,8)):
    response = requests.get(url_img)
    img = Image.open(BytesIO(response.content))
    
    img_no_bg = remove(img)
    
    mask = img_no_bg.convert("L")
    mask = np.array(mask)
    mask = np.where(mask > 128, 255, 0)
    
    wc = WordCloud(width=800, height=400, background_color="white",
                   mask=mask, contour_color='black', contour_width=1).generate(testo)
    
    plt.figure(figsize=figsize)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()