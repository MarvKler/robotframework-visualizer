from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger

import os
import pandas as pd
from pandas import DataFrame
from pathlib import Path
from io import StringIO
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import matplotlib.dates as mdates
import random

from ..utils.enums import GraphColor

class Keywords():
    
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        self.graph_data = []
        self.add_graph = False
        self.path = {}
        self.unique_directory = "visualizer"
        self.diagram_name = None

    ####################################################################################################################
    # Robot Framework Listener Functions:
    ####################################################################################################################

    def start_test(self, data, result):
        logger.trace("Resetted state machine")
        self.add_graph = False
        self.path = {}

    def end_test(self, data, result):
        if self.add_graph:
            for img_path in self.path:
                logger.debug(f"Added graph to test documentation for: {img_path} / {self.path[img_path]}")
                result.doc += f"\n\n*{img_path}:* \n\n ["+ self.path[img_path] + f"| {img_path} ]"
        self._cleanup()

    ####################################################################################################################
    # Internal Helper Functions:
    ####################################################################################################################

    def _get_csv_as_pandas(self, csv_data: str, usecols = None) -> DataFrame:
        if isinstance(csv_data, str) and os.path.isfile(csv_data):
            # csv_data is a file path
            return pd.read_csv(csv_data, usecols=usecols)
        elif isinstance(csv_data, str):
            # csv_data is a CSV string
            csv_buffer = StringIO(csv_data)
            return pd.read_csv(csv_buffer, usecols=usecols)
        else:
            raise ValueError("csv_data must be either a CSV string or a valid file path as string.")
        
    def _validate_columns(self, csv_data: DataFrame, x_axis: str, *y_axis: str):
        if x_axis not in csv_data.columns:
            raise ValueError(f"Column '{x_axis}' not found in CSV!")
        
        for col in y_axis:
            if col not in csv_data.columns:
                raise ValueError(f"Column '{col}' not found in CSV!")
            
    def _cleanup(self):
        self.graph_data.clear()
        self.diagram_name = None
        self.add_graph = False
        self.path = {}
        
    ####################################################################################################################
    # Public Keywords for Robot Framework:
    ####################################################################################################################

    @keyword()
    def add_to_diagramm(
            self,
            csv_data: str,
            csv_header_x_axis: str,
            csv_header_y_axis: str,
            graph_name: str,
            line_color: GraphColor = GraphColor.Blue
        ):
        """
        TBD
        """
        
        # Einlesen der CSV mit nur den benötigten Spalten
        df = self._get_csv_as_pandas(csv_data, usecols=[csv_header_x_axis, csv_header_y_axis])
        self._validate_columns(df, csv_header_x_axis, csv_header_y_axis)

        # X-Achse als Zeit formatieren
        df[csv_header_x_axis] = pd.to_datetime(df[csv_header_x_axis], format="mixed")
        df = df.sort_values(by=csv_header_x_axis)

        # Zwischenspeichern
        self.graph_data.append({
            "df": df,
            "x_axis": csv_header_x_axis,
            "y_axis": csv_header_y_axis,
            "graph_name": graph_name,
            "color": line_color.value
        })

    @keyword(tags=['Visualizer'])
    def visualize(
            self,
            diagram_name: str
        ):
        """
        TBD
        """
        if not self.graph_data:
            raise ValueError("No graph data available. Call 'Add To Diagramm' first.")
        
        self.diagram_name = diagram_name

        # Set state machine for RF listener
        self.add_graph = True

        # Get output directory + create individual sub directory
        img_dir = Path(BuiltIn().get_variable_value('$OUTPUT_DIR')) / self.unique_directory
        img_dir.mkdir(parents=True, exist_ok=True)

        # Generate random file name + define path variables
        file_name = f"graph{''.join(random.choices('123456789', k=10))}.png"
        full_file_path = str(img_dir / file_name)
        self.path[diagram_name] = f"{self.unique_directory}/{file_name}"

        # Create diagram
        fig, ax = plt.subplots(figsize=(10, 3))

        # Plot given data fron entry list
        for entry in self.graph_data:
            df = entry["df"]
            x = entry["x_axis"]
            y = entry["y_axis"]
            color = entry["color"]
            df.plot(x=x, y=y, ax=ax, label=entry['graph_name'], color=color)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y %H:%M'))
        fig.autofmt_xdate()
        plt.xlabel(self.graph_data[0]["x_axis"])
        plt.ylabel("Value(s)")
        plt.legend()
        plt.tight_layout(rect=[0, 0, 1, 0.95])

        # Save plot to PNG file
        plt.savefig(full_file_path, format='png')
