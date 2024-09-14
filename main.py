from typing import List, Optional, Set
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from enums import Columns, GraphType


class GraphGenerator:
    def __init__(self, filepath: str, graph_type: GraphType) -> None:
        self.filepath = filepath
        self.df = pd.read_csv(self.filepath)
        self.columns = self.csv_to_dict()
        self.graph_type = graph_type

    def csv_to_dict(self):
        result = {col: np.array(self.df[col].values[1:]) for col in self.df.columns}
        return result

    def create_string_to_number_map(self, strings: List[str]):
        """
        Create a map from unique strings to unique numbers.

        Parameters:
        strings (list of str): List of strings to map.

        Returns:
        pd.DataFrame: DataFrame with unique strings and their corresponding numbers.
        """

        series = pd.Series(strings)
        unique_strings = series.unique()
        string_to_number = {string: idx for idx, string in enumerate(unique_strings)}

        return string_to_number

    def closest_square_number(self, n):
        # Calculate the integer square root of n
        root = math.ceil(math.sqrt(n))
        # Return the square of that integer
        return root * root

    def make_line(self, main_col, compare_cols):
        dimension = int(math.sqrt(self.closest_square_number(len(compare_cols))))
        _, axs = plt.subplots(dimension, dimension, figsize=(100, 100))
        for i in range(dimension):
            for j in range(dimension):
                col_index = i * dimension + j
                if col_index < len(compare_cols):
                    axs[i, j].plot(
                        self.columns[main_col.value],
                        self.columns[compare_cols[col_index].value],
                    )
                    # Set x and y labels for the scatter plot
                    axs[i, j].set_xlabel(main_col.value)
                    axs[i, j].set_ylabel(compare_cols[col_index].value)

    def make_histo(self, main_col, compare_cols):
        if compare_cols is not None:
            raise Exception("cannot make histogram for 2 features")

        column_data = self.columns[main_col.value]

        bins = set(column_data)
        list_bins = sorted([bin for bin in bins])  # Sort bins to keep the bars in order

        # Get counts for each bin
        counts = [list(column_data).count(bin) for bin in list_bins]

        # Create bar chart
        plt.bar(list_bins, counts, width=0.8, align="center")

        # Center labels and rotate them
        plt.xticks(list_bins, list_bins, rotation=45, ha="center")

        # Add labels to the axes
        plt.xlabel(main_col.value)
        plt.ylabel("Frequency")

        # Display the plot
        plt.show()

        def make_scatter(self, main_col, compare_cols):
            dimension = int(math.sqrt(self.closest_square_number(len(compare_cols))))
            fig, axs = plt.subplots(dimension, dimension, figsize=(15, 15))

            # Improve spacing between plots
            plt.subplots_adjust(hspace=0.4, wspace=0.4)

            for index, ax in enumerate(axs.flat):
                # Customize scatter plot: marker size, color, and transparency
                ax.scatter(
                    self.columns[main_col.value],
                    self.columns[compare_cols[index].value],
                    color="blue",
                    alpha=0.7,
                    edgecolors="k",
                    s=10,
                )
                # Set x and y labels
                ax.set_xlabel(main_col.value, fontsize=10)
                ax.set_ylabel(compare_cols[index].value, fontsize=10)
                ax.grid(True)  # Add grid for better visualization

                # Set a title for each subplot
                ax.set_title(
                    f"{main_col.value} vs {compare_cols[index].value}",
                    fontsize=12,
                )

            # Apply tight layout for better spacing between subplots
            fig.tight_layout()

    #
    # def make_scatter(self, main_col, compare_cols):
    #     dimension = int(math.sqrt(self.closest_square_number(len(compare_cols))))
    #     fig, axs = plt.subplots(dimension, dimension, figsize=(15, 15))
    #
    #     # Improve spacing between plots
    #     plt.subplots_adjust(hspace=0.4, wspace=0.4)
    #
    #     for i in range(dimension):
    #         for j in range(dimension):
    #             col_index = i * dimension + j
    #             if col_index < len(compare_cols):
    #                 # Customize scatter plot: marker size, color, and transparency
    #                 axs[i, j].scatter(
    #                     self.columns[main_col.value],
    #                     self.columns[compare_cols[col_index].value],
    #                     color="blue",
    #                     alpha=0.7,
    #                     edgecolors="k",
    #                     s=10,
    #                 )
    #                 # Set x and y labels
    #                 axs[i, j].set_xlabel(main_col.value, fontsize=10)
    #                 axs[i, j].set_ylabel(compare_cols[col_index].value, fontsize=10)
    #                 axs[i, j].grid(True)  # Add grid for better visualization
    #
    #                 # Set a title for each subplot
    #                 axs[i, j].set_title(
    #                     f"{main_col.value} vs {compare_cols[col_index].value}",
    #                     fontsize=12,
    #                 )
    #
    #     # Apply tight layout for better spacing between subplots
    #     fig.tight_layout()
    #

    def make_bar(self, main_col, compare_cols):
        # Determine the grid size for the subplots
        dimension = int(math.ceil(math.sqrt(len(compare_cols))))
        fig, axs = None, None

        if dimension < 3:
            fig, axs = plt.subplots(figsize=(15, 15))
            axs = [axs]
        else:

            # Create a figure and axes with the given grid size
            fig, axs = plt.subplots(dimension, dimension, figsize=(15, 15))

            # Flatten the array of axes for easier iteration
            axs = axs.flatten()

        for idx, col in enumerate(compare_cols):
            # Plot bar chart
            axs[idx].bar(
                self.columns[main_col.value],
                self.columns[col.value],
                color="skyblue",
                edgecolor="black",
            )

            # Set x and y labels
            axs[idx].set_xlabel(main_col.value, fontsize=12)
            axs[idx].set_ylabel(col.value, fontsize=12)

            # Set title
            axs[idx].set_title(f"{main_col.value} vs {col.value}", fontsize=14)

            # Improve layout
            axs[idx].grid(True, linestyle="--", alpha=0.7)
            axs[idx].tick_params(axis="both", which="both", labelsize=10)

        # Hide any unused subplots
        for idx in range(len(compare_cols), len(axs)):
            axs[idx].axis("off")

        # Adjust layout for better spacing
        plt.tight_layout()

    def make_graph(
        self, main_col: Columns, compare_cols: Optional[List[Columns]] = None
    ):
        if self.graph_type == GraphType.SCATTER:
            self.make_scatter(main_col, compare_cols)
        elif self.graph_type == GraphType.BAR:
            self.make_bar(main_col, compare_cols)
        elif self.graph_type == GraphType.LINE:
            self.make_line(main_col, compare_cols)
        elif self.graph_type == GraphType.HISTO:
            self.make_histo(main_col, compare_cols)
        plt.subplots_adjust(wspace=0.5, hspace=0.5)


graphGen = GraphGenerator("./AutomobilePrice_Lab2.csv", GraphType.HISTO)
# graphGen.make_graph(Columns.MAKE, [col for col in Columns])
# graphGen.make_graph(Columns.MAKE, [Columns.CITY_MPG, Columns.NUM_OF_CYLINDERS])
graphGen.make_graph(Columns.MAKE)
plt.show()
