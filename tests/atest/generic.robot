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
    
