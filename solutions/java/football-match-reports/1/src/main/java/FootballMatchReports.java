public class FootballMatchReports {
    public static String onField(int shirtNumber) {
        if (shirtNumber < 1 || shirtNumber > 11) {
            throw new IllegalArgumentException("Invalid shirt number: " + shirtNumber);
        }

        switch (shirtNumber) {
            case 1:
                return "goalie";
            case 2:
                return "left back";
            case 3:
            case 4:
                return "center back";
            case 5:
                return "right back";
            case 6:
            case 7:
            case 8:
                return "midfielder";
            case 9:
                return "left wing";
            case 10:
                return "striker";
            case 11:
                return "right wing";
            default:
                // Diese Zeile ist eigentlich nicht mehr nötig, da oben geprüft wird.
                return "unknown";
        }
    }
}

