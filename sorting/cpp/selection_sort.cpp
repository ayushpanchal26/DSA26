// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;
void selection(int arr[], int n){
    for(int i = 0  ; i<n-1;i++){
        int mini = i;
        for (int j = i+1 ;j<n;j++){
            if (arr[j]< arr[mini]){
                mini = j;
                
            }
        // swap
        int temp = arr[mini];
        arr[mini] = arr[i];
        arr[i]= temp;
        }
    }
    for (int i = 0;i<=n;i++){
        cout<<arr[i]<<" ";
    }
}
int main() {
    // Write C++ code here
    int arr[] = {13,46,24,52,20,9};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    for (int i = 0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    selection(arr,n);
    return 0;
}
