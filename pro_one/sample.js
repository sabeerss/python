elAdd = document.getElementById('add');
elCallOther = document.getElementById('callOther');
console.log(elAdd);
console.log(elCallOther);
elAdd.addEventListener("click", addOption);
elCallOther.addEventListener("click", callOther);

eltxt = document.getElementById('txt');
eltxt.addEventListener ("keypress", function(event) {
    console.log(txt.value);
});

function addOption(name)
{
    var sampleJson = '{ "1": "one", "2": "two", "3": "three", "4": "four"}';
    
    var jsObject = JSON.parse(sampleJson);

    //var jsObject = { 1: "one", 2: "two", 3: "three", 4: "four"};

    for (var i in jsObject) {
        $('#drp').append(`<option value='${i}'>  ${jsObject[i]} </option>`);    
    };
    
}
