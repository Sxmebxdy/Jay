class Fighter {

    boolean isVulnerable() {
        return true;
    }

    int getDamagePoints(Fighter fighter) {
        return 1;
    }
}

class Warrior extends Fighter {
    
    @Override
    public String toString(){
        return "Fighter is a Warrior";
    }

    @Override
    boolean isVulnerable() {
        return false;
    }

    @Override
    int getDamagePoints(Fighter fighter){
        if (!fighter.isVulnerable()){
            return 6;
        }
        return 10;
    }
}

class Wizard extends Fighter{
    boolean prepared;
    @Override
    public String toString(){
        return "Fighter is a Wizard";
    }

    boolean prepareSpell(){
        this.prepared = true;
        return prepared;
    }

    @Override 
    boolean isVulnerable(){
        if (prepared){
            return false;
        }
        return true;
    }
    @Override
    int getDamagePoints(Fighter fighter){
        if (prepared){
            return 12;
        }
        return 3;
    }
}
