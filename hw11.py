import numpy as np

# Vor sezonin e patkanum xndzor@ (summer, autumn, winter)

# Y - season: summer, autumn, winter;
# X color: green - summer(0), yellow - autumn(1), red - winter(2);
# X sort: yubilyar - summer(0), golden - autumn(1), kexura - winter(2);
# X size: small - summer(0), medium - autumn (1), big - winter(2);

class ApplesANN:
    def __init__(self, color=0, sort=1, size=2):
        self.color = color
        self.sort = sort
        self.size = size

    def activate (self, signal):
        if signal > 0.7:
            return 2 #winter
        elif signal > 0.4:
            return 1 # autumn
        else:
            return 0 # summer

    def predict(self):
        inputs = np.array([self.color, self.sort, self.size]) # Inputs(X - features)
        weights_input_to_hiddenOne = [0, 0.1, 0.3]
        weights_input_to_hiddenTwo = [0.1, 0.5, 0.4]
        weights_input_to_hiddenThree = [0.6, 0.2, 0.9]
        weights_input_to_hidden = np.array([weights_input_to_hiddenOne, weights_input_to_hiddenTwo, weights_input_to_hiddenThree])
        weights_hidden_to_output = np.array([0.2, 0.4, 0.7])

        #prediction
        from_input_to_hidden = np.dot(weights_input_to_hidden, inputs)
        hidden_activation = np.array([self.activate(s) for s in from_input_to_hidden]) # s - from_input_to _hidden elementnern en
        from_hidden_to_output = np.dot(weights_hidden_to_output, hidden_activation)
        output_activation = self.activate(from_hidden_to_output)
        return output_activation

model = ApplesANN(1, 1, 1)
print(model.predict())