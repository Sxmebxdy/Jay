import java.util.ArrayList;
import java.util.List;

public class LanguageList {
    private final List<String> languages = new ArrayList<>();

    public boolean isEmpty() {
        if (languages.isEmpty()){
            return true;
        }
        return false;
    }

    public void addLanguage(String language) {
        languages.add(language);
    }

    public void removeLanguage(String language) {
        languages.remove(language);
    }

    public String firstLanguage() {
        return languages.get(0);
    }

    public int count() {
        int sum = 0;
        for (int i = 0; i < languages.size(); i++){
            sum += i;
        }
        return sum;
    }

    public boolean containsLanguage(String language) {
        for (int i = 0; i < languages.size(); i++){
            if (languages.get(i).equals(language)){
                return true;
            }
        }
        return false;
    }

    public boolean isExciting() {
        if (containsLanguage("Java") || containsLanguage("Kotlin")){
            return true;
        }
        return false;
    }
}
