var person = {
  firstName: 'Ally',
  lastName : 'Hills',
   getFullName : function() {
    return person.firstName + " " + person.lastName;
  }
};

var fullName = person.getFullName();
console.log(fullName);

var person2 = person;
person = {}
console.log(person2.getFullName());

/* the object Person can change later in the code, in order to refer to the
properties of the specific object, we use 'this' key word.*/

var obj = {method: () => this};
console.log(obj);
console.log(obj.method());
