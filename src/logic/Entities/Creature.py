from src.logic import Vector2d


class Creature:

    xy: Vector2d
    speed: Vector2d

    fitness: float

    direction: float

    debug_info: float

    def __init__(self, x: float, y: float):
        self.xy = Vector2d.Vector2d(x, y)




'''
package logic.entities.creature;

import logic.GameConstants;
import logic.entities.Brain;
import logic.entities.Vector2d;

import static java.lang.Math.*;
import static logic.GameConstants.FIELD_SIZE_X;
import static logic.GameConstants.FIELD_SIZE_Y;
import static logic.GameConstants.FITNESS_DEGRADATION;

public class Creature extends Brain{
    //private boolean readyToBirth = false;

    private double fitness;
    //private int age = 0;

    private Vector2d xy;
    private Vector2d speed;
    private double direction;
    double[] info = new double[getNeuronLayers()[0].getColumnDimension() - 1];

    public double[] getInfo(){
        double[] out = new double[info.length];
        System.arraycopy(info, 0, out, 0, info.length);
        return out;
    }

    //private String name;
    //private String type = "Herbivore";

    /*public void addAge(double aging){
        if (aging > 0) age += (aging);
    }

    public double getAge() {
        return age;
    }*/


    public Creature(){
        super(new String[]{"Food dist", "Food dir", "Fitness", "Speed"}, new String[]{"Eat", "Accelerate", "Turn", "Birth"});
        fitness = GameConstants.STARTING_FITNESS;
        direction = ((Math.random()*2)-1)*Math.PI*2;
        speed = new Vector2d(0);
        xy = new Vector2d(Math.random() * FIELD_SIZE_X, Math.random() * FIELD_SIZE_Y);
        initRandom(-GameConstants.BRAIN_INIT_RANGE, GameConstants.BRAIN_INIT_RANGE);
    }

    public Creature(double x, double y){
        this();
        speed = new Vector2d(0);
        xy.setVector(x, y);
        initRandom(-GameConstants.BRAIN_INIT_RANGE, GameConstants.BRAIN_INIT_RANGE);
    }

// --Commented out by Inspection START (24.04.18 12:24):
//    public Creature(Creature c){
//        super(c);
//        xy = new Vector2d(c.xy);
//
//        fitness = GameConstants.STARTING_FITNESS;
//        direction = ((Math.random()*2)-1)*Math.PI;
//        speed = new Vector2d(0, 0);
//    }
// --Commented out by Inspection STOP (24.04.18 12:24)

    public Creature child(){
        Creature c = new Creature();

        c.mutate();
        c.fitness = fitness;
        c.direction = direction;
        c.speed = speed;

        return c;
    }

    public double getFitness() {
        return fitness;
    }

// --Commented out by Inspection START (24.04.18 12:24):
//    public void setFitness(double fitness) {
//        this.fitness = fitness;
//    }
// --Commented out by Inspection STOP (24.04.18 12:24)


    public Vector2d getXY() {
        return xy;
    }

    public Vector2d getSpeed() {
        return speed;
    }

    public double getDirection() {
        return direction;
    }

    public Creature giveBirth(){
        //readyToBirth = false;
        fitness -= GameConstants.BIRTH_FITNESS_COST;

        return child();
    }

    public void updateInfo(double[] inputs){
        System.arraycopy(inputs, 0, info, 0, info.length);
    }

    private void updateMoving(){
        direction += GameConstants.CREATURE_TURNING_SPEED*
                getNeuronLayers()[getNeuronLayers().length - 1].get(0,1);

        if(direction > PI) direction -= 2*PI;
        if(direction < -PI) direction += 2*PI;

        double x = speed.getX() * (1 - GameConstants.SURFACE_ROUGHNESS)
                + GameConstants.ACCELERATION*getNeuronLayers()[getNeuronLayers().length - 1].get(0,0)*cos(direction);
        double y = speed.getY() * (1 - GameConstants.SURFACE_ROUGHNESS)
                + GameConstants.ACCELERATION*getNeuronLayers()[getNeuronLayers().length - 1].get(0,0)*sin(direction);
        double speed = sqrt(x*x + y*y);

        if(speed > GameConstants.CREATURE_SPEED) {
            x *= GameConstants.CREATURE_SPEED/speed;
            y *= GameConstants.CREATURE_SPEED/speed;
        }

        this.speed.setX(x);
        this.speed.setY(y);

        this.xy.add(this.speed);

        fitness -= abs(getNeuronLayers()[getNeuronLayers().length - 1].get(0,1) )*GameConstants.FOOD_PER_RAD
                + speed * GameConstants.FOOD_PER_PX
                + FITNESS_DEGRADATION;
    }

    private void move(){
        xy.add(speed);

    }

    public void updateCreature(){
        calculate();
        updateMoving();
        move();
    }

    /*public boolean isReadyToBirth() {
        return readyToBirth;
    }*/

    public void feed(double f){
        fitness += f;
    }

// --Commented out by Inspection START (24.04.18 12:24):
//    public double getSpeedDouble(){
//        return sqrt(speed.getX()*speed.getX() + speed.getY()*speed.getY());
//    }
// --Commented out by Inspection STOP (24.04.18 12:24)

    //public abstract void interactCreature(Creature c){}
}
'''