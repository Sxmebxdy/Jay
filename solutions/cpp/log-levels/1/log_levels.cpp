#include <string>

namespace log_line {
std::string message(std::string line) {
    int pos = line.find(":");
    return line.substr(pos + 2);
}

std::string log_level(std::string line) {
    int anfang = line.find("[");
    int ende = line.find("]");
    return line.substr(anfang+1, ende-1);
}

std::string reformat(std::string line) {
    std::string msg = message(line);
    std::string lvl = log_level(line);
    return msg + " " + "(" + lvl + ")";
}
}  // namespace log_line
