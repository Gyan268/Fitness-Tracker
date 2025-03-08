import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def print_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print("Response:")
        print(json.dumps(response.json(), indent=2))
    except Exception:
        print("No JSON response.")
    print("------\n")

# Register User 1
print("Registering User 1 (Gyan)...")
response = requests.post(f"{BASE_URL}/user", json={"name": "Gyan", "age": 21})
print_response(response)
user1_id = response.json().get("id")

# Register User 2
print("Registering User 2 (Mark)...")
response = requests.post(f"{BASE_URL}/user", json={"name": "Mark", "age": 22})
print_response(response)
user2_id = response.json().get("id")

# Register User 3
print("Registering User 3 (Alex)...")
response = requests.post(f"{BASE_URL}/user", json={"name": "Alex", "age": 28})
print_response(response)
user3_id = response.json().get("id")

# List All Users
print("Listing all users...")
response = requests.get(f"{BASE_URL}/users")
print_response(response)

# Add Workouts for User 2
if user2_id:
    print(f"Adding a workout for User {user2_id}...")
    response = requests.put(f"{BASE_URL}/workouts/{user2_id}", json={
        "date": "2024-11-21",
        "time": "45 minutes",
        "distance": "5 miles"
    })
    print_response(response)

    print(f"Adding another workout for User {user2_id}...")
    response = requests.put(f"{BASE_URL}/workouts/{user2_id}", json={
        "date": "2024-11-22",
        "time": "30 minutes",
        "distance": "3 miles"
    })
    print_response(response)

# List Workouts for User 2
if user2_id:
    print(f"Listing workouts for User {user2_id}...")
    response = requests.get(f"{BASE_URL}/workouts/{user2_id}")
    print_response(response)

# FollowFriend API - User 1 follows User 2
if user1_id and user2_id:
    print(f"User {user1_id} is following User {user2_id}...")
    response = requests.put(f"{BASE_URL}/follow-list/{user1_id}", json={"follow_id": user2_id})
    print_response(response)

# FollowFriend API - User 3 follows User 2
if user3_id and user2_id:
    print(f"User {user3_id} is following User {user2_id}...")
    response = requests.put(f"{BASE_URL}/follow-list/{user3_id}", json={"follow_id": user2_id})
    print_response(response)

# ShowFriendWorkouts API - User 1 views workouts of User 2
if user1_id and user2_id:
    print(f"User {user1_id} viewing workouts of User {user2_id}...")
    response = requests.get(f"{BASE_URL}/follow-list/{user1_id}/{user2_id}")
    print_response(response)

# ShowFriendWorkouts API - User 3 views workouts of User 2
if user3_id and user2_id:
    print(f"User {user3_id} viewing workouts of User {user2_id}...")
    response = requests.get(f"{BASE_URL}/follow-list/{user3_id}/{user2_id}")
    print_response(response)

# Attempt ShowFriendWorkouts Without Following
if user1_id and user3_id:
    print(f"User {user1_id} attempting to view workouts of User {user3_id} without following...")
    response = requests.get(f"{BASE_URL}/follow-list/{user1_id}/{user3_id}")
    print_response(response)

# Attempt to Follow a Non-existent User
if user1_id:
    print("User 1 attempting to follow a non-existent user...")
    response = requests.put(f"{BASE_URL}/follow-list/{user1_id}", json={"follow_id": "nonexistent-id"})
    print_response(response)

# Attempt ShowFriendWorkouts for Non-existent User
if user1_id:
    print("User 1 attempting to view workouts of a non-existent user...")
    response = requests.get(f"{BASE_URL}/follow-list/{user1_id}/nonexistent-id")
    print_response(response)

# Remove User 3
if user3_id:
    print(f"Removing User {user3_id}...")
    response = requests.delete(f"{BASE_URL}/user/{user3_id}")
    print_response(response)

# Attempt to Get Removed User
if user3_id:
    print(f"Attempting to get removed User {user3_id}...")
    response = requests.get(f"{BASE_URL}/user/{user3_id}")
    print_response(response)