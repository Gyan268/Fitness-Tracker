from flask_restful import Api
from api import RegisterUser, GetUser, RemoveUser, ListUsers, AddWorkout, ListWorkouts, FollowFriend, ShowFriendWorkouts
from constants import *

def init_routes(api: Api) -> None:
    """Dynamically register routes with Flask-RESTful API"""
    ROUTES = {
        REGISTER_USER: "/user",
        GET_USER: "/user/<int:user_id>",
        REMOVE_USER: "/user/<int:user_id>",
        LIST_USERS: "/users",
        ADD_WORKOUT: "/workouts/<int:user_id>",
        LIST_WORKOUTS: "/workouts/<int:user_id>",
        "FollowFriend": "/follow-list/<int:user_id>",
        "ShowFriendWorkouts": "/follow-list/<int:user_id>/<int:follow_id>"
    }

    METHODS = {
        REGISTER_USER: "POST",
        GET_USER: "GET",
        REMOVE_USER: "DELETE",
        LIST_USERS: "GET",
        ADD_WORKOUT: "PUT",
        LIST_WORKOUTS: "GET",
        "FollowFriend": "PUT",
        "ShowFriendWorkouts": "GET"
    }

    RESOURCES = {
        REGISTER_USER: RegisterUser,
        GET_USER: GetUser,
        REMOVE_USER: RemoveUser,
        LIST_USERS: ListUsers,
        ADD_WORKOUT: AddWorkout,
        LIST_WORKOUTS: ListWorkouts,
        "FollowFriend": FollowFriend,
        "ShowFriendWorkouts": ShowFriendWorkouts
    }

    for api_name, resource in RESOURCES.items():
        api.add_resource(resource, ROUTES[api_name], methods=[METHODS[api_name]])