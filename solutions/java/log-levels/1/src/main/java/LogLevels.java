public class LogLevels {
    
    public static String message(String logLine) {
        int colonIndex = logLine.indexOf(":");
        String message = logLine.substring(colonIndex + 1);
        return message.trim();
    }

    public static String logLevel(String logLine) {
        int start = logLine.indexOf("[") + 1;
        int ende = logLine.indexOf("]");
        String level = logLine.substring(start, ende);
        return level.toLowerCase();
    }

    public static String reformat(String logLine) {
        String letzterTeil = message(logLine);
        String ersterTeil = logLevel(logLine);
        String Ergebnis = letzterTeil + " (" + ersterTeil + ")";
        return Ergebnis;
    }
}
