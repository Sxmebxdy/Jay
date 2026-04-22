class ProductionRemoteControlCar implements RemoteControlCar, Comparable <ProductionRemoteControlCar> {
    int units = 0;
    int numberOfVictories = 0;
    public void drive() {
        units += 10;
    }

    public int getDistanceTravelled() {
        return this.units;
    }

    public int getNumberOfVictories() {
        return this.numberOfVictories;
    }

    public void setNumberOfVictories(int numberOfVictories) {
        this.numberOfVictories = numberOfVictories;
    }
    @Override
    public int compareTo (ProductionRemoteControlCar car){
        return Integer.compare(car.numberOfVictories, this.numberOfVictories);
    }
}
