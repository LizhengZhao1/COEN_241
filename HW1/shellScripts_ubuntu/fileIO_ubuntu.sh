sysbench fileio --file-total-size=1G --file-test-mode=rndrw prepare
sysbench fileio --file-total-size=1G --file-test-mode=rndrw run 
sysbench fileio --file-total-size=1G --file-test-mode=rndrw cleanup 