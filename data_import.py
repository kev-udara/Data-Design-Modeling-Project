import csv
import random
import json
from pymongo import MongoClient
from datetime import datetime, timedelta

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def parse_duration(duration_str):
    if duration_str:
        parts = duration_str.strip().split(' ', 1)
        if len(parts) == 2:
            number, unit = parts
            return {"number": int(number), "unit": unit}
    return {"number": None, "unit": None}

def generate_name():
    first_names = ["John", "Emma", "Oliver", "Sophia", "William", "Ava", "James", "Mia", "Benjamin", "Charlotte"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_user_id(name, index):
    first_name = name.split()[0].lower()
    return f"{first_name}_{str(index).zfill(3)}"

def create_users(num_users):
    countries = ["United States", "India", "United Kingdom", "Canada", "Germany"]
    preferences = ["Action", "Comedy", "Drama", "Sci-Fi", "Horror"]
    users = []

    for i in range(1, num_users + 1):
        name = generate_name()
        user = {
            "user_id": generate_user_id(name, i),  # Generate user ID based on name and index
            "name": name,
            "age": random.randint(18, 65),
            "country": random.choice(countries),
            "preferences": random.sample(preferences, random.randint(1, 3))
        }
        users.append(user)
    return users

def create_interactions(users, shows):
    interactions = []
    for user in users:
        for _ in range(random.randint(1, 20)):  # Random number of interactions per user
            show = random.choice(shows)
            interaction = {
                "interaction_id": f"interaction_{len(interactions) + 1}",
                "user_id": user["user_id"],           # Link interaction to user ID
                "show_id": show["show_id"],           # Link interaction to show ID
                "user_rating": round(random.uniform(1, 5), 1),  
                "review": f"Review by {user['name']} for {show['title']}",
                "watched_date": (datetime.now() - timedelta(days=random.randint(1, 365))).isoformat()
            }
            interactions.append(interaction)
    return interactions

def main():
    input_csv = 'netflix_titles.csv'
    config = load_config()

    # Movies and Shows collection
    shows = []
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            show = {
                "show_id": row['show_id'],
                "type": row['type'],
                "title": row['title'],
                "director": [d.strip() for d in row['director'].split(',')] if row['director'] else [],
                "cast": [c.strip() for c in row['cast'].split(',')] if row['cast'] else [],
                "country": [c.strip() for c in row['country'].split(',')] if row['country'] else [],
                "date_added": datetime.strptime(row['date_added'].strip(), '%B %d, %Y').isoformat() if row['date_added'] else None,
                "release_year": int(row['release_year']) if row['release_year'] else None,
                "listed_in": [g.strip() for g in row['listed_in'].split(',')] if row['listed_in'] else [],
                "rating": row['rating'] if row['rating'] else None,
                "duration": parse_duration(row['duration']) if row['duration'] else {"number": None, "unit": None},
                "description": row['description'] if row['description'] else None
            }
            shows.append(show)

    # Users collection
    users = create_users(5000)  

    # Interactions collection
    interactions = create_interactions(users, shows)

    # Connect to MongoDB
    client = MongoClient(config["MONGODB_URI"])
    db = client["movies&shows"]  

    # Insert into collections
    db["movies&shows"].delete_many({})  # Clear existing data
    db["movies&shows"].insert_many(shows)
    print(f"Inserted {len(shows)} documents into 'movies&shows' collection.")

    db["users"].delete_many({})  # Clear existing data
    db["users"].insert_many(users)
    print(f"Inserted {len(users)} documents into 'users' collection.")

    db["interactions"].delete_many({})  # Clear existing data
    db["interactions"].insert_many(interactions)
    print(f"Inserted {len(interactions)} documents into 'interactions' collection.")

    print("Data successfully inserted into MongoDB.")

if __name__ == '__main__':
    main()