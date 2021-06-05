import copy
import random


class Hat:

    def __init__(self, **balls):
        t = [[key] * int(value) for key, value in balls.items()]
        self.contents = [item for sublist in t for item in sublist]

    def _returnRandom(self):
        res = random.choice(self.contents)
        self.contents.remove(res)
        return res

    def draw(self, count):
        response = []
        if len(self.contents) < count:
            response = copy.deepcopy(self.contents)
            self.contents = []
            return response
        for i in range(count):
            res = self._returnRandom()
            response.append(res)
        return response


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    favoured_outcome = 0
    for i in range(num_experiments):
        hatObj = copy.deepcopy(hat)
        balls = hatObj.draw(num_balls_drawn)
        favoring = 0
        for ball in expected_balls:
            if balls.count(ball) >= int(expected_balls[ball]):
                favoring = 1
                continue
            else:
                favoring = 0
                break
        if favoring:
            favoured_outcome += 1
    return favoured_outcome / num_experiments


hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=1000)
print("Probability:", probability)
