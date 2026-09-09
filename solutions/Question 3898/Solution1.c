/*
 * Problem: 3898. Find the Degree of Each Vertex
 * Difficulty: Easy
 * Topics: Array, Graph Theory, Matrix
 * URL: https://leetcode.com/problems/find-the-degree-of-each-vertex/
 * Runtime: 3 ms
 * Memory: 18.4 MB
 * Solved via CodePath Auto-Committer
 */

#include <stdlib.h>

int* findDegrees(int** matrix, int matrixSize, int* matrixColSize, int* returnSize) {

    *returnSize = matrixSize;

    int *ans = (int *)malloc(matrixSize * sizeof(int));

    for (int i = 0; i < matrixSize; i++) {
        ans[i] = 0;

        for (int j = 0; j < matrixColSize[i]; j++) {
            ans[i] += matrix[i][j];
        }
    }

    return ans;
}