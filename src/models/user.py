import sqlalchemy as sa
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    email = sa.Column(sa.String(255), primary_key=True)
    password = sa.Column(sa.String(255))

    group_id = sa.Column(sa.Integer(), sa.ForeignKey('groups.id'), nullable=True)
    group = relationship('Group', back_populates='users')
