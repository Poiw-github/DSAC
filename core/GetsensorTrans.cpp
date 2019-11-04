#include <bits/stdc++.h>

#include "properties.h"
#include "util.h"
#include "thread_rand.h"
#include "generic_io.h"

using namespace std;

int main() 
{
    cv::Mat_<double> sensorTrans;
    std::ifstream calibFile("./sensorTrans.dat", std::ios::binary | std::ios_base::in);
    jp::read(calibFile, sensorTrans);
    std::cout << sensorTrans << std::endl << std::endl;
    std::ofstream fout("./sensorTrans.txt");
    for(int i = 0; i < 4; i++)
        for(int j = 0; j < 4; j++)
            fout << sensorTrans(i, j) << (j == 3 ? '\n' : ' ');
    return 0;
}