/* let n=5
let array = [];
if(n==0){
    console.log("Error")
}else{
for(let i=0; i<n; i++){
    array.push('_')
}

let middle = Math.floor(n/2)
 for(let j=0; j<n; j++){
    if(j>=0 && j<middle){
        array[j]='*'
        array[n-j-1]='*'
        if(j>0 && j<middle){
            array[j-1]='_'
            array[n-j]='_'     
        }
        if(j== middle){
            array[j]='*'
            array[j-1]='_'
            array[j+1]='_'
        }
}

    console.log(array)

 
}
} */