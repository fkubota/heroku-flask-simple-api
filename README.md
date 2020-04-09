ref: https://techacademy.jp/magazine/26403

## app
app name: heroku-flask-simple-api
url: https://heroku-flask-simple-api.herokuapp.com/
git: https://git.heroku.com/heroku-flask-simple-api.git

- check
	- curl(local): curl localhost:5002/myapi -d "arg01=hello_flask"
    - curl(web): curl https://heroku-flask-simple-api.herokuapp.com/myapi -d "arg01=hello_flask"

