# JCSS

JCSS stands for *jaccount captcha solver server*.

## Usage

``` shell script
$ docker-compose up -d
$ curl -F "image=@captcha.jpg" localhost:8000
{"status":"success","data":{"prediction":"gbmke","elapsed_time":40}}
```