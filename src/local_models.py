from typing import Annotated, Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, str_256

intpk = Annotated[int, mapped_column(primary_key=True)]


class SectionSeries(Base):
    
    __tablename__ = 'SectionSeries'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    family_id: Mapped[int]
    shape_id: Mapped[int]
    group_id: Mapped[int]
    type_id: Mapped[int]
    manufacturer_id: Mapped[int]
    sectionNameRule: Mapped[str_256]
    stressPointDefinitions: Mapped[str_256]
    subpanelDefinitions: Mapped[str_256]
    dimensionDefinitions: Mapped[str_256]
    bitmapDimensionDefinitions: Mapped[str_256]
    outlineDefinition: Mapped[str_256]
    stressPointConnectionDefinitions: Mapped[str_256]
    weldsDefinitions: Mapped[str_256]
    note1: Mapped[str_256]
    description: Mapped[str_256]
