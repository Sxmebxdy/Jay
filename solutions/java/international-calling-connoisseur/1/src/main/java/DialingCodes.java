import java.util.Map;
import java.util.HashMap;

public class DialingCodes {
    Map<Integer, String> Codes = new HashMap<>();
    public Map<Integer, String> getCodes() {
        return Codes;
    }

    public void setDialingCode(Integer code, String country) {
        Codes.put(code, country);
    }

    public String getCountry(Integer code) {
        return Codes.get(code);
    }

    public void addNewDialingCode(Integer code, String country) {
        if (Codes.containsKey(code) || Codes.containsValue(country)){
        
        }
        else {
            Codes.put(code, country);
        }
    }

   public Integer findDialingCode(String country) {
    if (!Codes.containsValue(country)) {
        return null;
    }
    for (Map.Entry<Integer, String> entry : Codes.entrySet()) {
        if (entry.getValue().equals(country)) {
            return entry.getKey();
        }
    }
    return null;
}

    public void updateCountryDialingCode(int newCode, String country) {
    Integer oldCode = findDialingCode(country); 
    if (oldCode == null) {
        return; 
    }
    Codes.remove(oldCode);         
    Codes.put(newCode, country);  
}

}
