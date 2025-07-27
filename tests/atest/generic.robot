*** Settings ***
Library    Visualizer


*** Test Cases ***
Add One Data Set
    [Documentation]    Add one graph to diagram.
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _strom    Strom    Blue
    Visualizer.Visualize    Strom / Spannung Verlauf

Add Two Data Sets
    [Documentation]    Add two graphs to diagram.
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _spannung    Spannung    Green
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _strom    Strom    Blue
    Visualizer.Visualize    Strom / Spannung Verlauf

Modify Graph Metadata
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _spannung    Spannung    Green
    Visualizer.Modify Graph Metadata    Spannung    x_axis=_time    y_axis=_spannung    color=Red
    Visualizer.Visualize    Strom / Spannung Verlauf

Delete from Diagram
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _spannung    Spannung    Green
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _strom    Strom    Blue
    Visualizer.Remove From Diagram     Strom
    Visualizer.Visualize    Strom / Spannung Verlauf

Reset Data Object
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _spannung    Spannung    Green
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _strom    Strom    Blue
    Visualizer.Reset
    BuiltIn.Run Keyword And Expect Error    REGEXP: ValueError.*
    ...    Visualizer.Visualize    Strom / Spannung Verlauf


    
