class class1:
    def __init__(self, config):
        self.batch_size = config.batch_size
        self.num_steps = config.num_steps

class config:
    batch_size = 10
    num_steps = 50


if __name__ == '__main__':
    newIns = class1(config)
    print(newIns.batch_size)
    print(newIns.num_steps)