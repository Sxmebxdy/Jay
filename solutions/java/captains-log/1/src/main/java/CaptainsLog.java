import java.util.Random;

class CaptainsLog {

    private static final char[] PLANET_CLASSES = new char[]{'D', 'H', 'J', 'K', 'L', 'M', 'N', 'R', 'T', 'Y'};

    private Random random;

    CaptainsLog(Random random) {
        this.random = random;
    }

    char randomPlanetClass() {
        int r = random.nextInt(10);
        return PLANET_CLASSES[r];
    }

    String randomShipRegistryNumber() {
        int r = random.nextInt(1000, 10000);
        return "NCC-" + r;
    }

    double randomStardate() {
        double r = random.nextDouble();
        return 41000.0 + r * 1000.0;
    }
}
