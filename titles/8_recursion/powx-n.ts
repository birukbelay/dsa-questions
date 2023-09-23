function myPow(x: number, n: number): number {
    return xpow(x, n, x, Math.abs(n))
};

function xpow(x:number, n: number, tot:number, ctrN:number):number{
    if (n==0) return 1
    if (ctrN==1){
        if(n<0) return 1/tot
        return tot
    }
    if (ctrN%2==0) return xpow(x*x, n, tot*x, ctrN/2)
    return xpow(x, n, tot*x, ctrN-1)
    
}
console.log(myPow(2, 10))