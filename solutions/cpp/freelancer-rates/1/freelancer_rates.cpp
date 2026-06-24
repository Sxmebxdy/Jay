#include <cmath> //to round numbers

// daily_rate calculates the daily rate given an hourly rate
double daily_rate(double hourly_rate) {
    double d_rate = 8 * hourly_rate;
    return d_rate;
}

// apply_discount calculates the price after a discount
double apply_discount(double before_discount, double discount) {
    double after_discount = before_discount * (1.0 - discount / 100.0);
    return after_discount;
}

// monthly_rate calculates the monthly rate, given an hourly rate and a discount
// The returned monthly rate is rounded up to the nearest integer.
int monthly_rate(double hourly_rate, double discount) {
    double d_rate = daily_rate(hourly_rate);
    double monthly_rate = d_rate * 22;
    double discounted_rate = apply_discount(monthly_rate, discount);
    return std::ceil(discounted_rate);
}

// days_in_budget calculates the number of workdays given a budget, hourly rate,
// and discount The returned number of days is rounded down (take the floor) to
// the next integer.
int days_in_budget(int budget, double hourly_rate, double discount) {
    double daily_cost = daily_rate(hourly_rate);
    double discounted_cost = apply_discount(daily_cost, discount);
    double work_days = budget / discounted_cost;
    return std::floor(work_days);
}
