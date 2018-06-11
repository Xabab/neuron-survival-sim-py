from math import tanh, atan, tau

from src.logic.Entities.Creature import *
from src.logic.Entities.FoodPiece import FoodPiece
from src.logic.Vector2d import Vector2d


class Game:
    desiredIterationCount: int = 1
    theChosenOne: Creature = None
    creatures = []
    food = []
    sightCircle = []

    def __init__(self):

        self.startSpawn()

    def startSpawn(self):
        for i in range(0, MIN_CREATURES_COUNT):
            self.creatures.append(Creature(random() * FIELD_SIZE_X, random() * FIELD_SIZE_Y))
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
            direction = atan(temp.y / temp.x)
        else:
            if (temp.x > 0.) & (temp.y < 0.):
                direction = atan(temp.y / temp.x)
            else:
                if temp.x < 0.:
                    direction = atan(temp.y / temp.x) - pi
                else:
                    if (temp.x == 0.) & (temp.y > 0.):  # redundant
                        direction = pi / 2
                    else:
                        if (temp.y == 0.) & (temp.y < 0.):  # redundant
                            direction = 3 * pi / 2
                        else:
                            direction = 0  # redundant

        direction += pi

        while direction < (-pi):
            direction += tau

        while direction > (pi):
            direction -= tau

        return Vector2d(temp.length(), direction)

    def creatureClick(self, x: int, y: int):
        c: Creature
        for i in range(0, len(self.creatures)):
            c = self.creatures[i]
            if (x < c.xy.x + CREATURE_SIZE) & (x > c.xy.x - CREATURE_SIZE) & \
                    (y < c.xy.y + CREATURE_SIZE) & (y > c.xy.y - CREATURE_SIZE):
                return c
        return None

    def choseCreature(self, x: int, y: int):
        if len(self.creatures) <= 0:
            return
        self.theChosenOne = self.creatureClick(x - FIELD_X_OFFSET, y)

    def iteration(self):
        # print("iteration")
        # spawn new if needed
        for i in range(len(self.creatures), MIN_CREATURES_COUNT):
            # print("creature spawn in iteration", i)
            self.creatures.append(Creature(random() * FIELD_SIZE_X, random() * FIELD_SIZE_Y))

        # spawn food if needed
        while len(self.food) < FOOD_COUNT:
            self.food.append(FoodPiece(random() * FIELD_SIZE_X, random() * FIELD_SIZE_Y))

        for c in range(0, len(self.creatures)):
            # todo optimise food search: next line takes 2/3 of computation time!
            tmp = self.findClosestFoodDistanceAndDirection(self.creatures[c])
            # tmp = Vector2d(1, -pi)


            # todo fix input ranges
            # update inputs
            self.creatures[c].updateInputs([
                tanh((FIELD_SIZE_X / 10) / tmp.x),  # 1st input done
                tanh(tmp.y),  # 2d input done
                tanh((self.creatures[c].fitness / BIRTH_FITNESS_COST) * 6 - 3),  # 3d done
                tanh((self.creatures[c].speed.length() + 0.000001) / CREATURE_SPEED * 6 - 3)  #
            ])

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
                # print("dead ☠")
                self.creatures.remove(c)


g = Game()
