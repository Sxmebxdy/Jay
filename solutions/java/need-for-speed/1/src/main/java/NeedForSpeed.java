class NeedForSpeed {
    private int speed;
    private int batteryDrain;
    private int battery = 100;
    public int distanceDriven;
    
    NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
    }

    public boolean batteryDrained() {
        if (battery < batteryDrain){
            return true;
        }
        return false;
    }

    public int distanceDriven() {
        return this.distanceDriven;
    }

    public void drive() {
        if (battery >= batteryDrain){
            distanceDriven += speed;
            battery -= batteryDrain;
        }
       
    }

    public static NeedForSpeed nitro() {
        NeedForSpeed car = new NeedForSpeed(50, 4);
        return car;
    }
}

class RaceTrack {
    int distance;
    RaceTrack(int distance) {
        this.distance = distance;
    }

    public boolean canFinishRace(NeedForSpeed car) {
            while (distance > car.distanceDriven){
                if (car.batteryDrained()){
                    return false;
               }
                car.drive();
            }
        return true;
    }
}
