// `let` allows you to declare variables that are limited in scope to the block.
if(true) {
  let age = 27;
}

// console.log(age); // have an error that age is not defined
let name = "Hilfiger";

// let allows you to define variables inside of the block stays inside of the block
if(true) {
  let name = "Tommy";
  console.log(name);
}
name = "New name";
console.log(name); // "New name"

// `const` cannot be changed , thus no new objects can be changed.
const OBJ = {
  age: 27
};

console.log(OBJ); // age: 27
// the value will be changed but the object is still the same
OBJ.age = 100;
console.log(OBJ); // age: 100
