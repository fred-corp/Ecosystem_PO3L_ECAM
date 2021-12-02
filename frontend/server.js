let express = require('express');
var bodyParser = require("body-parser");

let app = express();

var msg = "This website is not constructed yet ! \n It's supposed to pull the data from the GitHub repo every minute though";

app.set('view engine','ejs');
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static('public'));


app.get('/', function(request, response) {
    //response.send("Hello, world!");
    response.render('home.ejs', {validationMessage: msg});
});


app.listen(3000, function() {
    console.log('Server is running on port 3000');
});
