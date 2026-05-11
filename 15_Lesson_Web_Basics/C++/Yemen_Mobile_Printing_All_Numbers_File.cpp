#include <iostream>
#include <fstream>

int main() {

    std::ofstream file("numbers.txt");

    for (int num = 770000000; num <= 779999999; num++) {
        file << num << '\n';
    }

    file.close();

    std::cout << "Done.\n";

    return 0;
}