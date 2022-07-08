from typing import Dict, Any
from ariadne import (
    GraphQLResolveInfo,
    convert_kwargs_to_snake_case)


from bigbangGraphQL.api.models import Email


@convert_kwargs_to_snake_case
def getEmail_resolver(obj: Any, info: GraphQLResolveInfo, id: str) -> Dict:
    try:
        email = Email.query.get(id).to_dict()
        payload = {
            "success": True,
            "post": email
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Email matching {id} not found"]
        }
    return payload


def listEmails_resolver(obj: Any, info: GraphQLResolveInfo) -> Dict:
    try:
        emails = [email.to_dict() for email in Email.query.all()]
        payload = {
            "success": True,
            "emails": emails
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
