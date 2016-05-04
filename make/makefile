DATE=`date +%Y-%m-%d`
rule1:
	for ((i=1;i<3;i++)); do echo $$i; done

test.txt: input.txt
	touch test.txt

date:
	echo $(DATE)

data/test.txt: data
	echo "touching data/test.txt"
	touch data/test.txt
data:
	echo "creating dir data"
	mkdir data
