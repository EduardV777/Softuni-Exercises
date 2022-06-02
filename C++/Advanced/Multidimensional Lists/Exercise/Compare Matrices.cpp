#include <iostream>
#include <string>
#include <climits>
using namespace std;

void ShowArray(int** arr, int r, int c){
    for(int k=0;k<r;k++){
        for(int j=0;j<c;j++){
            cout<<arr[k][j]<<" ";
        }
        cout<<endl;
    }
}

int main() {
    int** arr1; int** arr2;
    int count=0, rowLength=INT_MIN, rowCount=INT_MIN;
    while(count<=1){
        int rows=0, r=0;
        cin>>rows;
        while(r<rows){
            string values, curr="";
            getline(cin>>ws, values);
            if(rowLength==INT_MIN){
                rowLength=values.length()/2;
            }
            if(rowCount==INT_MIN){
                rowCount=rows;
            }

            if(count){
                arr1[r]=new int [rowLength];
            }else {
                arr2[r]=new int [rowLength];
            }
            for(int j=0, i=0;j<=values.length();j++){
                if(j==values.length() || values[j]==' '){
                    if(count==0){
                        arr1[r][i]=stoi(curr);
                    }else {
                        arr2[r][i]=stoi(curr);
                    }
                    curr="";
                    i++;
                }else {
                    curr+=values[j];
                }
            }
            r++;
        }
        count++;
    }

    ShowArray(arr1, rowCount, rowLength);
    return 0;
}