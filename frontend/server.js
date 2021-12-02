let express = require('express');
var bodyParser = require("body-parser");

let app = express();

app.set('view engine','ejs');
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static('public'));


app.get('/', function(request, response) {
    //response.send("Hello, world!");
    response.render('home.ejs', {validationMessage: "This website is not constructed yet !"});
});


app.listen(3000, function() {
    console.log('Server is running on port 3000');
});
