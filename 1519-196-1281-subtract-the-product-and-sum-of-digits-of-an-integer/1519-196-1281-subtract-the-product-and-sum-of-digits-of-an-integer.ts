function subtractProductAndSum(n: number): number {
    let sum:number = 0;
    let product:number = 1;
    for (let i of String(n)) {
        sum += Number(i)
        product *= Number(i)
    };
    return product - sum;
};