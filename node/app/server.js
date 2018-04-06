var express = require('express');
var request = require('sync-request');
var app = express();
var body_parser = require('body-parser');
 
app.use(body_parser());


app.set('view engine', 'pug');
app.set('views', __dirname + '/views');
app.use(express.static('node_modules'));


app.get('/api', function (req, res) {
  res.render('index', { data: '' });
});

app.get('/api/page', function (req, res) {
  var params = ''
  for(key in req.query){
    params = params + key + '=' + encodeURIComponent(req.query[key]) + '&'
  }
  console.log(params)
  var url = 'http://api:8000/api/page';
  var pages = request('GET', url + '?' + params).getBody(); 
  res.render('index', { data: pages });
});

app.post('/api/page', function (req, res) {
  var url = 'http://api:8000/api/page';
  var params = {
    json: {
      'title': req.body.title,
      'url': req.body.url,
      'site': req.body.site,
      'type': req.body.type
    }
  };
  pages = request('POST', url, params).getBody();
  res.render('index', { data: pages });
});

app.get('/api/page/new', function (req, res) {
  var url = 'http://api:8000/api/page/new';
  var pages = request('GET', url).getBody();
  res.render('index', { data: pages });
});

app.post('/api/page/new', function (req, res) {
  var url = 'http://api:8000/api/page/new';
  pages = request('POST', url).getBody();
  res.render('index', { data: pages });
});

app.get('/api/tag', function (req, res) {
  var url = 'http://api:8000/api/tag';
  var pages = request('GET', url).getBody();
  res.render('index', { data: pages });
});

app.post('/api/tag', function (req, res) {
  var url = 'http://api:8000/api/tag';
  var params = {
    json: {
      'name': req.body.name,
      'description': req.body.description
    }
  };
  pages = request('POST', url, params).getBody();
  res.render('index', { data: pages });
});

app.listen(8081);
