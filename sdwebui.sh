#!/bin/bash

#启用虚拟环境
eval "$(conda shell.bash hook)"
conda activate python3.10

#关闭占用7891端口进程
process=`lsof -t -i:7891`
if [ "${process}" != "" ]; then
    kill -9 ${process}
fi
#关闭占用7860端口进程
process=`lsof -t -i:7860`
if [ "${process}" != "" ]; then
    kill -9 ${process}
fi
#关闭占用7865端口进程
process=`lsof -t -i:7865`
if [ "${process}" != "" ]; then
    kill -9 ${process}
fi
#关闭占用7866端口进程
process=`lsof -t -i:7866`
if [ "${process}" != "" ]; then
    kill -9 ${process}
fi

#设置代理
cd ~/
rm nohup.out 2>/dev/null
rm nohup.log 2>/dev/null
nohup clash 1>nohup.out 2>nohup.log &
#文件浏览器
cd ~/.config/filebrowser/
rm nohup.out 2>/dev/null
rm nohup.log 2>/dev/null
nohup filebrowser -d filebrowser.db 1>nohup.out 2>nohup.log &
#webui
cd /data/deep/stable-diffusion-webui/
rm nohup.out 2>/dev/null
rm nohup.log 2>/dev/null
nohup ./start.sh 1>nohup.out 2>nohup.log &
#lora
cd /data/deep/lora-scripts/
rm nohup.out 2>/dev/null
rm nohup.log 2>/dev/null
nohup ./start.sh 1>nohup.out 2>nohup.log &
