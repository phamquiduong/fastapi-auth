import sqlalchemy as sa
from sqlalchemy.orm import relationship

from database import Base


class Group(Base):
    __tablename__ = 'groups'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), unique=True, nullable=False)

    users = relationship('User', back_populates='group')
