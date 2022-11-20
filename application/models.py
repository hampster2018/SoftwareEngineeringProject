"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from pydantic.dataclasses import dataclass
from uuid import uuid4
from typing import Optional

from . import db

@dataclass
class User(UserMixin):

    _id: int
    name: str = "Default Name"
    email: str = "example@example.com"
    password: str = "..."

    def get_id(self):
        object_id = self._id
        return object_id

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method="sha256")
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
    def __repr__(self):
        return "<User {}>".format(self.name)