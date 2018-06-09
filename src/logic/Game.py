from src.logic.Entities.Creature import *
from src.logic.Entities.FoodPiece import FoodPiece
from src.logic.Vector2d import Vector2d


class Game:
    desiredIterationCount: int = 1
    theChosenOne: Creature
    creatures = []
    food = []

    def __init__(self):
        self.startSpawn()

    def startSpawn(self):
        for i in range(0, MIN_CREATURES_COUNT):
            self.creatures.append(Creature())
        for i in range(0, FOOD_COUNT):
            self.food.append(FoodPiece(random() * FIELD_SIZE_X, random() * FIELD_SIZE_Y))

    def iterationCount_pp(self):
        if self.desiredIterationCount >= 10:
            return
        print("++")
        self.desiredIterationCount = self.desiredIterationCount + 1

    def iterationCount_mm(self):
        if self.desiredIterationCount <= 0:
            return
        print("--")
        self.desiredIterationCount = self.desiredIterationCount - 1

    def update(self):
        for i in range(0, self.desiredIterationCount):
            self.iteration()

    def findClosestFoodDistanceAndDirection(self, c: Creature):
        dist = 100000.  # inf

        temp = self.food[0]

        for i in self.food[:]:
            out = Game.findDistanceAndDirection(c.xy, i.xy)

            d = out.x

            if d < dist:
                dist = d
                temp = i

            # check for food collisions and eat

            if out.x < CREATURE_SIZE:  # & "Eat" neuron > 0
                c.feed(FOOD_COST)
                self.food.remove(i)

        out = Game.findDistanceAndDirection(c.xy, temp.xy)

        return out

    @staticmethod
    def findDistanceAndDirection(m1: Vector2d, m2: Vector2d):
        temp = Vector2d(-(m2.x - m1.x), m2.y - m1.y)

        if (temp.x > 0.) & (temp.y >= 0.):
            direction = np.arctan(temp.y / temp.y)
        else:
            if (temp.x > 0.) & (temp.y < 0.):
                direction = np.arctan(temp.y / temp.x) + 2 * np.pi
            else:
                if temp.x < 0.:
                    direction = np.arctan(temp.y / temp.x) + np.pi
                else:
                    if (temp.x == 0.) & (temp.y > 0.):
                        direction = np.pi / 2
                    else:
                        if (temp.y == 0.) & (temp.y < 0.):
                            direction = 3 * np.pi / 2
                        else:
                            direction = 0

        direction += np.pi

        return Vector2d(temp.length(), direction)

    def creatureClick(self, x: int, y: int):
        for i in range(0, len(self.creatures)):
            if (x - self.creatures[i].xy.x) * (y - self.creatures[i].xy.y) < CREATURE_SIZE * CREATURE_SIZE:
                return self.creatures[i]
        return None

    def choseCreature(self, x: int, y: int):
        if len(self.creatures) <= 0:
            return
        self.theChosenOne = self.creatureClick(x, y)

    def iteration(self):
        # print("iteration")
        # spawn new if needed
        for i in range(len(self.creatures), MIN_CREATURES_COUNT):
            print("creature spawn in iteration", i)
            self.creatures.append(Creature())

        # spawn food if needed
        while len(self.food) < FOOD_COUNT:
            self.food.append(FoodPiece())

        for c in range(0, len(self.creatures)):
            tmp = self.findClosestFoodDistanceAndDirection(self.creatures[c])

            # update inputs
            self.creatures[c].updateInputs([np.tanh(tmp.x / FIELD_SIZE_X),
                                            - tmp.y,
                                            np.tanh(self.creatures[c].fitness / BIRTH_FITNESS_COST),
                                            np.tanh(self.creatures[c].speed.length()) / (
                                                        CREATURE_SIZE * CREATURE_SPEED)])

            self.creatures[c].updateInfo([tmp.x, -tmp.y, self.creatures[c].fitness, self.creatures[c].speed.length()])

            # update creatures
            self.creatures[c].updateCreature()

            # check collisions with walls
            if self.creatures[c].xy.x < 0:
                self.creatures[c].xy.x = 0
            else:
                if self.creatures[c].xy.x > FIELD_SIZE_X:
                    self.creatures[c].xy.x = FIELD_SIZE_X

            if self.creatures[c].xy.y < 0:
                self.creatures[c].xy.y = 0
            else:
                if self.creatures[c].xy.y > FIELD_SIZE_Y:
                    self.creatures[c].xy.y = FIELD_SIZE_Y

        # give birth

        for c in range(0, len(self.creatures)):
            if self.creatures[c].brain.neuronLayers[len(self.creatures[c].brain.neuronLayers) - 1][0][3] \
                    > BIRTH_NEURON_ACTIVATION:
                if self.creatures[c].fitness > BIRTH_FITNESS_COST:
                    self.creatures.append(self.creatures[c].giveBirth())  # else creature.feed(- BIRTH_FITNESS_COST);

        for c in self.creatures[:]:
            if c.fitness < 0:
                print("dead ☠")
                self.creatures.remove(c)


g = Game()
