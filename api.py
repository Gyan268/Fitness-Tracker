from flask_restful import Resource, reqparse
from models import db, User, Workout  # Ensure models are properly imported



# Request Parsers
register_user_parser = reqparse.RequestParser()
register_user_parser.add_argument("name", type=str, required=True)
register_user_parser.add_argument("age", type=int, required=False)

add_workout_parser = reqparse.RequestParser()
add_workout_parser.add_argument("date", type=str, required=True)
add_workout_parser.add_argument("time", type=str, required=True)
add_workout_parser.add_argument("distance", type=str, required=True)

follow_friend_parser = reqparse.RequestParser()
follow_friend_parser.add_argument("follow_id", type=int, required=True)  # Use int for user IDs

# ✅ Register a User (POST /user)
class RegisterUser(Resource):
    def post(self):
        args = register_user_parser.parse_args()
        new_user = User(name=args["name"], age=args.get("age"))
        db.session.add(new_user)
        db.session.commit()

        return {
            "id": new_user.id,
            "name": new_user.name,
            "age": new_user.age,
            "workouts": [],
            "following": []
        }, 201

# ✅ Get User by ID (GET /user/<user_id>)
class GetUser(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        return {
            "id": user.id,
            "name": user.name,
            "age": user.age,
            "workouts": [
                {"date": w.date, "time": w.time, "distance": w.distance} for w in user.workouts
            ],
            "following": []
        }, 200

# ✅ Delete User (DELETE /user/<user_id>)
class RemoveUser(Resource):
    def delete(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted successfully"}, 200

# ✅ List All Users (GET /users)
class ListUsers(Resource):
    def get(self):
        users = User.query.all()
        return {
            "users": [
                {"id": u.id, "name": u.name, "age": u.age} for u in users
            ]
        }, 200

# ✅ Add Workout (PUT /workouts/<user_id>)
class AddWorkout(Resource):
    def put(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        args = add_workout_parser.parse_args()
        new_workout = Workout(user_id=user.id, date=args["date"], time=args["time"], distance=args["distance"])
        db.session.add(new_workout)
        db.session.commit()

        return {
            "date": new_workout.date,
            "time": new_workout.time,
            "distance": new_workout.distance
        }, 201

# ✅ List Workouts for a User (GET /workouts/<user_id>)
class ListWorkouts(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}, 404

        workouts = Workout.query.filter_by(user_id=user.id).all()
        return {
            "workouts": [
                {"date": w.date, "time": w.time, "distance": w.distance} for w in workouts
            ]
        }, 200
        
class FollowFriend(Resource):
    def put(self, user_id):
        args = follow_friend_parser.parse_args()
        follow_id = args["follow_id"]

        user = User.query.get(user_id)
        friend = User.query.get(follow_id)

        if not user or not friend:
            return {"error": "User or friend not found"}, 404

        # Check if already following
        if user.following.filter_by(id=follow_id).first():
            return {"message": "Already following this user"}, 400

        user.following.append(friend)  # Append friend's ID
        db.session.commit()

        return {"following": [u.id for u in user.following]}, 201


class ShowFriendWorkouts(Resource):
    def get(self, user_id, follow_id):
        user = User.query.get(user_id)
        friend = User.query.get(follow_id)

        if not user or not friend:
            return {"error": "User or friend not found"}, 404

        workouts = Workout.query.filter_by(user_id=friend.id).all()
        return {
            "workouts": [
                {"date": w.date, "time": w.time, "distance": w.distance} for w in workouts
            ]
        }, 200