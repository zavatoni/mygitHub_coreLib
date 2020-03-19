#!/bin/bash
#########################################
## Linux系统LVM逻辑卷创建过程以及自动化脚本
## email: 15012750830@163.com
## 邵喆桢
## centos 6
#########################################

echo "请输入一个英文目录:"
read partition           # 定义最终挂载的名称

if [ -e $partition ]
then
    echo "file exists $partition"
else
    echo "file not exist $partition"
fi

if [ -d $partition ]
then
    echo "directory exists $partition"
else
    echo "auto created directory $partition"
    /bin/mkdir -p $partition
fi

vgname=vgSzz                      # 定义逻辑卷组的名称
lvname=lvmSzz                     # 定义逻辑卷的名称
code='b c d e f g h i k j l'      # 根据分区的实际情况修改
disk=

for i in $code
do
if [ -b /dev/sd$i ]
then
echo "Existing device files /dev/sd$i/"
sudo fdisk /dev/sd$i << EOF          # 这里自动化完成了所有分区fdisk苦逼的交互步骤
n
p
1
1

t
8e
w
EOF
disk="$disk /dev/sd${i}1" # 将所有分区拼起来
else
echo "Found /dev/sd$i/"
fi
done

/sbin/pvcreate $disk
/sbin/vgcreate $vgname $disk
/sbin/lvcreate -l 100%VG -n $lvmname $vgname
/sbin/mkfs.ext4 /dev/$vgname/$lvmname
/bin/mount -a
/bin/df -h
