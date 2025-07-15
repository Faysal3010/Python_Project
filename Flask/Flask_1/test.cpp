#include <iostream>
#include <chrono>

using namespace std;

// টাইম মাপার ডেকোরেটর টাইপ ফাংশন
template<typename Func>
void cal_time_decorator(Func func, const string& func_name) {
    auto start = chrono::high_resolution_clock::now();
    func(); // ফাংশন কল
    auto end = chrono::high_resolution_clock::now();

    chrono::duration<double> duration = end - start;
    cout << func_name << " : " << duration.count() << " seconds" << endl;
}

// fast_time ফাংশন
void fast_time() {
    for (int i = 0; i < 10000000; ++i) {
        int x = i * i;
    }
}

// slow_time ফাংশন
void slow_time() {
    for (int i = 0; i < 100000000; ++i) {
        int x = i * i;
    }
}

int main() {
    cal_time_decorator(fast_time, "fast_time");
    cal_time_decorator(slow_time, "slow_time");
    return 0;
}