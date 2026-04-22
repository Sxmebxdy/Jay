public class LogLine {
    private String logLine;
    public LogLine(String logLine) {
        this.logLine = logLine;
    }

    public LogLevel getLogLevel() {
        String levelCode = logLine.substring(1, 4);
        switch (levelCode) {
            case "TRC": return LogLevel.TRACE;
            case "DBG": return LogLevel.DEBUG;
            case "INF": return LogLevel.INFO;
            case "WRN": return LogLevel.WARNING;
            case "ERR": return LogLevel.ERROR;
            case "FTL": return LogLevel.FATAL;
            default: return LogLevel.UNKNOWN;
        }
        
    }

    public String getOutputForShortLog() {
        String level = logLine.substring(1, 4);
        String ende = logLine.substring(7);
        switch (level){
            case "TRC": return "1:" + ende;
            case "DBG": return "2:" + ende;
            case "INF": return "4:" + ende;
            case "WRN": return "5:" + ende;
            case "ERR": return "6:" + ende;
            case "FTL": return "42:" + ende;
            default: return "0:" + ende;
        }
    }
}
