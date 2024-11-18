import datetime as _dt
import sqlalchemy as _sa
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import database as _database


class User(_database.Base):
    __tablename__ = "users"
    id = _sa.Column(_sa.Integer, primary_key=True, index=True)
    email = _sa.Column(_sa.String, unique=True, index=True)
    hashed_password = _sa.Column(_sa.String)

    leads = _orm.relationship("Lead", back_populates="user")

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)


class Lead(_database.Base):
    __tablename__ = "leads"
    id = _sa.Column(_sa.Integer, primary_key=True, index=True)
    first_name = _sa.Column(_sa.String, index=True)
    last_name = _sa.Column(_sa.String, index=True)
    email = _sa.Column(_sa.String, index=True)
    company = _sa.Column(_sa.String, index=True, default="")
    note = _sa.Column(_sa.String, default="")
    created_at = _sa.Column(_sa.DateTime, default=_dt.datetime.now)
    updated_at = _sa.Column(_sa.DateTime, default=_dt.datetime.now)
    owner = _orm.relationship("User", back_populates="leads")
