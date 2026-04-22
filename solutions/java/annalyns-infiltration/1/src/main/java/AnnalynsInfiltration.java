class AnnalynsInfiltration {
    public static boolean canFastAttack(boolean knightIsAwake) {
        return !knightIsAwake;
    }

    public static boolean canSpy(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake) {
        if (knightIsAwake || archerIsAwake || prisonerIsAwake){
            return true;
        }
        return false;
    }

    public static boolean canSignalPrisoner(boolean archerIsAwake, boolean prisonerIsAwake) {
        if (prisonerIsAwake && !archerIsAwake){
            return true;
        }
        return false;
    }

    public static boolean canFreePrisoner(boolean knightIsAwake, boolean archerIsAwake, boolean prisonerIsAwake, boolean petDogIsPresent) {
        if (petDogIsPresent) {
            // She can rescue the prisoner if the archer is asleep.
            // The knight's state doesn't matter because of the dog.
            return !archerIsAwake;
        } else {
            // Rule 2: If Annalyn does not have her pet dog
            // She can free the prisoner if the prisoner is awake AND both the knight and archer are sleeping.
            // If the prisoner is sleeping, they can't be rescued.
            return prisonerIsAwake && !knightIsAwake && !archerIsAwake;
        }
    }
}
