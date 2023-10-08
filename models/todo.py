from sqlmodel import BigInteger, Column, Field, SQLModel


class Todo(SQLModel, table=True):
    id: int = Field(
        sa_column=Column(BigInteger(), primary_key=True, autoincrement=False)
    )
    content: str = Field(default="!")
    done: bool = Field(default=False)
