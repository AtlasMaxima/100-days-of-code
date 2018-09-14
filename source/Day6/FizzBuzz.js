
function basic() {
  // print numbers from 1 to 100
  for (i = 1; i <= 100; i++) {
    // multiples of 3, print 'Fizz' and multiples of 5, print 'Buzz'
    multipleThree = i % 3
    multipleFive = i % 5
    if (multipleFive == 0 && multipleThree == 0){
      console.log('FizzBuzz')
    }
    else if (multipleThree == 0) {
      console.log('Fizz')

    }
    else if (multipleFive == 0) {
      console.log('Buzz')
    }
    else {
      console.log(i)
    }
  }
}

basic()

function shorter() {
  for(let i = 1; i<= 100; i++) {
    var fizz = i % 3 == 0, buzz = i % 5 == 0;
    console.log(fizz ? buzz ? "FizzBuzz" : "Fizz" : buzz ? "Buzz" : i);

  }
}

shorter()
