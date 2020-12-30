//BIG O notation
const data = ['A','B','C']
const data2 = [1,2,3,4,5]
for(let i = 0; i<data.length; i++){
    console.log(data[i])
}
//Here, time complexity is O(n),it scales linerally

const data = ['A','B','C']
const data2 = [1,2,3,4,5]
for(let j = 0; j< data2.length; j++){
    console.log(data2[j])
}
for(let i = 0; i<data.length; i++){
    console.log(data[i])
}
//here, time complexity is O(n+a), n is length of data array,
//a is length of data2 array
const data = ['A','B','C']
const data2 = [1,2,3,4,5]
for(let i = 0; i<data.length; i++){
for(let i = 0; i<data.length; i++){
    console.log(data[i]+ data2[j])
}
}
//Here, the time complexity if O(n * a)
const data = ['A','B','C']
//if only one data array
for(let i = 0; i<data.length; i++){
    for(let i = 0; i<data.length; i++){
        console.log(data[i]+ data[j])
    }
    }
// Here,the time complexity is O(n^2).

const data = ['A','B','C']
//if only one data array
for(let i = 0; i<data.length; i++){
    for(let i = 0; i<data.length; i++){
        console.log(data[i]+ data[j])
        console.log(data[i]+ data[j])
        console.log(data[i]+ data[j])
        console.log(data[i]+ data[j])
    }
    }

//Here, time complexity if O(4n^2), but we can remove the 
// 4 as it is a  dominant term.

const data = ['A','B','C']
//if only one data array
for(let i = 0; i<data.length; i++){
    for(let i = 0; i<data.length; i++){
        console.log(data[i]+ data[j])
    }
}
for(let i = 0; i<data.length; i++){
    console.log(data[i])
}
//O(n^2+ n), but we remove the value that is less than n^2, so, 
//the time complexity is O(n^2 + n

//SPACE COMPLEXITY
const data = ['A','B','C']
for(let i = 0; i<data.length; i++){
    console.log(data[i])
}
//The space complexity is O(1)


