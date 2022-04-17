docker run -it --cpus=4 -m 16G zyclonite/sysbench --test=cpu --cpu-max-prime=1000 --time=30 run
docker rm $(docker ps -a -q -f status=exited)
