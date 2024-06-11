#include <iostream>
#include <vector>
#include <cmath>
#include <random>

constexpr int X = 10;
constexpr int Y = 10;
constexpr int n = 500;
constexpr double field = 0;

std::vector<std::vector<bool>> gen_grid(int x, int y) {
    std::vector<std::vector<bool>> grid(x, std::vector<bool>(y));
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, 1);

    for (int i = 0; i < x; ++i) {
        for (int j = 0; j < y; ++j) {
            grid[i][j] = dist(gen);
        }
    }
    return grid;
}

double energy(int X, int Y, const std::vector<std::vector<bool>>& grid) {
    double E = 0.0;
    for (int i = 0; i < X; ++i) {
        for (int j = 0; j < Y; ++j) {
            int d_10 = grid[(i + 1) % X][j] ? 1 : -1;
            int d_12 = grid[(i - 1 + X) % X][j] ? 1 : -1;
            int d_01 = grid[i][(j + 1) % Y] ? 1 : -1;
            int d_21 = grid[i][(j - 1 + Y) % Y] ? 1 : -1;
            int S = d_10 + d_12 + d_01 + d_21;
            E += (S + field) * (grid[i][j] ? 1 : -1);
        }
    }
    return -E;
}

std::vector<double> glauber_warp(int X, int Y, int n, double T, std::vector<std::vector<bool>>& grid) {
    std::vector<double> engs(X * Y);
    int x = X - 1;
    int y = Y - 1;
    int iters = (x + 1) * (y + 1) * n;
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dist(0.0, 1.0);

    for (int k = 0; k < iters; ++k) {
        int i = rd() % X;
        int j = rd() % Y;
        int d_11 = grid[i][j] ? 1 : -1;
        int d_10 = grid[(i + 1) % X][j] ? 1 : -1;
        int d_12 = grid[(i - 1 + X) % X][j] ? 1 : -1;
        int d_01 = grid[i][(j + 1) % Y] ? 1 : -1;
        int d_21 = grid[i][(j - 1 + Y) % Y] ? 1 : -1;
        int S = d_10 + d_12 + d_01 + d_21;
        double E = 2.0 * d_11 * (S + field);
        double p = 1.0 / (1.0 + std::exp(E / T));
        double t = dist(gen);
        if (t < p) {
            grid[i][j] = !grid[i][j];
        }
        if (k % n == 0) {
            engs[k / n] = energy(X, Y, grid);
        }
    }
    return engs;
}

constexpr int temps = 50;
constexpr int reps = 100;

int main()
{   
    int N = X * Y;
    double means[temps];
    double variances[temps];
    std::vector<std::vector<bool>> grid = gen_grid(X, Y);
    std::vector<double> vals;
    for (int i = 0; i < temps; ++i) {
        double T = 0.2 + 5 * i / temps;
        double mean = 0;
        double variance = 0;
        for (int j = 0; j < reps; ++j) {
            double m = 0;
            double v = 0;
            for (double x : vals) {
                double delta = x - m;
                m += delta / N;
                v += delta * (x - m);
            }
            mean = mean + m;
            variance = variance + v/N;
            vals = glauber_warp(X, Y, n, T, grid);
            grid = gen_grid(X, Y);
        }
        mean = mean / reps;
        variance = variance / reps;
        means[i] = mean;
        variances[i] = variance;
    }
    for (int value : means) {
        std::cout << value << " ";
    }
    std::cout << "\n";
    for (int value : variances) {
        std::cout << value << " ";
    }
    std::cout << std::endl;
    return 0;
}