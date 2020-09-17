#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String

import repository


class User(repository.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    fullname = Column(String(32))
    nickname = Column(String(32))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)

    def greet(self):
        return 'Hello, I am {}'.format(self.name)
