// Meredith Reiner
// Final Project

var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var fs = require('fs')
var {PythonShell} = require('python-shell')

app.use(express.static(__dirname + '/public'));

io.on('connection', function(socket) {  

  var myImageName;
  
  console.log('user connected');

  socket.on('sendinputpic', function(data, name) {
    fs.writeFile("./public/images/"+name, data, (err) => {
      if (err == null) {
        console.log(name + " file saved");
        myImageName = name;
      }
      else{
        console.log(err);
      }
    });
    socket.emit('drawinputimage', name);
  });

  socket.on('process', function(colors, factor){
    if(myImageName != undefined){
      var colors_string = ""
      for(i in colors){
        colors_string = colors_string + colors[i] + ",";
      }
      colors_string = colors_string.slice(0,-1);
      console.log(colors_string);
      PythonShell.run('transform.py', {args: [myImageName, colors_string, factor]}).then(messages=>{
        console.log(messages);
        socket.emit('drawoutputimage', myImageName);
      });
    }
  });
  
  socket.on('disconnect', function() {
    console.log('user disconnected');
  });
});

// Setup port 3002 as our webserver
// --------------------------------
http.listen(3002, function() {
	console.log('Listening on #:3002');
});