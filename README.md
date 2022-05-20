# README

#### Build

```
docker build -t anthony -f .\.docker\Dockerfile . 
```

#### Run

```
docker run --rm --shm-size=2g anthony anthony --help
```