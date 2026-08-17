// Dsa question in javascript

let str1 = "direk"
let capital_str = str1.toUpperCase()
let length_str = str1.length
let ref = 2

const insertAt = (str, sub, pos) => `${str.slice(0, pos)}${sub}${str.slice(pos)}`;

for (let i = 1; i < length_str; i++) {
    x = str1.charAt(i)
    for (let j = 0; j < i; j++) {
        capital_str = insertAt(capital_str, x, ref)
        ref++;
    }
    ref = ref + 1
}

console.log(capital_str)
str3 = ""
// with less time complexity
for (let i = 0; i < length_str; i++) {
    let n1 = str1[i].toUpperCase()
    let n2 = str1[i].toLowerCase().repeat(i)
    str3 = str3 + n1
    str3 = str3 + n2
}
console.log(str3)