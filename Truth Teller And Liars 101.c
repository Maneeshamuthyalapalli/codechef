#include <stdio.h>
int min_people_to_ask(int N, int M) {
    if (N < M + 1) {
        return -1;
    }
    return 2 * M + 1;
}
int main() {
    int T; 
    scanf("%d", &T);
    while (T--) {
        int N, M;
        scanf("%d %d", &N, &M);
        printf("%d\n", min_people_to_ask(N, M));
    }
    
    return 0;
}


