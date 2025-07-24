# robot-visualizer
Keywords from this repository can visualize CSV data as graph within the robotframework log file.

## Statistics

[![Release Pipeline](https://github.com/MarvKler/robotframework-visualizer/actions/workflows/release.yml/badge.svg)](https://github.com/MarvKler/robotframework-visualizer/actions/workflows/release.yml)  
[![PyPI - Version](https://img.shields.io/pypi/v/robotframework-visualizer.svg)](https://pypi.org/project/robotframework-visualizer)    
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/robotframework-visualizer.svg)](https://pypi.org/project/robotframework-visualizer)   
[![PyPI Downloads - Total](https://static.pepy.tech/badge/robotframework-visualizer)](https://pepy.tech/projects/robotframework-visualizer)    
[![PyPI Downloads - Monthly](https://static.pepy.tech/badge/robotframework-visualizer/month)](https://pepy.tech/projects/robotframework-visualizer)  

## GitHub Repository

Link to GitHub Project: [robotframework-visualizer](https://github.com/MarvKler/robotframework-visualizer)

## Use Case

If you have time-series data like energey measurements or temperature values over period of time, you can use this library to visualize thos raw data as visual diagram into your robot framework logfile.     
The generated diagram is saved as ``png`` file in your output directory and visualized as html image in your log file.

> [!IMPORTANT]
> X-Axis data should contain always the date-time value. The real value should be placed on Y-Axis.

## Installation

```shell
pip install robotframework-visualizer
```

## Usage

```python
*** Settings ***
Library    Visualizer


*** Test Cases ***
Visualize Data
    ${csv_file_path} =    Keyword.Write Data To Csv
    Visualizer.Add To Diagram     ${csv_file_path}    _time    _value    Value Axis    Blue
    Visualizer.Visualize
```
