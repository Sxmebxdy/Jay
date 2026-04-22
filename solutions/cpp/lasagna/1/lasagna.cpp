// ovenTime returns the amount in minutes that the lasagna should stay in the
// oven.
int ovenTime() {
    int neededtime{40};
    return neededtime;
}

/* remainingOvenTime returns the remaining
   minutes based on the actual minutes already in the oven.
*/
int remainingOvenTime(int actualMinutesInOven) {
    int remaining{ovenTime() - actualMinutesInOven};
    return remaining;
}

/* preparationTime returns an estimate of the preparation time based on the
   number of layers and the necessary time per layer.
*/
int preparationTime(int numberOfLayers) {
    int layertime{numberOfLayers * 2};
    return layertime;
}

// elapsedTime calculates the total time spent to create and bake the lasagna so
// far.
int elapsedTime(int numberOfLayers, int actualMinutesInOven) {
    int total{preparationTime(numberOfLayers) + actualMinutesInOven};
    return total;
}
