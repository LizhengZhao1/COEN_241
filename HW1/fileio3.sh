docker run --rm -it --cpus=1 -m 16G --entrypoint /bin/sh zyclonite/sysbench 
sysbench fileio --file-total-size=1G --file-test-mode=rndrw prepare
sysbench fileio --file-total-size=1G --file-test-mode=rndrw run 
sysbench fileio --file-total-size=1G --file-test-mode=rndrw cleanup 

