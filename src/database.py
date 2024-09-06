from typing import Annotated

from sqlalchemy import String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings

from sqlcipher3 import dbapi2 as sqlcipher


remote_engine = create_engine(
    url = settings.REMOTE_DATABASE_URL,
    echo = True,
    use_setinputsizes = False
)

local_engine = create_engine(
    url = settings.LOCAL_DATABASE_URL,
    module = sqlcipher,
    echo = True
)


remote_session = sessionmaker(remote_engine)

local_session = sessionmaker(local_engine)

str_256 = Annotated[str, 256]

class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }
    
    repr_cols_num = 3
    repr_cols = tuple()
    
    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"