numbersE = []
numbersO = []
let sumE = 0
let sumO = 0


for (i=0;i<=100;i++) {

    if(i % 2 == 0){
        numbersE.push(i)
     }

    else {
        numbersO.push(i)
        
    }
    
    sumE += numbersE[i]
    sumO += numbersO[i]
}

console.log(sumE, sumO)

Nan Nan