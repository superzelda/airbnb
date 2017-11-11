#include <iostream>
#include <vector>
using namespace std;

class vec2d{
public:
    vector<vector<int>>:: iterator begin, end, row;
    int col = 0;
    vec2d(vector<vector<int>>& nums) {
        begin = nums.begin();
        end = nums.end();
        row = nums.begin();
    }
    int next() {
        if (hasNext()) {
            return (*row)[col++];
        } else {
            cout << "invalid operation" << endl;
        }
    }
}