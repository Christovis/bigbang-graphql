from datetime import date
from typing import Dict, Any
from ariadne import (
    GraphQLResolveInfo,
    convert_kwargs_to_snake_case)

from bigbangGraphQL.api import db
from bigbangGraphQL.api.models import Email


@convert_kwargs_to_snake_case
def create_email_resolver(
    obj: Any,
    info: GraphQLResolveInfo,
    messageID: str,
    archivedAt: str,
    senderAdress: str,
    fromAdress: str,
    replyTo: str,
    subject: str,
    inReplyTo: str,
    commentsTo: str,
    contentType: str,
    mimeVersion: str,
) -> Dict:
    try:
        today = date.today()
        email = Email(
            messageID=messageID,
            archivedAt=archivedAt,
            senderAdress=senderAdress,
            fromAdress=fromAdress,
            dateTime=today.strftime("%a, %d %b %Y %H:%M:%S %z"),
            replyTo=replyTo,
            subject=subject,
            inReplyTo=inReplyTo,
            commentsTo=commentsTo,
            contentType=contentType,
            mimeVersion=mimeVersion,
        )
        db.session.add(email)
        db.session.commit()
        payload = {
            "success": True,
            "post": email.to_dict(),
        }
    except ValueError:  # date format errors
        payload = {
            "success": False,
            "errors": [
                "Incorrect date format provided. Date should be in " +
                "the format: '%a, %d %b %Y %H:%M:%S %z'"
            ],
        }
    return payload


@convert_kwargs_to_snake_case
def delete_email_resolver(obj: Any, info: GraphQLResolveInfo, id: str) -> Dict:
    try:
        email = Email.query.get(id)
        db.session.delete(email)
        db.session.commit()
        payload = {"success": True, "post": email.to_dict()}
    except AttributeError:
        payload = {"success": False, "errors": ["Not found"]}
    return payload
