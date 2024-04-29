from matplotlib import pyplot as plt


class DataPlotter:
    def __init__(self, processor, detector):
        self.processor = processor
        self.detector = detector

    def plot_data(self):
        # Timeline of intervals
        timeline = [self.processor.start_date + i * self.processor.interval for i in range(int(self.processor.span))]

        # Plot the entire normalized vector
        plt.figure(figsize=(12, 6))
        plt.plot(timeline, self.processor.normalized_vector, label='DataProcessor')
        #plt.plot(timeline, self.detector.vector, label='Detector')

        # Add labels and legend
        plt.title('Data Processor and Detector Results Over Time')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Show plot
        plt.show()
