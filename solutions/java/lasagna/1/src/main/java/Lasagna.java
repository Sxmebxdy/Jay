public class Lasagna {
    public int expectedMinutesInOven(){
        return 40;
    }
    public int remainingMinutesInOven(int m){
        return 40 - m;
    }
    public int preparationTimeInMinutes(int p){
        return p * 2;
    }
    public int totalTimeInMinutes(int layers, int time){
        int sum = 0;
        sum = time + preparationTimeInMinutes(layers);
        return sum;
    }

    // TODO: define the 'totalTimeInMinutes()' method
}
