# Import libraries 
import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Add page options for the overall app
ui.page_opts(title="DG's PyShiny App with Plots",fillable=True)

# Create a sidebar with a slider input for bins
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 50, 15)

# Define function for rendering histogram plot
@render.plot(alt="A histogram showing random data distribution")
def draw_histogram():
    # Additional labeling for plot
    plt.title("Histogram Data")
    plt.xlabel("X Value")
    plt.ylabel("Y Density")
    # Pass in numpy data array
    count_of_points: int = 500
    np.random.seed(345)
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
    #Plot visual customizations
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color="purple")

# Define function for rendering line plot
@render.plot(alt="Scatter plot showing random data distribution")
def draw_scatter_plot():
    # Generate random data for the scatter plot (will use same seed)
    x_values = np.random.rand(100) * 10
    y_values = np.random.randn(100) 
    # Plot the data and customize plot
    plt.scatter(x_values, y_values, color="black", alpha=0.5)
    plt.title("Scatter Plot")
    plt.xlabel("X Value")
    plt.ylabel("Y Value")

# Define function for rendering heatmap
@render.plot(alt="Heatmap showing random data distribution")
def draw_heatmap():
    # Generate random data for the heatmap (will use same seed)
    x_values = np.random.rand(100) * 10
    y_values = np.random.rand(100) * 10  
    # Create and plot heatmap and customize
    plt.hist2d(x_values, y_values, bins=20, cmap='coolwarm')
    plt.colorbar(label='Density of Data')
    plt.title("Heatmap for Data Density")
    plt.xlabel("X Value")
    plt.ylabel("Y Value")
    
