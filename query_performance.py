from pymongo import MongoClient
import time
import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def run_queries():
    config = load_config()
    client = MongoClient(config["MONGODB_URI"])
    db = client["movies&shows"]
    collection = db["movies&shows"]
    interactions_collection = db["interactions"]
    results = []

    def log_query(query_number, query_description, query_execution):
        """Execute the query and log results."""
        start_time = time.time()
        result = query_execution()
        end_time = time.time()
        results.append({
            "query_number": query_number,
            "query": query_description,
            "time": end_time - start_time,
            "count": len(result),
            "result": result[:5]  # Show only the first 5 results for clarity
        })

    # Query 1: Retrieve all Thrillers movies released after 2010
    log_query(
        1,
        "Retrieve all Thrillers movies released after 2010",
        lambda: list(collection.find(
            {"type": "Movie", "listed_in": "Thrillers", "release_year": {"$gt": 2010}},
            {"title": 1, "release_year": 1, "_id": 0}
        ))
    )

    # Query 2: Find all TV Shows from the United States
    log_query(
        2,
        "Find all TV Shows from the United States",
        lambda: list(collection.find(
            {"type": "TV Show", "country": "United States"},
            {"title": 1, "country": 1, "_id": 0}
        ))
    )

    # Query 3: Search for movies with a specific actor (Leonardo DiCaprio)
    log_query(
        3,
        "Search for movies with a specific actor (Leonardo DiCaprio)",
        lambda: list(collection.find(
            {"cast": "Leonardo DiCaprio"},
            {"title": 1, "cast": 1, "_id": 0}
        ))
    )

    # Query 4: Find titles added to Netflix in 2021
    log_query(
        4,
        "Find titles added to Netflix in 2021",
        lambda: list(collection.find(
            {"date_added": {"$regex": "2021"}},
            {"title": 1, "date_added": 1, "_id": 0}
        ))
    )

    # Query 5: Retrieve all titles with a PG-13 rating
    log_query(
        5,
        "Retrieve all titles with a PG-13 rating",
        lambda: list(collection.find(
            {"rating": "PG-13"},
            {"title": 1, "rating": 1, "_id": 0}
        ))
    )

    # Query 6: Search for movies with a duration greater than 120 minutes
    log_query(
        6,
        "Search for movies with a duration greater than 120 minutes",
        lambda: list(collection.find(
            {"type": "Movie", "duration.number": {"$gt": 120}},
            {"title": 1, "duration": 1, "_id": 0}
        ))
    )

    # Query 7: List all movies released between 2000 and 2010
    log_query(
        7,
        "List all movies released between 2000 and 2010",
        lambda: list(collection.find(
            {"type": "Movie", "release_year": {"$gte": 2000, "$lte": 2010}},
            {"title": 1, "release_year": 1, "_id": 0}
        ))
    )

    # Query 8: Count the number of movies by genre
    log_query(
        8,
        "Count the number of movies by genre",
        lambda: list(collection.aggregate([
            {"$match": {"type": "Movie"}},
            {"$unwind": "$listed_in"},
            {"$group": {"_id": "$listed_in", "count": {"$sum": 1}}},
            {"$project": {"genre": "$_id", "count": 1, "_id": 0}}
        ]))
    )

    # Query 9: Average duration of movies per genre
    log_query(
        9,
        "Average duration of movies per genre",
        lambda: list(collection.aggregate([
            {"$match": {"type": "Movie"}},
            {"$unwind": "$listed_in"},
            {"$group": {"_id": "$listed_in", "avg_duration": {"$avg": "$duration.number"}}},
            {"$project": {"genre": "$_id", "avg_duration": 1, "_id": 0}}
        ]))
    )

    # Query 10: Count TV Shows per country
    log_query(
        10,
        "Count TV Shows per country",
        lambda: list(collection.aggregate([
            {"$match": {"type": "TV Show"}},
            {"$unwind": "$country"},
            {"$group": {"_id": "$country", "count": {"$sum": 1}}},
            {"$project": {"country": "$_id", "count": 1, "_id": 0}}
        ]))
    )

    # Query 11: Find the total duration of all movies in each genre
    log_query(
        11,
        "Find the total duration of all movies in each genre",
        lambda: list(collection.aggregate([
            {"$match": {"type": "Movie"}},
            {"$unwind": "$listed_in"},
            {"$group": {"_id": "$listed_in", "total_duration": {"$sum": "$duration.number"}}},
            {"$project": {"genre": "$_id", "total_duration": 1, "_id": 0}}
        ]))
    )

    # Query 12: Identify the top 5 most common genres for movies
    log_query(
        12,
        "Identify the top 5 most common genres for movies",
        lambda: list(collection.aggregate([
            {"$match": {"type": "Movie"}},
            {"$unwind": "$listed_in"},
            {"$group": {"_id": "$listed_in", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 5},
            {"$project": {"genre": "$_id", "count": 1, "_id": 0}}
        ]))
    )

    # Query 13: Find titles directed by Christopher Nolan, grouped by type
    log_query(
        13,
        "Find titles directed by Christopher Nolan, grouped by type",
        lambda: list(collection.aggregate([
            {"$match": {"director": "Christopher Nolan"}},
            {"$group": {"_id": "$type", "titles": {"$push": "$title"}}},
            {"$project": {"type": "$_id", "titles": 1, "_id": 0}}
        ]))
    )

    # Query 14: List the genres of movies added to Netflix in 2020
    log_query(
        14,
        "List the genres of movies added to Netflix in 2020",
        lambda: list(collection.aggregate([
            {"$match": {"type": "Movie", "date_added": {"$regex": "2020"}}},
            {"$unwind": "$listed_in"},
            {"$group": {"_id": "$listed_in", "count": {"$sum": 1}}},
            {"$project": {"genre": "$_id", "count": 1, "_id": 0}}
        ]))
    )

    # Query 15: Find all actors who appeared in more than 3 movies
    log_query(
        15,
        "Find all actors who appeared in more than 3 movies",
        lambda: list(collection.aggregate([
            {"$unwind": "$cast"},
            {"$group": {"_id": "$cast", "count": {"$sum": 1}}},
            {"$match": {"count": {"$gt": 3}}},
            {"$project": {"actor": "$_id", "count": 1, "_id": 0}}
        ]))
    )

    # # Query 16: Add a new genre to a movie
    # log_query(
    #     16,
    #     "Add a new genre to a movie",
    #     lambda: [db["movies&shows"].update_one(
    #         {"show_id": "s1"}, {"$push": {"listed_in": "Adventure"}}
    #     )]
    # )

    # # Query 17: Update the rating of a specific movie
    # log_query(
    #     17,
    #     "Update the rating of a specific movie",
    #     lambda: [db["movies&shows"].update_one(
    #         {"show_id": "s2"}, {"$set": {"rating": "R"}}
    #     )]
    # )

    # # Query 18: Change the release year of a title
    # log_query(
    #     18,
    #     "Change the release year of a title",
    #     lambda: [db["movies&shows"].update_one(
    #         {"show_id": "s3"}, {"$set": {"release_year": 2020}}
    #     )]
    # )

    # # Query 19: Delete a specific movie by ID
    # log_query(
    #     19,
    #     "Delete a specific movie by ID",
    #     lambda: [db["movies&shows"].delete_one({"show_id": "s100"})]
    # )

    # # Query 20: Remove all TV Shows from 2015
    # log_query(
    #     20,
    #     "Remove all TV Shows from 2015",
    #     lambda: [db["movies&shows"].delete_many({"type": "TV Show", "release_year": 2015})]
    # )

    # Query 21: Find the most watched movies (Top 5)
    log_query(
        21,
        "Find the most watched movies (Top 5)",
        lambda: list(interactions_collection.aggregate([
            {"$group": {"_id": "$show_id", "watch_count": {"$sum": 1}}},
            {"$sort": {"watch_count": -1}},
            {"$limit": 5},
            {"$lookup": {
                "from": "movies&shows",
                "localField": "_id",
                "foreignField": "show_id",
                "as": "movie_info"
            }},
            {"$project": {
                "title": {"$arrayElemAt": ["$movie_info.title", 0]},
                "watch_count": 1,
                "_id": 0
            }}
        ]))
    )

    # Query 22: Recommend the highest-rated movies/shows across all users (Top 5)
    log_query(
        22,
        "Recommend the highest-rated movies/shows across all users (Top 5)",
        lambda: list(interactions_collection.aggregate([
            {"$group": {
                "_id": "$show_id",
                "average_rating": {"$avg": "$rating"},
                "total_ratings": {"$sum": 1}
            }},
            {"$sort": {"average_rating": -1, "total_ratings": -1}},
            {"$limit": 5},
            {"$lookup": {
                "from": "movies&shows",
                "localField": "_id",
                "foreignField": "show_id",
                "as": "movie_info"
            }},
            {"$project": {
                "title": {"$arrayElemAt": ["$movie_info.title", 0]},
                "type": {"$arrayElemAt": ["$movie_info.type", 0]},
                "total_ratings": 1,
                "_id": 0
            }}
        ]))
    )

    # Query 23: Aggregate movies and TV shows by the number of countries involved
    log_query(
        23,
        "Aggregate movies and TV shows by the number of countries involved",
        lambda: list(collection.aggregate([
            {"$project": {"title": 1, "country_count": {"$size": "$country"}, "_id": 0}},
            {"$sort": {"country_count": -1}},
            {"$limit": 5}
        ]))
    )

    # Query 24: Find all genres with the average release year of titles
    log_query(
        24,
        "Find all genres with the average release year of titles",
        lambda: list(collection.aggregate([
            {"$unwind": "$listed_in"},
            {"$group": {"_id": "$listed_in", "avg_release_year": {"$avg": "$release_year"}}},
            {"$project": {"genre": "$_id", "avg_release_year": {"$round": ["$avg_release_year", 0]}, "_id": 0}}
        ]))
    )

    # Write results to a file
    with open("mongodb_query_performance.txt", "w", encoding="utf-8") as f:
        for res in results:
            f.write(f"Query {res['query_number']}: {res['query']}\n")
            f.write(f"Result Count: {res['count']}\n")
            f.write(f"Execution Time: {res['time']:.4f} seconds\n")
            f.write(f"Result (Sample): {res['result']}\n")
            f.write("-" * 80 + "\n")

    print("Query results written to 'mongodb_query_performance.txt'.")

if __name__ == "__main__":
    run_queries()