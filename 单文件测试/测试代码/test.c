#include <stdio.h>
int main()
{
    void inv(int *x, int n);
    int i, a[10];
    for (i = 0; i < 10; i++)
        scanf_s("%d", &a[i]);
    //printf("\n");
    inv(a, 10);
    //printf("The array has been inverted:\n");
    for (i = 0; i < 10; i++)
        printf("%d ", a[i]);
    //printf("\n");
    return 0;
}

void inv(int *x, int n)
{
    int *i, max, min, p, q, *c, *d;
    max = *x;
    min = *(x + 1);
    c = x + 0;
    d = x + 1;
    for (i = x; i < x + 10; i++)
        if (*i > max)
        {
            max = *i;
            c = i;
        }
    for (i = x; i < x + 10; i++)
        if (*i < min)
        {
            min = *i;
            d = i;
        }
    p = *x;
    *x = *d;
    *d = p;
    q = *(x + 9);
    *(x + 9) = *c;
    *c = q;
}