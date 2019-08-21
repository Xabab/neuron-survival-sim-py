from math import tanh, atan, tau

from engine import GameConstants
from logic.Entities.Creature import *
from logic.Entities.FoodPiece import FoodPiece
from logic.Vector2d import Vector2d


class Game:
    desiredIterationCount: int = 1
    theChosenOne: Creature = None
    creatures = []
    food = []
    sightCircle = []
    DIST_NEURON_MAGICAL_CONSTANT: float

    def __init__(self):
        if FOG_OF_WAR:
            self.DIST_NEURON_MAGICAL_CONSTANT = SIGHT_DISTANCE / 10  # UPD: wtf is that?
            for x in range(-GameConstants.SIGHT_DISTANCE_CELLS, GameConstants.SIGHT_DISTANCE_CELLS):
                for y in range(-GameConstants.SIGHT_DISTANCE_CELLS, GameConstants.SIGHT_DISTANCE_CELLS):
                    if sqrt((x * CELL_SIZE) ** 2 + (y * CELL_SIZE) ** 2) < GameConstants.SIGHT_DISTANCE / 2 + CELL_SIZE:
                        self.sightCircle.append([x, y])

            print(self.sightCircle)
        else:
            self.DIST_NEURON_MAGICAL_CONSTANT = FIELD_SIZE_X / (CREATURE_SIZE * 2)

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

    def inSightCell(self, c: Creature, f: FoodPiece) -> bool:
        if not FOG_OF_WAR:
            return True

        relativeCellX = int(f.xy.x / CELL_SIZE) - int(c.xy.x / CELL_SIZE)
        relativeCellY = int(f.xy.y / CELL_SIZE) - int(c.xy.y / CELL_SIZE)

        if (abs(relativeCellX) > SIGHT_DISTANCE_CELLS) | (abs(relativeCellY) > SIGHT_DISTANCE_CELLS):
            return False

        for s in range(0, len(self.sightCircle)):
            if self.sightCircle[s][0] == relativeCellX:
                if self.sightCircle[s][1] == relativeCellY:
                    return True

        return False

    def findClosestFoodDistanceAndDirection(self, c: Creature):
        dist = 100000.  # inf

        temp = self.food[0]

        for f in self.food[:]:
            if not self.inSightCell(c, f):
                continue
            dt = sqrt((c.xy.x - f.xy.x) ** 2 + (c.xy.y - f.xy.y) ** 2)

            if FOG_OF_WAR & (dt > SIGHT_DISTANCE / 2):
                continue

            d = dt

            if d < dist:
                dist = d
                temp = f

            # check for food collisions and eat

            if d < CREATURE_SIZE:  # & "Eat" neuron > 0
                c.feed(FOOD_COST)
                self.food.remove(f)

        if dist == 100000.:
            return Vector2d(100000., 0)

        out = Game.distanceAndDirection(c.xy, temp.xy, c)

        return out

    @staticmethod
    def distanceAndDirection(m1: Vector2d, m2: Vector2d, c: Creature):
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

        direction += pi + c.direction  # -dir

        while direction < (-pi):
            direction += tau

        while direction > (pi):
            direction -= tau

        return Vector2d(temp.length(), -direction)

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
            tmp = self.findClosestFoodDistanceAndDirection(self.creatures[c])
            # tmp = Vector2d(1, -pi)

            # update inputs
            self.creatures[c].updateInputs([
                2 * tanh((self.DIST_NEURON_MAGICAL_CONSTANT / tmp.x)) - 1,  # 1st input done
                tanh(tmp.y / pi * 4),  # done
                tanh((self.creatures[c].fitness / BIRTH_FITNESS_COST / 2) * 6 - 3),  # 3d done
                tanh((self.creatures[c].speed.length() + 0.000001) / CREATURE_SPEED * 6 - 3)  # 4th done
            ])

            dirTmp = tmp.y + self.creatures[c].direction
            while dirTmp < (-pi):
                dirTmp += tau

            while dirTmp > (pi):
                dirTmp -= tau

            self.creatures[c].updateInfo([tmp.x, dirTmp, self.creatures[c].fitness, self.creatures[c].speed.length()])

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
                if self.creatures[c].fitness > BIRTH_FITNESS_REQUIRMENT:
                    self.creatures.append(self.creatures[c].giveBirth())  # else creature.feed(- BIRTH_FITNESS_COST);

        for c in self.creatures[:]:
            if c.fitness < 0:
                # print("dead ☠")
                self.creatures.remove(c)


g = Game()
