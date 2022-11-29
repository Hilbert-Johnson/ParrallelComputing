DATA=0
WORKER=5

cd serial
echo "begin serial sort test....."
python QuickSort.py $DATA
python MergeSort.py $DATA

echo ""
echo "begin parrallel sort test....."
cd ..
cd parrallel
python QuickSort.py $DATA $WORKER
python MergeSort.py $DATA $WORKER
cd ..