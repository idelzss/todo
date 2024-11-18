from database.base import BASE
from sqlalchemy import Column, Integer, String, Text, Boolean



class ToDo(BASE):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(Text)
    completed = Column(Boolean, default=False)



    def __str__(self):
        return f"{self.title} - {self.description}"