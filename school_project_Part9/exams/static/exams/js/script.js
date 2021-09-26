// Fetch csrf token from browser cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


// Get the required elements from the DOM
const button1 = document.getElementById('fetchdata1');
const input1 = document.getElementById('text');


// On typing... send async request to the server.
input1.addEventListener('keyup', function(){
    const text = input1.value;

    // Define some data
    const data = {
        "text": text,
    }

    // Convert to json
    const json_data = JSON.stringify(data)

    // Build the request object
    const payload = {
        method: "post",
        body: json_data
    }

    // Define the address to call
    const url = 'asyncdemo/';
    
    // Async request to Url, sending Payload
    fetch(url, payload)                                     // Make async call to the server
    .then(response => response.json())                      // When it gets back THEN convert the JSON  (JSON is streamed. So its also async)
    .then(data => console.log(data['uppertext']))           // When you finish converting the JSON to DATA THEN console lot it.
});


// On click... send async request to the server.
button1.addEventListener('click', function(){
    const text = input1.value;

    // Define some data
    const data = {
        "text": text,
    }

    // Convert to json
    const json_data = JSON.stringify(data)

    // Build the request object
    const payload = {
        method: "post",
        body: json_data
    }

    // Define the address to call
    const url = 'asyncadduser/';
    const request = new Request(url, {headers: {'X-CSRFToken': getCookie('csrftoken')}});

    // Async request to Url, sending Payload
    fetch(request, payload)                         // Make async call to the server
    .then(response => response.json())              // When it gets back THEN convert the JSON  (JSON is streamed. So its also async)
    .then(data => {                                 // When you finish converting the JSON to DATA THEN console lot it.
        if (data['status'] == "success"){
            console.log(data['message'])
        }
        else{
            alert(data['message'])
        }
    })         
});
