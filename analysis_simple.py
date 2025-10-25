#!/usr/bin/env python3
"""
MovieLens Dataset Analysis - Stage 1: Feature Engineering & Exploration
Author: Adu Morenikeji Toluwalope
Date: October 2025
Dataset: MovieLens ml-latest-small
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print("=== MOVIELENS DATASET ANALYSIS - STAGE 1 ===")
print("Libraries imported successfully!")
print()

# Load the datasets
print("Loading datasets...")
ratings = pd.read_csv('ml-latest-small/ratings.csv')
movies = pd.read_csv('ml-latest-small/movies.csv')
tags = pd.read_csv('ml-latest-small/tags.csv')
links = pd.read_csv('ml-latest-small/links.csv')

print("Dataset shapes:")
print(f"Ratings: {ratings.shape}")
print(f"Movies: {movies.shape}")
print(f"Tags: {tags.shape}")
print(f"Links: {links.shape}")
print()

# Data Quality Check
print("=== DATA QUALITY CHECK ===")
print("Duplicates:")
print(f"Ratings duplicates: {ratings.duplicated().sum()}")
print(f"Movies duplicates: {movies.duplicated().sum()}")

print("\nMissing values:")
print("Ratings missing values:", ratings.isnull().sum().sum())
print("Movies missing values:", movies.isnull().sum().sum())
print()

# Merge datasets
df = pd.merge(ratings, movies, on='movieId', how='inner')
print(f"Merged dataset shape: {df.shape}")

# Convert timestamp to datetime
df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
print(f"Date range: {df['datetime'].min()} to {df['datetime'].max()}")
print()

print("=== FEATURE ENGINEERING ===")

# Feature 1: Extract release year from movie title
def extract_year(title):
    try:
        year = title.split('(')[-1].split(')')[0]
        if year.isdigit() and len(year) == 4:
            return int(year)
        return None
    except:
        return None

df['release_year'] = df['title'].apply(extract_year)
print(f"Feature 1 - Release Year: {df['release_year'].notna().sum()} movies with valid years")

# Feature 2: Count number of genres per movie
df['genre_count'] = df['genres'].apply(lambda x: len(x.split('|')) if x != '(no genres listed)' else 0)
print(f"Feature 2 - Genre Count: Average {df['genre_count'].mean():.2f} genres per movie")

# Feature 3: Movie age at time of rating
df['rating_year'] = df['datetime'].dt.year
df['movie_age_at_rating'] = df['rating_year'] - df['release_year']
print(f"Feature 3 - Movie Age at Rating: Average {df['movie_age_at_rating'].mean():.2f} years")

# Feature 4: Rating time features
df['rating_hour'] = df['datetime'].dt.hour
df['rating_day_of_week'] = df['datetime'].dt.dayofweek
df['rating_month'] = df['datetime'].dt.month
print(f"Feature 4 - Temporal Features: Hour, day of week, month extracted")

# Feature 5: Movie popularity
movie_popularity = df.groupby('movieId')['rating'].count().reset_index()
movie_popularity.columns = ['movieId', 'popularity_score']
df = pd.merge(df, movie_popularity, on='movieId', how='left')
print(f"Feature 5 - Movie Popularity: Average {df['popularity_score'].mean():.2f} ratings per movie")

# Feature 6: Average rating per movie
movie_avg_rating = df.groupby('movieId')['rating'].mean().reset_index()
movie_avg_rating.columns = ['movieId', 'avg_movie_rating']
df = pd.merge(df, movie_avg_rating, on='movieId', how='left')
print(f"Feature 6 - Average Movie Rating: Overall average {df['avg_movie_rating'].mean():.2f}")

# Feature 7: User activity level
user_activity = df.groupby('userId')['rating'].count().reset_index()
user_activity.columns = ['userId', 'user_activity_level']
df = pd.merge(df, user_activity, on='userId', how='left')
print(f"Feature 7 - User Activity Level: Average {df['user_activity_level'].mean():.2f} ratings per user")

# Feature 8: Decade categorization
def categorize_decade(year):
    if pd.isna(year):
        return 'Unknown'
    elif year < 1950:
        return 'Pre-1950'
    elif year < 1960:
        return '1950s'
    elif year < 1970:
        return '1960s'
    elif year < 1980:
        return '1970s'
    elif year < 1990:
        return '1980s'
    elif year < 2000:
        return '1990s'
    elif year < 2010:
        return '2000s'
    else:
        return '2010s+'

df['decade'] = df['release_year'].apply(categorize_decade)
print(f"Feature 8 - Decade Categories created")
print()

# Save enhanced dataset
df.to_csv('enhanced_movielens_dataset.csv', index=False)
print("Enhanced dataset saved as 'enhanced_movielens_dataset.csv'")
print()

print("=== EXPLORATORY DATA ANALYSIS ===")

# Basic statistics
print("BASIC STATISTICS:")
print(f"Total users: {df['userId'].nunique():,}")
print(f"Total movies: {df['movieId'].nunique():,}")
print(f"Total ratings: {len(df):,}")
print(f"Average rating: {df['rating'].mean():.2f}")
print()

# Generate key insights
print("=== 6 KEY INSIGHTS FROM ANALYSIS ===")
print()

# Insight 1: Rating Distribution
print("INSIGHT 1 - RATING PATTERNS:")
most_common_rating = df['rating'].mode().iloc[0]
high_ratings_pct = (df['rating'] >= 3.5).mean() * 100
print(f"- Users tend to rate movies positively - {high_ratings_pct:.1f}% of ratings are 3.5+ stars")
print(f"- Most common rating is {most_common_rating} stars")
print()

# Insight 2: Movie Popularity
print("INSIGHT 2 - MOVIE POPULARITY DISTRIBUTION:")
most_popular_movie = df.groupby('title')['rating'].count().idxmax()
most_popular_count = df.groupby('title')['rating'].count().max()
avg_ratings_per_movie = df['popularity_score'].mean()
print(f"- Most popular movie: '{most_popular_movie}' with {most_popular_count} ratings")
print(f"- Average movie receives only {avg_ratings_per_movie:.1f} ratings")
print()

# Insight 3: Genre Analysis
print("INSIGHT 3 - GENRE PREFERENCES:")
all_genres = []
for genres in df['genres'].unique():
    if genres != '(no genres listed)':
        all_genres.extend(genres.split('|'))
most_common_genre = pd.Series(all_genres).mode().iloc[0]
avg_genres = df['genre_count'].mean()
print(f"- Most common genre: '{most_common_genre}'")
print(f"- Movies average {avg_genres:.1f} genres")
print()

# Insight 4: Temporal Patterns
print("INSIGHT 4 - TEMPORAL RATING BEHAVIOR:")
peak_hour = df.groupby('rating_hour')['rating'].count().idxmax()
peak_day = df.groupby('rating_day_of_week')['rating'].count().idxmax()
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(f"- Peak rating activity occurs at {peak_hour}:00")
print(f"- Most active day: {days[peak_day]}")
print()

# Insight 5: User Engagement
print("INSIGHT 5 - USER ENGAGEMENT PATTERNS:")
max_user_activity = df['user_activity_level'].max()
avg_user_activity = df['user_activity_level'].mean()
heavy_users = (df['user_activity_level'] >= 100).sum()
print(f"- Most active user rated {max_user_activity} movies")
print(f"- Average user rates {avg_user_activity:.1f} movies")
print(f"- {heavy_users} users rated 100+ movies")
print()

# Insight 6: Movie Age Impact
print("INSIGHT 6 - MOVIE AGE AND RATINGS:")
decade_ratings = df.groupby('decade')['rating'].mean().sort_values(ascending=False)
best_decade = decade_ratings.index[0]
best_decade_rating = decade_ratings.iloc[0]
avg_movie_age = df['movie_age_at_rating'].mean()
print(f"- {best_decade} movies have highest average rating ({best_decade_rating:.2f})")
print(f"- Average movie is {avg_movie_age:.1f} years old when rated")
print()

print("=== FEATURE ENGINEERING SUMMARY ===")
print("Successfully created 8 new features:")
print("1. release_year - Extracted from movie titles")
print("2. genre_count - Number of genres per movie")
print("3. movie_age_at_rating - Movie age when rated")
print("4. rating_hour/day_of_week/month - Temporal features")
print("5. popularity_score - Number of ratings per movie")
print("6. avg_movie_rating - Average rating per movie")
print("7. user_activity_level - Number of ratings per user")
print("8. decade - Movie decade category")
print()

print("=== ANALYSIS COMPLETE ===")
print("Files created:")
print("- enhanced_movielens_dataset.csv (cleaned dataset with new features)")
print("- movielens_analysis.ipynb (Jupyter notebook)")
print()
print("Next steps:")
print("1. Open Jupyter notebook: jupyter notebook movielens_analysis.ipynb")
print("2. Run all cells to generate visualizations")
print("3. Export notebook as PDF")
print("4. Create 6-page report using insights above")