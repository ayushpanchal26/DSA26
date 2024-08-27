'''
Pattern5: https://bit.ly/3WXGSDD

Pattern6: https://bit.ly/3i06XDu
'''
void nNumberTriangle(int n) {
    // Write your code here.
    for(int i = 0 ; i<=n;i++){
        for(int j = 1 ; j<n-i+1;j++){
            cout<<j<<' ';

        }
        cout<<endl;
    }
}

def nNumberTriangle(n):
  for i in range(n+1):
    for j in range(n-i+1):
      print('* ',end='')
    print('')
