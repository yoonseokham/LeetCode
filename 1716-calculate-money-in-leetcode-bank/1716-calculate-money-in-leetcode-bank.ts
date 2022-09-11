function totalMoney(n: number): number {
    let answer:number = 0
    let pre_monday_saved_money:number = 0
    for (let i = 0;i < n;i++) {
        if (i%7===0) {
            pre_monday_saved_money ++ 
        }
        answer += i%7 +pre_monday_saved_money
    }
    return answer
};