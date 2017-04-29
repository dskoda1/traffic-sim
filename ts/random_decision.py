import random

class RandomDecision(object):
    """This class is used for making choices between various options.
    It allows the user to pass in an array of options at initialization
    time, and each time the choice() method is called one option will
    be picked according to the weights provided.
    """

    def __init__(self, choices):
        """Init occurs with a list of objects, `choices`. Each object must
        be able to index the key `weight`. These weights will be taken
        in consideration for future `choice` calls.
        """
        self.choices = choices
        #self.total_weight = sum([x['weight'] for x in choices])
        self.weight = 0
        self.weights = {}
        # This loop creates a hash map of effectively pointers to each
        # choice, which only takes up O(N) space where N is all of the
        # weights aggregated, since the value for each entry is a pointer.
        for choice in choices:
            for x in range(choice['weight']):
                self.weights[self.weight + x] = choice
            self.weight = choice['weight']

    def choice(self):
        return self.weights[random.randint(0, len(self.weights) - 1)]
