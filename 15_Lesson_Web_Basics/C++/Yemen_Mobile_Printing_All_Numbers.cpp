#include <iostream>

int main()
{
    long long start_number = 770000000;
    long long end_number = 779999999;

    for(long long number = start_number; number <= end_number; number++)
    {
        std::cout<< number << std::endl;
    }

    return 0;
}