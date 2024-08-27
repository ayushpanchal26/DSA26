void nStarTriangle(int n) 
{
    // Write your code here.
    for(int i ; i<=2*n-1;i++){
        int stars = i;
        if(i>n) stars = 2*n-i;
        for(int j = 1;j<=stars;j++){
            cout<<'*';
        }
        cout<<endl;
    }
}

/*
link - Pattern10: https://bit.ly/3WZoytT
*/
