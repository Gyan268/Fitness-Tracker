### Project 
Fitness Tracking Application

### Description
Developed a full-stack fitness tracking application that allows users to register, log workouts, and follow friends. The Flask backend (Python) handles user authentication, workout storage (PostgreSQL), and API endpoints, while the Angular frontend (TypeScript, HTML, CSS) dynamically fetches and displays user data. Integrated RESTful APIs, Flask-RESTful, SQLAlchemy ORM, and CORS for seamless backend operations. Implemented HTTP client requests in Angular to retrieve users and workouts efficiently. Deployed using Docker and Azure to ensure scalability and performance.

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
