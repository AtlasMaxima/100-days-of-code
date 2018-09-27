/*Default Binding*/
function display() {
  console.log(this); // referring to the window or global object
}

// display();

/*Implicit Binding*/
var person = {
  name: 'Sarah',
  display: function() {
    console.log(this.name); // `this` will point to the person object
  }
};

var name = "uh oh ! Global Object";
console.log(person.name) // Sarah
person.display(); // Sarah

/*Explicit Binding*/
var person2 = {
  name: 'AllyHills'
}

person.display = person.display.bind(person2);
var outer = person.display;
outer();
