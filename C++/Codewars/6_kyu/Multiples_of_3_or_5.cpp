int solution(int number){
    int sum = 0;
    for (int i = 0; i < number; i++){
        if (i % 3 == 0 || i % 5 == 0) sum += i;
    }
    if (sum < 0) return 0;
    return sum;
}
