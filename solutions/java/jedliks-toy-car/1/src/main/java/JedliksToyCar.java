public class JedliksToyCar {
    int Meter = 0;
    int battery = 100;
    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + Meter +  " meters";
    }

    public String batteryDisplay() {
        if (battery > 0){
            return "Battery at " + battery + "%";
        }
        return "Battery empty";
        
    }

    public void drive() {
        if (battery > 0){
            Meter = Meter + 20;
            battery = battery - 1;
        }
    }
}
