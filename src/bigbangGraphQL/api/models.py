from typing import Dict

from bigbangGraphQL.api import db


class Email(db.Model):
    messageID = db.Column(db.String(200), primary_key=True)
    archivedAt = db.Column(db.String(300))
    senderAdress = db.Column(db.String(150))
    fromAdress = db.Column(db.String(150))
    dateTime = db.Column(db.String(150))
    replyTo = db.Column(db.String(300))
    subject = db.Column(db.String(300))
    inReplyTo = db.Column(db.String(300))
    commentsTo = db.Column(db.String(300))
    contentType = db.Column(db.String(200))
    mimeVersion = db.Column(db.String(10))

    def to_dict(self) -> Dict[str, str]:
        return {
            "messageID": self.messageID,
            "archivedAt": self.archivedAt,
            "senderAdress": self.senderAdress,
            "fromAdress": self.fromAdress,
            "dateTime": self.dateTime,
            "replyTo": self.replyTo,
            "subject": self.subject,
            "inReplyTo": self.inReplyTo,
            "commentsTo": self.commentsTo,
            "contentType": self.contentType,
            "mimeVersion": self.mimeVersion,
        }
