sftp user_name@remote - server - name
password: *******

index = 0
INPUT = 5
while [ $index < $INPUT]
do
  touch
  remote_folder / "$index".txt
done

gzip remote_folder
cp remote_folder.gzip local_folder
exit

cd local_folder
gunzip remote_folder.gzip