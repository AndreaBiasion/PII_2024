class Detector:
    def __init__(self):
        self.treshold = 0.02
        self.vector = None
        pass

    def detect(self, processor):
        self.vector = [0] * len(processor.normalized_vector)

        for i in range(len(processor.normalized_vector)):
            if processor.normalized_vector[i] > self.treshold:
                self.vector[i] = 1