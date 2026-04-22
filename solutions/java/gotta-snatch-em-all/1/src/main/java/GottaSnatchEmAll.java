import java.util.List;
import java.util.Set;
import java.util.HashSet;

class GottaSnatchEmAll {

    static Set<String> newCollection(List<String> cards) {
        return new HashSet<>(cards);
    }

    static boolean addCard(String card, Set<String> collection) {
        if (collection.contains(card)){
            return false;
        }
        collection.add(card);
        return true;
    }

    
    static boolean canTrade(Set<String> myCollection, Set<String> theirCollection) {
        if (myCollection.isEmpty() || theirCollection.isEmpty()){
            return false;
        }
        else if (myCollection.equals(theirCollection)){
            return false;
        }
        else if (myCollection.containsAll(theirCollection) || theirCollection.containsAll(myCollection)){
            return false;
        }
        return true;
    }

    static Set<String> commonCards(List<Set<String>> collections) {
        if (collections == null || collections.isEmpty()){
            return new HashSet<>();
        }
        Set<String> commonCards = new HashSet<>(collections.get(0));
        for (int i = 1; i < collections.size(); i ++){
            commonCards.retainAll(collections.get(i));
        }
        return commonCards;
        }
    

    static Set<String> allCards(List<Set<String>> collections) {
        Set<String> allCards = new HashSet<>();
        for (Set card: collections){
            allCards.addAll(card);
        }
        return allCards;
    }
}
