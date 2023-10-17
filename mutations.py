from ariadne import ObjectType, convert_kwargs_to_snake_case

from store import users, messages

mutation = ObjectType("Mutation")


@mutation.field("createUser")
@convert_kwargs_to_snake_case
async def resolve_create_user(obj, info, username):
    try:
        if not users.get(username):
            user = {
                "user_id": len(users) + 1,
                "username": username
            }
            users[username] = user
            return {
                "success": True,
                "user": user
            }
        return {
            "success": False,
            "errors": ["Username is taken"]
        }

    except Exception as error:
        return {
            "success": False,
            "errors": [str(error)]
        }