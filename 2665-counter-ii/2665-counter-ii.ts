type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

const createCounter = (init: number) : ReturnObj => {

    let inital_number:number = init
    let current_number:number = init
    const increment = ():number => {
        current_number++;
        return current_number
    }
    const decrement = ():number => {
        current_number--;
        return current_number
    }
    const reset = () :number => {
        current_number = inital_number  
        return current_number
    }
    return { increment, decrement, reset };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */