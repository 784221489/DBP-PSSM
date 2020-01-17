cd E:/python3/Lib/site-packages/libsvm-3.23/windows
mkdir tongji_all
for ccc in {0.0009765625,0.001953125,0.00390625,0.0078125,0.015625,0.03125,0.0625,0.125,0.25,0.5,1,2,4,8,16,32,64,128,256,512,1024}
do
for gamma in {0.0009765625,0.001953125,0.00390625,0.0078125,0.015625,0.03125,0.0625,0.125,0.25,0.5,1,2,4,8,16,32,64,128,256,512,1024}
do
mkdir rbf_PDB1075_${gamma}_${ccc}
for i in {1,2,3,4,5}
do
E:/python3/Lib/site-packages/libsvm-3.23/windows/svm-train.exe -b 1 -s 0 -t 2 -g $gamma -c $ccc E:/python3/Lib/site-packages/libsvm-3.23/windows/PDB1075/nofold${i}.txt rbf_PDB1075_${gamma}_${ccc}/no${i}.train.model
E:/python3/Lib/site-packages/libsvm-3.23/windows/svm-predict.exe  -b 1 E:/python3/Lib/site-packages/libsvm-3.23/windows/PDB1075/fold${i}.txt rbf_PDB1075_${gamma}_${ccc}/no${i}.train.model rbf_PDB1075_${gamma}_${ccc}/no${i}.train.model.out >>rbf_PDB1075_${gamma}_${ccc}/rbf_PDB1075_${gamma}_${ccc}.accuracy
done
cp rbf_PDB1075_${gamma}_${ccc}/rbf_PDB1075_${gamma}_${ccc}.accuracy tongji_all/

done
done
 