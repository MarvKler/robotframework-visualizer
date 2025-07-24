*** Settings ***
Library    Visualizer


*** Test Cases ***
Add One Data Set
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _strom    Strom    Blue
    Visualizer.Visualize    Strom / Spannung Verlauf

Add Two Data Sets
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _spannung    Spannung    Green
    Visualizer.Add To Diagramm    ${CURDIR}${/}testdata${/}dummy_strom_spannung.csv    _time    _strom    Strom    Blue
    Visualizer.Visualize    Strom / Spannung Verlauf
    
