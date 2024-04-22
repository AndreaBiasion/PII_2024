import matplotlib.pyplot as plt
class DataPlotter:
    def __init__(self, processor):
        self.processor = processor

    def plot_data(self):
        timeline = [self.processor.start_date + i * self.processor.interval for i in range(int(self.processor.span))]  # Timeline of intervals
        keywords = list(self.processor.keywords_counter.keys())  # List of keywords

        # Plot keyword frequencies over time
        plt.figure(figsize=(12, 6))
        for keyword in keywords:
            plt.plot(timeline, self.processor.keywords_counter[keyword], label=keyword)

        # Add labels and legend
        plt.title('Keyword Frequencies Over Time')
        plt.xlabel('Time')
        plt.ylabel('Frequency')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Show plot
        plt.show()
