# MovieLens Dataset Analysis Report - Stage 1
## Feature Engineering & Exploratory Data Analysis

**Author:** Adu Morenikeji Toluwalope  
**Date:** October 2025  
**Dataset:** MovieLens ml-latest-small  
**HNG Internship - Data Analytics Track**

---

## Executive Summary

This report presents a comprehensive analysis of the MovieLens dataset, focusing on feature engineering and exploratory data analysis. The analysis successfully created 8 new features and uncovered 6 key insights that will support future recommendation system development.

**Key Results:**
- Processed 100,836 ratings from 610 users on 9,724 movies
- Created 8 meaningful features for recommendation systems
- Identified significant patterns in user behavior and movie characteristics
- Generated actionable insights for recommendation algorithm design

---

## 1. Dataset Overview

### 1.1 Data Sources
The MovieLens ml-latest-small dataset consists of four main files:

| Dataset | Records | Description |
|---------|---------|-------------|
| ratings.csv | 100,836 | User ratings (userId, movieId, rating, timestamp) |
| movies.csv | 9,742 | Movie metadata (movieId, title, genres) |
| tags.csv | 3,683 | User-generated tags |
| links.csv | 9,742 | External database links |

### 1.2 Data Quality Assessment
- **No duplicate records** found in primary datasets
- **No missing values** in core rating and movie data
- **Clean data quality** with consistent formatting
- **Date range:** March 1996 to September 2018 (22+ years of data)

---

## 2. Feature Engineering

### 2.1 Methodology
Created 8 new features to enhance the dataset for recommendation systems:

### 2.2 Feature Descriptions

#### Feature 1: Release Year
- **Method:** Extracted from movie titles using regex parsing
- **Coverage:** 100,818 movies (99.98% success rate)
- **Range:** 1902 to 2018
- **Value:** Enables era-based recommendations and temporal analysis

#### Feature 2: Genre Count
- **Method:** Count genres per movie (split by '|' delimiter)
- **Range:** 0 to 10 genres per movie
- **Average:** 2.7 genres per movie
- **Value:** Indicates movie complexity and broad appeal potential

#### Feature 3: Movie Age at Rating
- **Method:** Calculate difference between rating year and release year
- **Average:** 13.3 years
- **Value:** Captures user preferences for new vs classic films

#### Feature 4: Temporal Features
- **Components:** Rating hour, day of week, month
- **Peak Activity:** 8:00 PM, Monday
- **Value:** Enables time-aware recommendation delivery

#### Feature 5: Popularity Score
- **Method:** Count total ratings per movie
- **Average:** 58.8 ratings per movie
- **Range:** 1 to 329 ratings
- **Value:** Addresses cold start and long tail problems

#### Feature 6: Average Movie Rating
- **Method:** Calculate mean rating per movie
- **Overall Average:** 3.50/5.0
- **Value:** Quality indicator for recommendation filtering

#### Feature 7: User Activity Level
- **Method:** Count total ratings per user
- **Average:** 603.9 ratings per user
- **Range:** 20 to 2,698 ratings
- **Value:** Indicates user engagement and data reliability

#### Feature 8: Decade Categories
- **Method:** Categorize movies into decade buckets
- **Categories:** Pre-1950, 1950s, 1960s, 1970s, 1980s, 1990s, 2000s, 2010s+
- **Value:** Enables era-based clustering and recommendations

---

## 3. Exploratory Data Analysis

### 3.1 Key Statistics
- **Total Users:** 610
- **Total Movies:** 9,724
- **Total Ratings:** 100,836
- **Average Rating:** 3.50/5.0
- **Rating Distribution:** Positively skewed (61.2% are 3.5+ stars)

---

## 4. Six Key Insights

### 4.1 Insight 1: Rating Patterns
**Finding:** Users exhibit positive rating bias
- 61.2% of ratings are 3.5 stars or higher
- Most common rating is 4.0 stars
- **Implication:** Users primarily rate movies they expect to like, creating selection bias

### 4.2 Insight 2: Movie Popularity Distribution
**Finding:** Highly skewed popularity distribution
- Most popular movie: "Forrest Gump (1994)" with 329 ratings
- Average movie receives only 58.8 ratings
- **Implication:** Creates "long tail" problem requiring specialized algorithms for niche content

### 4.3 Insight 3: Genre Preferences
**Finding:** Drama dominates, multi-genre movies are common
- Most common genre: Drama
- Movies average 2.7 genres each
- **Implication:** Multi-genre movies may appeal to broader audiences, enabling cross-genre recommendations

### 4.4 Insight 4: Temporal Rating Behavior
**Finding:** Clear patterns in rating activity
- Peak activity: 8:00 PM (evening leisure time)
- Most active day: Monday
- **Implication:** Temporal features can optimize recommendation timing and delivery

### 4.5 Insight 5: User Engagement Patterns
**Finding:** Wide variation in user activity levels
- Most active user: 2,698 ratings
- Average user: 603.9 ratings
- Heavy users (100+ ratings): 84,313 instances
- **Implication:** User activity levels should inform recommendation confidence and algorithm selection

### 4.6 Insight 6: Movie Age and Quality
**Finding:** Era effects on movie ratings
- Highest rated decade: 1950s (3.85 average rating)
- Average movie age when rated: 13.3 years
- **Implication:** Older movies show survivorship bias; only quality films remain popular over time

---

## 5. Recommendation System Applications

### 5.1 Content-Based Filtering
**Applicable Features:**
- Genre count and categories
- Release year and decade
- Average movie rating
- Movie age patterns

**Use Cases:**
- "Movies similar to X" recommendations
- Genre-based filtering and discovery
- Era-specific recommendations

### 5.2 Collaborative Filtering
**Applicable Features:**
- User activity levels
- Temporal rating patterns
- Popularity scores

**Use Cases:**
- User-user similarity calculations
- Item-item collaborative filtering
- Activity-weighted recommendations

### 5.3 Hybrid Systems
**Combined Approach:**
- Balance popularity with personalization
- Use temporal features for timing
- Leverage user activity for confidence scoring
- Apply genre diversity for exploration

### 5.4 Cold Start Mitigation
**Strategies:**
- Use movie features for new users
- Leverage popularity scores for new items
- Apply temporal patterns for timing optimization

---

## 6. Technical Implementation

### 6.1 Data Processing Pipeline
1. **Data Loading:** Multi-file CSV ingestion
2. **Quality Checks:** Duplicate and missing value detection
3. **Feature Engineering:** 8 new feature creation
4. **Data Integration:** Merge operations with validation
5. **Export:** Enhanced dataset generation

### 6.2 Feature Engineering Code Structure
```python
# Example feature creation
df['release_year'] = df['title'].apply(extract_year)
df['genre_count'] = df['genres'].apply(lambda x: len(x.split('|')))
df['movie_age_at_rating'] = df['rating_year'] - df['release_year']
```

### 6.3 Performance Metrics
- **Processing Time:** < 5 seconds for full dataset
- **Memory Usage:** Efficient pandas operations
- **Feature Coverage:** 99.98% success rate for year extraction

---

## 7. Conclusions and Future Work

### 7.1 Key Achievements
✅ **Data Preparation:** Successfully cleaned and integrated multi-file dataset  
✅ **Feature Engineering:** Created 8 meaningful features for recommendation systems  
✅ **Insight Generation:** Discovered 6 actionable insights about user behavior  
✅ **System Readiness:** Enhanced dataset prepared for advanced analytics  

### 7.2 Recommendation System Readiness
The enhanced dataset now supports:
- **Advanced collaborative filtering algorithms**
- **Content-based recommendation engines**
- **Hybrid recommendation approaches**
- **Temporal and popularity-aware systems**

### 7.3 Future Enhancements
1. **Advanced NLP:** Process user tags for semantic features
2. **External Data:** Integrate IMDb/TMDb metadata via links
3. **Deep Learning:** Prepare features for neural collaborative filtering
4. **Real-time Systems:** Design features for streaming recommendations

### 7.4 Business Impact
- **Improved Recommendations:** Better user experience through enhanced features
- **Cold Start Solutions:** New user/item handling capabilities
- **Personalization:** Activity-based recommendation confidence
- **Temporal Optimization:** Time-aware recommendation delivery

---

## 8. Deliverables

### 8.1 Files Created
1. **enhanced_movielens_dataset.csv** - Cleaned dataset with 8 new features
2. **movielens_analysis.ipynb** - Complete Jupyter notebook with visualizations
3. **MovieLens_Analysis_Report.pdf** - This comprehensive report
4. **analysis_simple.py** - Reproducible analysis script

### 8.2 Technical Specifications
- **Programming Language:** Python 3.11
- **Key Libraries:** pandas, numpy, matplotlib, seaborn
- **Dataset Size:** 100,836 records with 15 features
- **Processing Environment:** Windows 11, Jupyter Notebook

---

**Report prepared for HNG Internship - Data Analytics Track Stage 1**  
**Submission Date:** October 2025