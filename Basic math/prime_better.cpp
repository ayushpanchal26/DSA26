#include<iostream>
using namespace std;

int main() {
	// Write your code here
	int count = 0;
	int n;
	cin>>n;
	
	for(int i=1;i*i<=n;i++){
		if(n%i==0){
			count++;
			if ((n/i)!=0){
				count++;
			}
		}
	}
	if (count==2) cout<<"true";
	else cout<<"false";
}
