### Name
 Gyan Gali

### Email
ggali@stevens.edu

### Github 
https://github.com/Gyan268/StravaLite

### Project Title
Strava Lite

### Description
The Strava Lite project is a running tracker which allows users to register, track their workouts, and follow friends. The server is built using Flask and Flask-RESTful, providing REST APIs for all core functionalities.

### Project Structure
.
├── README.md
├── api.py
├── app.py
├── constants.py 
├── requirements.txt
├── routes.py
└── test.py

### APIs
## RegisterUser
**method** = `POST`
**route**: `/user`

**request**
```javascript
{
    "name": string,
    "age": int
}
```
**response**
```javascript
{
    "id": string,
    "name": string,
    "age": int,
    "workouts": [],
    "following": []
}
```
## GetUser
**method** = `GET`
**route**: `/user/<user_id>`

**request**
```javascript
{}
```
**response**
```javascript
{
    "id": string,
    "name": string,
    "age": int,
    "workouts": [],
    "following": []
}
```
## RemoveUser
**method** = `DELETE`
**route**: `/user/<user_id>`

**request**
```javascript
{}
```
**response**
```javascript
{}
```
## ListUsers
**method** = `GET`
**route**: `/users`

**request**
```javascript
{}
```
**response**
```javascript
{
    "users": [
        {
            "id": string,
            "name": string,
            "age": int,
            "workouts": [],
            "following": []
        }
    ]
}
```
## AddWorkout
**method** = `PUT`
**route**: `/workouts/<user_id>`

**request**
```javascript
{
    "date": string,
    "time": string,
    "distance": string
}
```
**response**
```javascript
{
    "date": string,
    "time": string,
    "distance": string
}
```
## ListWorkouts
**method** = `GET`
**route**: `/workouts/<user_id>`

**request**
```javascript
{}
```
**response**
```javascript
{
    "workouts": [
        {
            "date": string,
            "time": string,
            "distance": string
        }
    ]
}
```
## FollowFriend
**method** = `PUT`
**route**: `/follow-list/<user_id>`

**request**
```javascript
{
    "follow_id": string
}
```
**response**
```javascript
{
    "following": [
        string
    ]
}
```
## ShowFriendWorkouts
**method** = `GET`
**route**: `/follow-list/<user_id>/<follow_id>`

**request**
```javascript
{}
```
**response**
```javascript
{
    "workouts": [
        {
            "date": string,
            "time": string,
            "distance": string
        }
    ]
}
```
### Bug/Issues Faced
1. Early in development, requests without the application/json header caused unexpected errors. I added explicit checks to ensure all requests are JSON and return appropriate status codes when this validation fails.
2. Ensuring that users cannot follow non-existent accounts or duplicate follows was initially tricky. I implemented validation checks for both the current user and the user to follow, ensuring that the following list maintains unique entries.