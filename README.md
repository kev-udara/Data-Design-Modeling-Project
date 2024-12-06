Netflix Recommender System with MongoDB

This repository contains the implementation of a scalable Netflix-inspired movie and TV show recommender system using MongoDB. It leverages a structured dataset sourced from Kaggle’s Netflix Titles dataset, enriched with simulated user data and interactions. The project demonstrates efficient data modeling, querying, and performance analysis for personalized recommendations.

Features
	•	Data Import Script:
	•	Converts the Kaggle dataset into MongoDB collections (movies&shows, users, interactions).
	•	Simulates user profiles and interactions for real-world scenarios.
	•	Query Performance Analysis:
	•	Executes and benchmarks 24 custom queries.
	•	Measures execution time, result counts, and bottlenecks.
	•	Results logged into mongodb_query_performance.txt.
	•	Dataset Analysis:
	•	Computes memory footprint and field-wise statistics for each collection.
	•	Results logged into dataset_analysis.txt.

Dataset Overview

The dataset consists of three collections:
	1.	Movies & Shows Collection:
	•	Metadata for movies and TV shows.
	•	Fields: title, type, director, cast, country, date_added, release_year, rating, duration, genres, description.
	•	Approx. 6,000 records.
	2.	Users Collection:
	•	Simulated user profiles.
	•	Fields: user_id, name, age, country, preferences.
	•	5,000 users.
	3.	Interactions Collection:
	•	Tracks user interactions with movies/shows.
	•	Fields: interaction_id, user_id, show_id, user_rating, review, watched_date.
	•	50,000+ interactions.

Folder Structure

.
├── data/
│   ├── netflix_titles.csv                # Original dataset
│   ├── config.json                       # MongoDB configuration
├── scripts/
│   ├── import_data.py                    # Script to import and simulate data
│   ├── analyze_dataset.py                # Script to analyze dataset size
│   ├── query_performance.py              # Script to run and benchmark queries
├── outputs/
│   ├── dataset_analysis.txt              # Dataset analysis results
│   ├── mongodb_query_performance.txt     # Query performance results
├── README.md                             # Project documentation

How to Use

1. Setup MongoDB Connection

Update the config.json file with your MongoDB connection string:

{
    "MONGODB_URI": "your-mongodb-connection-string"
}

2. Run the Scripts
	•	Import Data:
Import the dataset into MongoDB and generate user data.

python scripts/import_data.py


	•	Analyze Dataset:
Analyze the dataset size and memory usage.

python scripts/analyze_dataset.py


	•	Run Queries:
Benchmark queries and log performance results.

python scripts/query_performance.py



3. Outputs
	•	dataset_analysis.txt:
Field-wise memory statistics and dataset size.
	•	mongodb_query_performance.txt:
Query execution times, result counts, and performance insights.

Key Queries
	1.	Retrieve all thrillers released after 2010.
	2.	List TV shows produced in the United States.
	3.	Find movies featuring a specific actor (e.g., Leonardo DiCaprio).
	4.	Count the number of movies by genre.
	5.	Recommend the highest-rated movies/shows.

For the complete list of queries, refer to the query_performance.py script.

Suggested Optimizations
	•	Indexing:
Add indexes on frequently queried fields (e.g., type, listed_in).
	•	Schema Design:
	•	Normalize repetitive fields like listed_in into separate collections.
	•	Denormalize critical fields for faster reads.
	•	Query Optimization:
Pre-filter data and avoid expensive operations like $regex on unindexed fields.
	•	Caching:
Use Redis for frequently queried data.
	•	Scaling:
Utilize sharding and replication for large-scale data distribution.

Requirements
	•	Python 3.7+
	•	MongoDB (Local or Atlas)
	•	Dependencies (install via pip install -r requirements.txt):
	•	pymongo
	•	datetime

Contributing

Contributions are welcome! Feel free to submit issues or pull requests for improvements.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

[Your Name]
Feel free to connect via GitHub or LinkedIn.

Acknowledgments
	•	Dataset sourced from Kaggle Netflix Titles Dataset.
