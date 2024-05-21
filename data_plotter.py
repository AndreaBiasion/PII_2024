import matplotlib.dates as mdates
from matplotlib import pyplot as plt


class DataPlotter:
    def __init__(self, processor, detector):
        self.processor = processor
        self.detector = detector

    def plot_data(self):
        # Timeline of intervals
        timeline = [self.processor.start_date + i * self.processor.interval for i in range(int(self.processor.span))]

        # Create a figure and axis
        plt.figure(figsize=(14, 7))
        ax = plt.gca()

        # Plot the entire normalized vector with the specified color
        plt.plot(timeline, self.detector.vector, label='Detector', linestyle='-', marker='o', color='#FBAB7E', markersize=5)

        # Add gridlines
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)

        # Add labels and legend with improved styling
        plt.title('Detector Over Time', fontsize=15, fontweight='bold')
        plt.xlabel('Time', fontsize=14)
        plt.ylabel('Value', fontsize=14)
        plt.legend(fontsize=12)

        # Format the x-axis for better readability
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()

        # Highlight a specific point or event with annotation (optional)
        max_value_index = self.detector.vector.index(max(self.detector.vector))
        max_value_time = timeline[max_value_index]
        max_value = self.detector.vector[max_value_index]

        # Show plot
        plt.show()
