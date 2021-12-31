#include <stdio.h>
#define N 10
void inputarray(int *arr);
void handlearray(int *arr);
void outputarray(int *arr);
void swap(int *p,int *q);
int main()
{
    int array[N]= {0};
    inputarray(array);
    handlearray(array);
    outputarray(array);
    return 0;
}
void swap(int *p,int *q)
{
    int temp=*p;
    *p=*q;
    *q=temp;
}
void handlearray(int *arr)
{
    int *p=arr;
    int min_index=0;    // the index of the minimum number 
    int min=arr[0]; // the minimum number
    for(int i=1;i<N;i++)
    {
        if(*(p+i)<min)
        {
            min=*(p+i);
            min_index=i;
        }

    }
    swap((p+min_index),(p+0));
    int max_index=0;    // the index of the maximum number 
    int max=arr[0]; // the maxinum number
    for(int i=1;i<N;i++)
    {
        if(*(p+i)>max)
        {
            max=*(p+i);
            max_index=i;
        }
    }
    swap((p+max_index),(p+9));
}
void inputarray(int *arr)
{
    int *p=arr;
    for(int i=0; i<N; i++)
    {
        scanf("%d",(p+i));
    }
}
void outputarray(int *arr)
{
    int *p=arr;
    for(int i=0; i<N; i++)
    {
        printf("%d ",*(p+i));
    }
}