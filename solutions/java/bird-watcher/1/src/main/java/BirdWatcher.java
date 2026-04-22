
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        int [] lastWeek = {0, 2, 5, 3, 7, 8, 4};
        return lastWeek;
    }

    public int getToday() {
        int laenge = birdsPerDay.length;
        return birdsPerDay[laenge - 1];
    }

    public void incrementTodaysCount() {
        int laenge = birdsPerDay.length;
        birdsPerDay[laenge - 1] += 1;
    }

    public boolean hasDayWithoutBirds() {
        for (int i = 0; i < birdsPerDay.length; i++){
            if (birdsPerDay[i] == 0){
                return true;
            }
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int sum = 0;
        if (numberOfDays > birdsPerDay.length){
            for (int i = 0; i < birdsPerDay.length; i++){
                sum += birdsPerDay[i];
            }
            return sum;
        }
        for (int i = 0; i < numberOfDays; i++){
            sum += birdsPerDay[i];
        }
        return sum;
    }

    public int getBusyDays() {
        int sum = 0;
        for (int i = 0; i < birdsPerDay.length; i++){
            if (birdsPerDay[i] >= 5){
                sum += 1;
            }
        }
        return sum;
    }
}
