import React from 'react'
import ReactDOM from 'react-dom'


class student {
    constructor(name){
        this.name = name;
    }
    present(){
        return this.name + 'is present';
    }
}
var person;
person = new student ("Harry");
person.present();



ReactDOM.render(<student />, document.getElementById('root'));

