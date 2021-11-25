# JCSS

> This project is *deprecated* and replaced by [JCSS (Rust)](https://github.com/PhotonQuantum/jcss-rs). The new version shares the same protocol with this one.
> 
> The docker image `photonquantum/jcss:latest` now points to the Rust version.
>
> If you want to use the Python version, pull with `photonquantum/jcss:legacy`.

JCSS stands for *jaccount captcha solver server*.

## Usage

``` shell script
$ docker-compose up -d
$ curl -F "image=@captcha.jpg" localhost:8000
{"status":"success","data":{"prediction":"gbmke","elapsed_time":40}}
```
