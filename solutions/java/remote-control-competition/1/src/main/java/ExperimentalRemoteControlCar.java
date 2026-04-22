public class ExperimentalRemoteControlCar implements RemoteControlCar {
    int units = 0;
    public void drive() {
        units += 20;
    }

    public int getDistanceTravelled() {
        return this.units;
    }
}

