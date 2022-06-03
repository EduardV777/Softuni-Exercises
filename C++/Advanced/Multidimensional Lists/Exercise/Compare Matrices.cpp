#include <iostream>
#include <string>
#include <climits>
using namespace std;

void ShowArray(int** arr, int r, int c) {
    for (signed int k = 0; k < r; k++) {
        for (signed int j = 0; j < c; j++) {
            cout << arr[k][j] << " ";
        }
        cout << endl;
    }
}

int GetRowLength(string valuesRow) {
    int i = 0;
    string nums = "";
    for (int k = 0; k <= valuesRow.length(); k++) {
        if (k == valuesRow.length() || valuesRow[k] == ' ') {
            i++;
        }
    }
    return i;
}


bool CompareArrays(int** array1, int** array2, int r, int c) {
    bool sameArrays = true;
    for (signed int k = 0; k < r; k++) {
        for (signed int j = 0; j < c; j++) {
            if (array1[k][j] != array2[k][j]) {
                sameArrays = false;
                break;
            }
        }
    }
    return sameArrays;
}


int main() {
    int** arr1 = new int* [1]; int** arr2 = new int* [1];
    int count = 0, rowsCount = INT_MIN, rowsLength = INT_MIN;
    while (count <= 1) {
        int rows, r = 0;
        cin >> rows;
        if (count == 0) {
            arr1 = new int* [rows];
        }
        else {
            arr2 = new int* [rows];
        }
        if (rowsCount == INT_MIN) {
            rowsCount = rows;
        }

        while (r < rows) {
            string values, curr = "";
            getline(cin >> ws, values);

            if (rowsLength == INT_MIN) {
                rowsLength = GetRowLength(values);
            }

            if (count == 0) {
                arr1[r] = new int[rowsLength];
            }
            else {
                arr2[r] = new int[rowsLength];
            }

            for (signed int k = 0, i = 0, l = 0; k <= values.length(); k++) {
                if (k == values.length() || values[k] == ' ') {
                    if (count == 0) {
                        arr1[r][i] = stoi(curr);
                    }
                    else {
                        arr2[r][i] = stoi(curr);
                    }
                    i++, l++;
                    curr = "";
                }
                else {
                    curr += values[k];
                }
            }
            r++;
        }
        count++;
    }
    // cout << endl;
    //ShowArray(arr1, rowsCount, rowsLength);

    if (CompareArrays(arr1, arr2, rowsCount, rowsLength)) {
        cout << "equal";
    }
    else {
        cout << "not equal";
    }
    return 0;
}