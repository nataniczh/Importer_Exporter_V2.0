from typing import Annotated, Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base, str_256

intpk = Annotated[int, mapped_column(primary_key=True)]



class Completer(Base):
    
    __tablename__ = 'Completer'
    
    SelectSectionNameWithoutAccents: Mapped[str_256]
    SectionNameWithoutAccents: Mapped[str_256]
    SectionName: Mapped[str_256]
    LookupNameWithoutAccents: Mapped[str_256]
    SectionSeriesId: Mapped[int] = mapped_column(ForeignKey('SectionSeries.id'))
    SectionId: Mapped[int] = mapped_column(ForeignKey('Section.id'))
    isInvalid: Mapped[int]
    seriesOrder: Mapped[int]
    itemOrder: Mapped[int]
    lang_de: Mapped[int]
    lang_en: Mapped[int]
    lang_cs: Mapped[int]
    lang_zh: Mapped[int]
    lang_fr: Mapped[int]
    lang_it: Mapped[int]
    lang_pl: Mapped[int]
    lang_pt: Mapped[int]
    lang_ru: Mapped[int]
    lang_es: Mapped[int]
    lang_nl: Mapped[int]
    lang_el: Mapped[int]
    
    # Relationships
    section_series: Mapped["SectionSeries"] = relationship(back_populates="completers")
    section: Mapped["Section"] = relationship(back_populates="completers")


class Manufacturer(Base):
    
    __tablename__ = 'Manufacturer'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    website: Mapped[str_256]
    iconId: Mapped[int]
    order: Mapped[int]
    
    # Relationships
    section_series: Mapped[List["SectionSeries"]] = relationship(back_populates="manufacturer")


class ManufacturingType(Base):
    
    __tablename__ = 'ManufacturingType'
    
    version: Mapped[int]
    id: Mapped[intpk]
    manufacturingMethodName: Mapped[str_256]
    iconId: Mapped[int]
    order: Mapped[int]
    
    # Relationships
    section_shapes: Mapped[List["SectionShape"]] = relationship(back_populates="manufacturing_type")
    

class ParameterCondition(Base):
    
    __tablename__ = 'ParameterCondition'
    
    id: Mapped[intpk]
    version: Mapped[int]
    order: Mapped[int]
    valueA: Mapped[str_256]
    valueB: Mapped[str_256]
    openBracket: Mapped[int]
    closeBracket: Mapped[int]
    operatorType: Mapped[int]
    combinationType: Mapped[int]


class Region(Base):
    
    __tablename__ = 'Region'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    iconId: Mapped[int]
    
    # Relationships
    standards: Mapped[List["Standard"]] = relationship(back_populates="region")


class Rf5Conversion(Base):
    
    __tablename__ = 'Rf5Conversion'
    
    Rf5Name: Mapped[str_256]
    SectionId: Mapped[int]


class Rf5ParametricConversion(Base):
    
    __tablename__ = 'Rf5ParametricConversion'
    
    Rf5Serie: Mapped[str_256]
    Rf6Serie: Mapped[int]
    GroupId: Mapped[int]
    ListOfParameters: Mapped[str_256]
    MirrorAboutYY: Mapped[int]
    MirrorAboutZZ: Mapped[int]
    InternalSeparator: Mapped[str_256]


class Section(Base):
    
    __tablename__ = 'Section'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    outlineDefinition: Mapped[str_256]
    order: Mapped[int]
    sectionSeries_id: Mapped[int] = mapped_column(ForeignKey('SectionSeries.id'))
    stressPointDefinitions: Mapped[str_256]
    sectionSizeValueId: Mapped[int]
    
    # Relationships
    section_series: Mapped["SectionSeries"] = relationship(back_populates="sections")
    completers: Mapped[List["Completer"]] = relationship(back_populates="section")


class Section_nonnumericParameterValues_keys(Base):
    
    __tablename__ = 'Section_nonnumericParameterValues_keys'
    
    id: Mapped[int]
    container_order: Mapped[int]
    value: Mapped[str_256]


class Section_nonnumericParameterValues_values(Base):
    
    __tablename__ = 'Section_nonnumericParameterValues_values'
    
    id: Mapped[int]
    container_order: Mapped[int]
    value: Mapped[str_256]


class Section_notes(Base):
    
    __tablename__ = 'Section_notes'
    
    id: Mapped[int]
    container_order: Mapped[int]
    value_id: Mapped[int] = mapped_column(ForeignKey('SectionNote.id'))
    
    # Relationships
    note: Mapped["SectionNote"] = relationship("SectionNote", back_populates="sections")


class Section_predefinedParameterValues_keys(Base):
    
    __tablename__ = 'Section_predefinedParameterValues_keys'
    
    id: Mapped[int]
    container_order: Mapped[int]
    value: Mapped[str_256]


class Section_predefinedParameterValues_values(Base):
    
    __tablename__ = 'Section_predefinedParameterValues_values'
    
    id: Mapped[int]
    container_order: Mapped[int]
    value: Mapped[float]


class SectionFamily(Base):
    
    __tablename__ = 'SectionFamily'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    order: Mapped[int]
    
    # Relationships
    section_series: Mapped[List["SectionSeries"]] = relationship("SectionSeries", back_populates="family")


class SectionGroup(Base):
    
    __tablename__ = 'SectionGroup'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    description: Mapped[str_256]
    iconId: Mapped[int]
    order: Mapped[int]
    
    # Relationships
    section_series: Mapped[List["SectionSeries"]] = relationship("SectionSeries", back_populates="group")


class SectionNote(Base):
    
    __tablename__ = 'SectionNote'
    
    version: Mapped[int]
    id: Mapped[intpk]
    text: Mapped[str_256]
    order: Mapped[int]
    
    # Relationships
    sections: Mapped[List["Section_notes"]] = relationship("Section_notes", back_populates="note")


class SectionParameter(Base):
    
    __tablename__ = 'SectionParameter'
    
    version: Mapped[int]
    id: Mapped[intpk]
    parameterId: Mapped[str_256]
    branch_id: Mapped[int] = mapped_column(ForeignKey('SectionParameterBranch.id'))
    description: Mapped[str_256]
    symbol: Mapped[str_256]
    imperialSymbol: Mapped[str_256]
    order: Mapped[int]
    unitId: Mapped[str_256]
    unitGroupId: Mapped[str_256]
    group: Mapped[int]
    signDeterminingAxes: Mapped[int]
    minOrMaxAxesDirectionTwin: Mapped[str_256]
    
    # Relationships
    branch: Mapped["SectionParameterBranch"] = relationship("SectionParameterBranch", back_populates="parameters")


class SectionParameterBranch(Base):
    
    __tablename__ = 'SectionParameterBranch'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    order: Mapped[int]
    
    # Relationships
    parameters: Mapped[List["SectionParameter"]] = relationship("SectionParameter", back_populates="branch")


class SectionParameterDefinition(Base):
    
    __tablename__ = 'SectionParameterDefinition'
    
    id: Mapped[intpk]
    version: Mapped[int]
    formula: Mapped[str_256]
    displayCondition: Mapped[int]
    definitionSource: Mapped[int]
    parameter_id: Mapped[int] = mapped_column(ForeignKey('SectionParameter.id'))
    defaultValue: Mapped[float]
    imperialDefaultValue: Mapped[float]
    bitmapValue: Mapped[float]
    minimalValue: Mapped[float]
    maximalValue: Mapped[float]
    ediclass: Mapped[bool]
    ediclassCondition: Mapped[str_256]
    showDefaultValueInName: Mapped[bool]
    inclusiveMinimalValue: Mapped[bool]
    inclusiveMaximalValue : Mapped[bool]
    controlParameterId: Mapped[str_256]
    updateFormula: Mapped[str_256]
    differentDescription: Mapped[str_256]
    differentSymbol: Mapped[str_256]
    differentUnitKey: Mapped[str_256]
    
    # Relationships
    parameter: Mapped["SectionParameter"] = relationship("SectionParameter", back_populates="parameter_definitions")


class SectionParameterValue(Base):
    
    __tablename__ = 'SectionParameterValue'
    
    id: Mapped[intpk]
    version: Mapped[int]
    inputUnit: Mapped[str_256]
    valueInputUnit: Mapped[float]
    valueSI: Mapped[float]
    displayCondition: Mapped[int]
    nonnumericValue: Mapped[str_256]
    
    # Relationships
    parameter: Mapped["SectionParameter"] = relationship("SectionParameter")


class SectionSeries(Base):
    
    __tablename__ = 'SectionSeries'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    family_id: Mapped[int]  = mapped_column(ForeignKey('SectionFamily.id'))
    shape_id: Mapped[int] = mapped_column(ForeignKey('SectionShape.id'))
    group_id: Mapped[int] = mapped_column(ForeignKey('SectionGroup.id'))
    type_id : Mapped[int] = mapped_column(ForeignKey('SectionType.id'))
    manufacturer_id : Mapped[int] = mapped_column(ForeignKey('Manufacturer.id'))
    sectionNameRule : Mapped[str_256]
    stressPointDefinitions  : Mapped[str_256]
    subpanelDefinitions : Mapped[str_256]
    dimensionDefinitions: Mapped[str_256]
    bitmapDimensionDefinitions  : Mapped[str_256]
    outlineDefinition: Mapped[str_256]
    stressPointConnectionDefinitions: Mapped[str_256]
    weldsDefinitions: Mapped[str_256]
    note1: Mapped[str_256]
    description : Mapped[str_256]
    isInvalid: Mapped[bool]
    hasImperialParameters: Mapped[bool]
    sectionSizeGroup_id : Mapped[int] = mapped_column(ForeignKey('SizeGroup.id'))
    order : Mapped[int]
    rsectionPoints  : Mapped[str_256]
    rsectionElements: Mapped[str_256]
    rsectionElementSets : Mapped[str_256]
    outlinesCompliancesDefinitions: Mapped[str_256]
    
    # Relationships
    family: Mapped["SectionFamily"] = relationship("SectionFamily", back_populates="section_series")
    shape: Mapped["SectionShape"] = relationship("SectionShape", back_populates="section_series")
    group: Mapped["SectionGroup"] = relationship("SectionGroup", back_populates="section_series")
    type: Mapped["SectionType"] = relationship("SectionType", back_populates="section_series")
    manufacturer: Mapped["Manufacturer"] = relationship("Manufacturer", back_populates="section_series")
    sections: Mapped[List["Section"]] = relationship("Section", back_populates="section_series")
    completers: Mapped[List["Completer"]] = relationship("Completer", back_populates="section_series")


class SectionSeries_builtUpRectangularLayoutInput(Base):
    
    __tablename__ = 'SectionSeries_builtUpRectangularLayoutInput'
    
    id: Mapped[int]
    container_order: Mapped[int]
    sectionId: Mapped[int]
    layoutActiveInY: Mapped[bool]
    patternsCountInY: Mapped[str_256]
    patternsDistanceInY: Mapped[str_256]
    layoutActiveInZ: Mapped[bool]
    patternsCountInZ: Mapped[str_256]
    patternsDistanceInZ: Mapped[str_256]


class SectionSeries_builtUpSectionSelections(Base):
    
    __tablename__ = 'SectionSeries_builtUpSectionSelections'
    
    id: Mapped[int]
    container_order: Mapped[int]
    sectionIdentifier: Mapped[str_256]
    sectionGroup: Mapped[int]
    identicalAs: Mapped[str_256]
    sectionShapes: Mapped[str_256]
    defaultSectionId: Mapped[int]
    imperialDefaultSectionId: Mapped[int]
    description: Mapped[str_256]
    rotate : Mapped[str_256]
    mirrorY: Mapped[bool]
    mirrorZ : Mapped[bool]
    move: Mapped[str_256]


class SectionSeries_compatibleSectionShapes(Base):
    
    __tablename__ = 'SectionSeries_compatibleSectionShapes'
    
    id: Mapped[int]
    container_order: Mapped[int]
    value: Mapped[int]


class SectionSeries_conditions(Base):
    
    __tablename__ = 'SectionSeries_conditions'
    
    id: Mapped[int]
    container_order: Mapped[int]
    order : Mapped[int]
    valueA: Mapped[str_256]
    valueB: Mapped[str_256]
    openBracket : Mapped[int]
    closeBracket : Mapped[int]
    operatorType: Mapped[int]
    combinationType: Mapped[int]


class SectionSeries_parameterDefinitions(Base):
    
    __tablename__ = 'SectionSeries_parameterDefinitions'
    
    id: Mapped[int]
    container_order: Mapped[int]
    formula: Mapped[str_256]
    displayCondition: Mapped[int]
    definitionSource: Mapped[int]
    parameter_id: Mapped[int]  = mapped_column(ForeignKey('SectionParameter.id'))
    defaultValue: Mapped[float]
    imperialDefaultValue  : Mapped[float]
    bitmapValue: Mapped[float]
    minimalValue: Mapped[float]
    maximalValue: Mapped[float]
    ediclass: Mapped[bool]
    ediclassCondition: Mapped[str_256]
    showDefaultValueInName: Mapped[bool]
    inclusiveMinimalValue : Mapped[bool]
    inclusiveMaximalValue : Mapped[bool]
    controlParameterId    : Mapped[str_256]
    updateFormula: Mapped[str_256]
    differentDescription  : Mapped[str_256]
    differentSymbol: Mapped[str_256]
    differentUnitKey : Mapped[str_256]


class SectionSeries_regions(Base):
    
    __tablename__ = 'SectionSeries_regions'
    
    id: Mapped[int]
    container_order: Mapped[int]
    value_id: Mapped[int]  = mapped_column(ForeignKey('Region.id'))
    
    
    region: Mapped["Region"] = relationship("Region")



class SectionSeries_sectionSources(Base):
    
    __tablename__ = 'SectionSeries_sectionSources'
    
    id: Mapped[int]
    container_order: Mapped[int]
    reference_id: Mapped[int]
    reference_class: Mapped[str_256]


class SectionSeries_standards(Base):
    
    __tablename__ = 'SectionSeries_standards'
    
    id: Mapped[int]
    container_order: Mapped[int]
    value_standardId: Mapped[int]  = mapped_column(ForeignKey('Standard.standardId'))
    
    
    standard: Mapped["Standard"] = relationship("Standard")


class SectionShape(Base):
    
    __tablename__ = 'SectionShape'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    manufacturingType_id: Mapped[int]  = mapped_column(ForeignKey('ManufacturingType.id'))
    sectionCategory: Mapped[int] 
    thinWalledModelling : Mapped[bool]
    transverseStiffener : Mapped[bool]
    effectiveLengths: Mapped[bool]
    interactingSections : Mapped[bool]
    isClosed: Mapped[bool]
    iconId: Mapped[int]
    order: Mapped[int]
    
    
    manufacturing_type: Mapped["ManufacturingType"] = relationship("ManufacturingType", back_populates="section_shapes")
    section_series: Mapped[List["SectionSeries"]] = relationship("SectionSeries", back_populates="shape")


class SectionShape_requiredParameters(Base):
    
    __tablename__ = 'SectionShape_requiredParameters'
    
    id: Mapped[int]
    container_order: Mapped[int]
    value: Mapped[str_256]


class SectionStandardGroup(Base):
    
    __tablename__ = 'SectionStandardGroup'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    isSubpanelDefinition: Mapped[bool]
    standardGroup_id: Mapped[int]  = mapped_column(ForeignKey('StandardsStandardGroup.id'))
    typeOfThicknessReduction: Mapped[int]
    displayConditionValue: Mapped[int]


class SectionType(Base):
    
    __tablename__ = 'SectionType'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    sectionFamily_id: Mapped[int]  = mapped_column(ForeignKey('SectionFamily.id'))
    order: Mapped[int]
    
    
    family: Mapped["SectionFamily"] = relationship("SectionFamily")
    section_series: Mapped[List["SectionSeries"]] = relationship("SectionSeries", back_populates="type")


class SizeGroup(Base):
    
    __tablename__ = 'SizeGroup'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    
    
    section_series: Mapped[List["SectionSeries"]] = relationship("SectionSeries", back_populates="size_group")



class SizeValue(Base):
    
    __tablename__ = 'SizeValue'
    
    version: Mapped[int]
    id: Mapped[intpk]
    sizeGroupId: Mapped[int]
    name: Mapped[str_256]
    order: Mapped[int]


class Source(Base):
    
    __tablename__ = 'Source'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name : Mapped[str_256]
    url1: Mapped[str_256]
    url2: Mapped[str_256]
    note: Mapped[str_256]
    languageIconId: Mapped[int]


class Standard(Base):
    
    __tablename__ = 'Standard'
    
    version: Mapped[int]
    standardId: Mapped[intpk]
    name: Mapped[str_256]
    comment: Mapped[str_256]
    region_id: Mapped[int] = mapped_column(ForeignKey('Region.id'))
    order: Mapped[int]
    
    
    region: Mapped["Region"] = relationship("Region", back_populates="standards")



class StandardsStandardGroup(Base):
    
    __tablename__ = 'StandardsStandardGroup'
    
    version: Mapped[int]
    id: Mapped[intpk]
    name: Mapped[str_256]
    application: Mapped[str_256]


class StressPointDefinition(Base):
    
    __tablename__ = 'StressPointDefinition'
    
    id: Mapped[intpk] 
    version: Mapped[int]
    stressPointId: Mapped[str_256]
    elementOrPartId: Mapped[str_256]
    definitionType: Mapped[int]
    distance: Mapped[str_256]
    position: Mapped[int]
    lineNumber: Mapped[str_256]
    coordinateY: Mapped[str_256]
    coordinateZ: Mapped[str_256]
    isHidable: Mapped[bool]


class WebSectionsUrl(Base):
    
    __tablename__ = 'WebSectionsUrl'
    
    SectionUrlName: Mapped[str_256]
    SectionId: Mapped[int]


class WebSeriesUrl(Base):
    
    __tablename__ = 'WebSeriesUrl'
    
    SerieUrlName: Mapped[str_256]
    SectionSeriesId: Mapped[int]
