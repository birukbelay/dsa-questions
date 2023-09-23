// https://leetcode.com/problems/counter-ii/submissions/
type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {
    let num=init;
    let origNum=init;
    return {
        increment:()=> { num++; return num},
        decrement:()=>--num,
        reset:()=> {
            num=origNum
            return num
        }
        
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */