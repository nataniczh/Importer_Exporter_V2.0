from sqlalchemy import Integer, and_, not_, cast, func, insert, inspect, or_, select, text, String
from sqlalchemy.orm import aliased, contains_eager, joinedload, selectinload
import pandas as pd

from database import Base, remote_engine, local_engine, remote_session, local_session

from local_models import SectionSeries





def test():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    with local_session() as session: 
        query = (
            select(SectionSeries.id,
                   SectionSeries.name,
                   SectionSeries.description
                   ).filter(SectionSeries.id == 2255)   
        )
    res = session.execute(query)
    df = pd.DataFrame(res.fetchall())
    print(df)
        

        
test()