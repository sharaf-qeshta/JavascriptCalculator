/*
    * Name: Sharaf Qeshta
    * ID: 120190644
*/



let output = document.getElementById('output');  // for getting the output element
let buttons = Array.from(document.getElementsByClassName('button'));  // for getting the array of buttons

/* i found a builtin function called eval that evaluate any mathematical expression */

buttons.map( button => { // map through all buttons (lambda)
    button.addEventListener('click', (e) => {
        switch(e.target.innerText){
            case 'C': // if the clicked button is C then it will clear the output element
                output.innerText = '';
                break;
            case '=': // if the user click on equal sign it will evaluate the given expression
                try{
                    output.innerText = eval(output.innerText);
                } catch { // if the expression have some error it will alert with error
                    alert("Error")
                }
                break;
            case '←': // if the user clicked on the back arrow it will delete the last character and so on
                if (output.innerText){  // check if the output screen have an element or its null
                   output.innerText = output.innerText.slice(0, -1);
                }
                break;
            default:
                output.innerText += e.target.innerText; // otherwise it will record the button that has been clicked
                                                         // in the expression to be evaluated
        }
    });
});
