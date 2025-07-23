from robot.api.deco import keyword

import pandas as pd
import matplotlib.pyplot as plt

class Keywords():

    def __init__(self):
        pass

    @keyword(tags=['Visualizer'])
    def visualize(
            self,
            csv_data: str,
            csv_header_x_axis: str,
            *csv_header_y_axis: str,
            graph_name: str
        ):
        df = pd.read_csv(csv_data)

        if csv_header_x_axis not in df.columns:
            raise ValueError(f"Column '{csv_header_x_axis}' not found in CSV!")
        
        for col in csv_header_y_axis:
            if col not in df.columns:
                raise ValueError(f"Column '{col}' not found in CSV!")

        df[csv_header_x_axis] = pd.to_datetime(df[csv_header_x_axis])

        plt.figure(figsize=(10, 6))

        for col in csv_header_y_axis:
            plt.plot(df[csv_header_x_axis], df[col], label=col)