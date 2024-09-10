from typing import Annotated, Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base, str_256

intpk = Annotated[int, mapped_column(primary_key=True)]

class SectionValue(Base):
    
    __tablename__ = 'ng_sectionvalue'
    
    id: Mapped[intpk]
    ng_value: Mapped[str_256]
    ng_section: Mapped[int] = mapped_column(ForeignKey('ng_section.id'))
    ng_sectionproperty: Mapped[int] = mapped_column(ForeignKey('ng_sectionproperty.id'))

    # Relationships
    section: Mapped["Section"] = relationship("Section", back_populates="section_values")
    section_property: Mapped["SectionProperty"] = relationship("SectionProperty", back_populates="section_values")


class SectionProperty(Base):
    
    __tablename__ = 'ng_sectionproperty'
    
    id: Mapped[intpk]
    ng_idsectionvariable: Mapped[int] = mapped_column(ForeignKey('ng_sectionvariable.id'))
    pid: Mapped[int] = mapped_column(ForeignKey('ng_sectionseries.id')) 
    ng_formula0: Mapped[str]
    ng_source: Mapped[str_256]

    # Relationships
    section_variable: Mapped["SectionVariable"] = relationship("SectionVariable", back_populates="section_properties")
    section_series: Mapped["SectionSeries"] = relationship("SectionSeries", back_populates="section_properties")
    section_values: Mapped[List["SectionValue"]] = relationship("SectionValue", back_populates="section_property")


class SectionVariable(Base):
    
    __tablename__ = 'ng_sectionvariable'
    
    id: Mapped[intpk]
    ng_sectionvariable: Mapped[str_256]
    ng_description: Mapped[str_256]
    ng_symbol: Mapped[str_256]

    # Relationships
    section_properties: Mapped[List["SectionProperty"]] = relationship("SectionProperty", back_populates="section_variable")


class Section(Base):
    
    __tablename__ = 'ng_section'
    
    id: Mapped[intpk]
    ng_section: Mapped[str_256]
    pid: Mapped[int] = mapped_column(ForeignKey('ng_sectionseries.id'))
    ng_sequence: Mapped[int]
    ng_idsectionsize: Mapped[int] = mapped_column(ForeignKey('ng_sectionsizesectionsizegroup.id'))

    # Relationships
    section_series: Mapped["SectionSeries"] = relationship("SectionSeries", back_populates="sections")
    section_size: Mapped["SectionSizes"] = relationship("SectionSizes", back_populates="sections")
    section_values: Mapped[List["SectionValue"]] = relationship("SectionValue", back_populates="section")


class SectionSeries(Base):
    
    __tablename__ = 'ng_sectionseries'
    
    id: Mapped[intpk]
    ng_sectionseries: Mapped[str_256]
    ng_description: Mapped[str_256]
    ng_invalid: Mapped[str_256]
    ng_active: Mapped[str_256]
    ng_sectionshape: Mapped[int] = mapped_column(ForeignKey('ng_sectionspecies.id'))
    ng_sectionregion: Mapped[str_256]
    ng_namingrule: Mapped[str_256]
    ng_idmanufacturer: Mapped[int] = mapped_column(ForeignKey('ng_manufacturer.id'))
    ng_idsectionsizegroup0: Mapped[int] = mapped_column(ForeignKey('ng_sectionsizegroup.id'))
    ng_idstandard: Mapped[str_256]
    ng_idsectiontype: Mapped[int] = mapped_column(ForeignKey('ng_sectiontype.id'))

    # Relationships
    sections: Mapped[List["Section"]] = relationship("Section", back_populates="section_series")
    section_properties: Mapped[List["SectionProperty"]] = relationship("SectionProperty", back_populates="section_series")
    section_species: Mapped["SectionSpecies"] = relationship("SectionSpecies", back_populates="section_series")
    manufacturer: Mapped["Manufacturer"] = relationship("Manufacturer", back_populates="section_series")
    section_size_group: Mapped["SectionSizeGroup"] = relationship("SectionSizeGroup", back_populates="section_series")
    section_type: Mapped["SectionType"] = relationship("SectionType", back_populates="section_series")


class SectionSizeGroup(Base):
    
    __tablename__ = 'ng_sectionsizegroup'
    
    id: Mapped[intpk]
    ng_sectionsizegroup: Mapped[str_256]

    # Relationships
    section_series: Mapped[List["SectionSeries"]] = relationship("SectionSeries", back_populates="section_size_group")
    section_sizes: Mapped[List["SectionSizes"]] = relationship("SectionSizes", back_populates="section_size_group")


class SectionSizes(Base):
    
    __tablename__ = 'ng_sectionsizesectionsizegroup'
    
    id: Mapped[intpk]
    pid: Mapped[int] = mapped_column(ForeignKey('ng_sectionsizegroup.id'))
    ng_sectionsize: Mapped[str_256]
    ng_sequence: Mapped[int]

    # Relationships
    section_size_group: Mapped["SectionSizeGroup"] = relationship("SectionSizeGroup", back_populates="section_sizes")
    sections: Mapped[List["Section"]] = relationship("Section", back_populates="section_size")


class SectionSpecies(Base):
    
    __tablename__ = 'ng_sectionspecies'
    
    id: Mapped[intpk]
    ng_sectionshape: Mapped[str_256]  

    # Relationships
    section_series: Mapped[List["SectionSeries"]] = relationship("SectionSeries", back_populates="section_species")


class Manufacturer(Base):
    
    __tablename__ = 'ng_manufacturer'
    
    id: Mapped[intpk]
    ng_manufacturer: Mapped[str_256]
    ng_active: Mapped[str_256]
    ng_bitmapname: Mapped[str_256]
    ng_icon: Mapped[str_256]

    # Relationships
    section_series: Mapped[List["SectionSeries"]] = relationship("SectionSeries", back_populates="manufacturer")


class SectionType(Base):
    __tablename__ = 'ng_sectiontype'
    
    id: Mapped[intpk]
    ng_sectiontype: Mapped[str_256]
    ng_sequence: Mapped[str_256]
    ng_color: Mapped[str_256]
    ng_active: Mapped[str_256]

    # Relationships
    section_series: Mapped[List["SectionSeries"]] = relationship("SectionSeries", back_populates="section_type")