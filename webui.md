### 1.配置环境

##### 1.1.配置~/.bashrc
```
vim ~/.bashrc
alias ll='ls -l'
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH

#export https_proxy="http://127.0.0.1:7890"
#export http_proxy="http://127.0.0.1:7890"
#export all_proxy="socks5://127.0.0.1:7891"
#export no_proxy="localhost,127.0.0.1,::1"
```

##### 1.2.配置~/.profile

```
vim ~/.profile
export TORCH_HOME=/data/cache/torch
export HUGGINGFACE_HUB_CACHE=/data/cache/huggingface
export MODELSCOPE_CACHE=/data/cache/modelscope
```

##### 1.3.配置Ubuntu软件仓库镜像

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释

# Ubuntu20.04清华源
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse

deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse

deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse

deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse
# # deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-proposed main restricted universe multiverse

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Ubuntu20.04阿里源
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
# deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
# deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
# deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
# deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
# # deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# Ubuntu20.04腾讯源
deb http://mirrors.tencentyun.com/ubuntu/ focal main restricted universe multiverse
# deb-src http://mirrors.tencentyun.com/ubuntu/ focal main restricted universe multiverse

deb http://mirrors.tencentyun.com/ubuntu/ focal-updates main restricted universe multiverse
# deb-src http://mirrors.tencentyun.com/ubuntu/ focal-updates main restricted universe multiverse

deb http://mirrors.tencentyun.com/ubuntu/ focal-backports main restricted universe multiverse
# deb-src http://mirrors.tencentyun.com/ubuntu/ focal-backports main restricted universe multiverse

deb http://mirrors.tencentyun.com/ubuntu/ focal-security main restricted universe multiverse
# deb-src http://mirrors.tencentyun.com/ubuntu/ focal-security main restricted universe multiverse

# 预发布软件源，不建议启用
# deb http://mirrors.tencentyun.com/ubuntu/ focal-proposed main restricted universe multiverse
# # deb-src http://mirrors.tencentyun.com/ubuntu/ focal-proposed main restricted universe multiverse
```

##### 1.4.配置Pypi镜像

```
python3 -m pip install --upgrade pip
#清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
#阿里源
pip config set global.extra-index-url https://mirrors.aliyun.com/pypi/simple
#腾讯源
pip config set global.extra-index-url https://mirrors.cloud.tencent.com/pypi/simple 
```

##### 1.5.配置anaconda

```
https://www.anaconda.com/download#downloads
curl -O https://repo.anaconda.com/archive/Anaconda3-2023.07-1-Linux-x86_64.sh

#安装
bash Anaconda3-2023.07-1-Linux-x86_64.sh

#常用命令
conda --version
conda env list
conda create --name python3.10 python=3.10.10
conda activate python3.10

#删除环境
conda remove --name env_name --all
#删除环境中的某个包
conda remove --name $env_name $package_name

#设置国内镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
#恢复默认镜像
conda config --remove-key channels
```

##### 1.6.配置git-lfs

```
#安装
sudo apt install git-lfs
#初始化
git lfs install
#测试
#GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/CompVis/stable-diffusion-v1-5
```

### 2.配置clash

##### 2.1.下载安装clash

```
https://github.com/Dreamacro/clash/releases/tag/v1.17.0
curl -O https://github.com/Dreamacro/clash/releases/download/v1.17.0/clash-linux-amd64-v1.17.0.gz
#解压gz文件
gunzip clash-linux-amd64-v1.17.0.gz
#移动到/usr/local/bin目录
sudo mv clash-linux-amd64-v1.17.0 /usr/local/bin/clash
sudo chmod 755 /usr/local/bin/clash
```

##### 2.2.配置clash，路径~/.config/clash/config.yaml

```
port: 7890
socks-port: 7891
allow-lan: true
mode: Rule
log-level: info
external-controller: '127.0.0.1:9090'
dns:
  enabled: true
  nameserver:
    - 119.29.29.29
    - 223.5.5.5
  fallback:
    - 8.8.8.8
    - 8.8.4.4
    - tls://1.0.0.1:853
    - tls://dns.google:853
proxies:
    - {name: 代理, server: 114.114.114.114, port: 12345, client-fingerprint: chrome, type: vmess, uuid: 465dec1a-e09b-4bb6-9905-70f75d6035c8, alterId: 64, cipher: auto, tls: false, tfo: false, skip-cert-verify: false}
proxy-groups:
  - name: PROXY
    type: select
    proxies:
      - 代理
rules:
  - DOMAIN-SUFFIX,google.com,PROXY
  - DOMAIN-KEYWORD,google,PROXY
  - DOMAIN,google.com,PROXY
  - DOMAIN-SUFFIX,github.com,PROXY
  - DOMAIN-KEYWORD,github,PROXY
  - DOMAIN,github.com,PROXY
  - DOMAIN-SUFFIX,civitai.com,PROXY
  - DOMAIN-KEYWORD,civitai,PROXY
  - DOMAIN,civitai.com,PROXY
  - GEOIP,CN,DIRECT
  - MATCH,PROXY
```

##### 2.3.启动clash

```
nohup clash 1>nohup.out 2>nohup.log &
```

##### 2.4.配置git代理

```
git config --global http.proxy socks5://127.0.0.1:7891
git config --global --unset http.proxy
```

##### 2.5.配置终端全局代理

```
export https_proxy="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
export all_proxy="socks5://127.0.0.1:7891"
export no_proxy="localhost,127.0.0.1,::1"
unset https_proxy
unset http_proxy
unset all_proxy
unset no_proxy
```

##### 2.6.查看端口占用

```
lsof -i:7891
```

### 3.配置webui

##### 3.1.从github下载

```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

##### 3.2.修改webui.sh，不启用venv

```
if [[ $use_venv -eq 1 ]] && ! "${python_cmd}" -c "import venv" &>/dev/null
#改为
if [[ $use_venv -eq 1 ]] && ! "${python_cmd}" -c "import sys" &>/dev/null

#删除194行到219行
if [[ $use_venv -eq 1 ]] && [[ -z "${VIRTUAL_ENV}" ]];
then
    printf "\n%s\n" "${delimiter}"
    printf "Create and activate python venv"
    printf "\n%s\n" "${delimiter}"
    cd "${install_dir}"/"${clone_dir}"/ || { printf "\e[1m\e[31mERROR: Can't cd to %s/%s/, aborting...\e[0m" "${install_dir}" "${clone_dir}"; exit 1; }
    if [[ ! -d "${venv_dir}" ]]
    then
        "${python_cmd}" -m venv "${venv_dir}"
        first_launch=1
    fi
    # shellcheck source=/dev/null
    if [[ -f "${venv_dir}"/bin/activate ]]
    then
        source "${venv_dir}"/bin/activate
    else
        printf "\n%s\n" "${delimiter}"
        printf "\e[1m\e[31mERROR: Cannot activate python venv, aborting...\e[0m"
        printf "\n%s\n" "${delimiter}"
        exit 1
    fi
else
    printf "\n%s\n" "${delimiter}"
    printf "python venv already activate or run without venv: ${VIRTUAL_ENV}"
    printf "\n%s\n" "${delimiter}"
fi
```

##### 3.3.安装TCMalloc

```
sudo apt install google-perftools
```

##### 3.4.单独安装torch（不是必须的，modules/launch_utils.py）

```
#可能安装不成功（下载到本地安装比较稳妥）
pip install torch==2.0.1 torchvision==0.15.2 --extra-index-url https://download.pytorch.org/whl/cu118
#下载二进制包安装torch
curl -O https://download.pytorch.org/whl/cu118/torch-2.0.1%2Bcu118-cp310-cp310-linux_x86_64.whl
pip install torch-2.0.1%2Bcu118-cp310-cp310-linux_x86_64.whl
#下载二进制包安装torchvision
curl -O https://download.pytorch.org/whl/cu118/torchvision-0.15.2%2Bcu118-cp310-cp310-linux_x86_64.whl
pip install torchvision-0.15.2%2Bcu118-cp310-cp310-linux_x86_64.whl
```

##### 3.5.从指定的zip包安装依赖（modules/launch_utils.py）

```
#GFPGAN
curl -O https://github.com/TencentARC/GFPGAN/archive/8d2447a2d918f8eba5a4a01463fd48e45126a379.zip
#或者
curl -O https://ghproxy.com/https://github.com/TencentARC/GFPGAN/archive/8d2447a2d918f8eba5a4a01463fd48e45126a379.zip

#CLIP
curl -O https://github.com/openai/CLIP/archive/d50d76daa670286dd6cacf3bcd80b5e4823fc8e1.zip
#或者
curl -O https://ghproxy.com/https://github.com/openai/CLIP/archive/d50d76daa670286dd6cacf3bcd80b5e4823fc8e1.zip

#OPENCLIP
curl -O https://github.com/mlfoundations/open_clip/archive/bb6e834e9c70d9c27d0dc3ecedeebeaeb1ffad6b.zip
#或者
curl -O https://ghproxy.com/https://github.com/mlfoundations/open_clip/archive/bb6e834e9c70d9c27d0dc3ecedeebeaeb1ffad6b.zip

#本地安装
python3 -m pip install 8d2447a2d918f8eba5a4a01463fd48e45126a379.zip --prefer-binary --use-pep517
python3 -m pip install d50d76daa670286dd6cacf3bcd80b5e4823fc8e1.zip --prefer-binary
python3 -m pip install bb6e834e9c70d9c27d0dc3ecedeebeaeb1ffad6b.zip --prefer-binary
```

##### 3.6.启动webui

```
#直接启动
bash webui.sh --listen --xformers --enable-insecure-extension-access --gradio-auth "apple:apple"
#设置代理
https_proxy="http://127.0.0.1:7890" http_proxy="http://127.0.0.1:7890" all_proxy="socks5://127.0.0.1:7891" no_proxy="localhost,127.0.0.1,::1" bash webui.sh --listen --xformers --enable-insecure-extension-access --gradio-auth "apple:apple" --api --api-log --api-auth "apple:apple"
```

### 4.配置lora-scripts

##### 4.1.下载lora-scripts

```
git clone --recurse-submodules https://github.com/Akegarasu/lora-scripts
```

##### 4.2.编辑train.sh

```
pretrained_model="./sd-models/model.ckpt" # base model path | 底模路径
is_v2_model=0                 # SD2.0 model | SD2.0模型 2.0模型下 clip_skip 默认无效
parameterization=0            # parameterization | 参数化 本参数需要和 V2 参数同步使用 实验性功能
train_data_dir="./train/aki"  # train dataset path | 训练数据集路径（在这个目录下需要再新建目录，比如10_aki，将训练数据放入）
reg_data_dir=""               # directory for regularization images | 正则化数据集路径，默认不使用正则化图像。

#线程数需要修改：--num_cpu_threads_per_process=8
#将每个进程的CPU线程数改为2：--num_cpu_threads_per_process=2
````

##### 4.3.安装依赖

```
#高版本open-clip-torch可能会冲突，降为2.6.1
pip install open-clip-torch==2.6.1
#安装依赖
pip install --upgrade -r requirements.txt
pip install --upgrade lion-pytorch lycoris-lora dadaptation prodigyopt fastapi uvicorn wandb
```

##### 4.4.启动gui

```
bash run_gui.sh --dev --host=0.0.0.0 --port=7865 --tensorboard-host=0.0.0.0 --tensorboard-port=6006
```

##### 4.5.终端执行训练

```
bash train.sh
```

### 5.配置filebrowser

##### 5.1.下载配置filebrowser

```
https://github.com/filebrowser/filebrowser/releases/tag/v2.23.0
curl -O https://github.com/filebrowser/filebrowser/releases/download/v2.23.0/linux-amd64-filebrowser.tar.gz
```

##### 5.2.安装filebrowser

```
#创建目录并解压
mkdir linux-amd64-filebrowser
tar -xzvf linux-amd64-filebrowser.tar.gz -C linux-amd64-filebrowser
#移动到/usr/local/bin目录
sudo mv ./linux-amd64-filebrowser/filebrowser /usr/local/bin/filebrowser
sudo chmod 755 /usr/local/bin/filebrowser
```

##### 5.3.配置config.json

```
mkdir -p ~/.config/filebrowser
cd ~/.config/filebrowser
#创建config.json
#必须使用绝对路径
{
    "address":"0.0.0.0",
    "port":7866,
    "database":"/home/ubuntu/.config/filebrowser/filebrowser.db",
    "log":"/home/ubuntu/.config/filebrowser/filebrowser.log",
    "root":"/data/deep",
    "username":"admin"
}

#常规运行
filebrowser -c config.json
#保持在后台运行
nohup filebrowser -c config.json &
```

##### 5.4.配置数据库

```
cd ~/.config/filebrowser
#创建配置数据库
filebrowser -d filebrowser.db config init
#设置监听地址
filebrowser -d filebrowser.db config set --address 0.0.0.0
#设置监听端口
filebrowser -d filebrowser.db config set --port 7866
#设置语言环境
filebrowser -d filebrowser.db config set --locale zh-cn
#设置日志位置
filebrowser -d filebrowser.db config set --log ~/.config/filebrowser/filebrowser.log
#添加一个用户
filebrowser -d filebrowser.db users add apple apple --perm.admin
#启动filebrowser
filebrowser -d filebrowser.db
#保持在后台运行
nohup filebrowser -d filebrowser.db 1>nohup.out 2>nohup.log &
```

### 6.注意事项

##### 6.1.Could not load dynamic library 'libnvinfer.so.7'

```
#教程
https://blog.csdn.net/sinat_20174131/article/details/130164234
#不同之处，动态链接库so可能不在tensorrt目录。而是在tensorrt_libs目录
~/anaconda3/envs/python3.10/lib/python3.10/site-packages/tensorrt
~/anaconda3/envs/python3.10/lib/python3.10/site-packages/tensorrt_libs

#创建软连接
sudo ln -s libnvinfer.so.8 libnvinfer.so.7
sudo ln -s libnvinfer_plugin.so.8 libnvinfer_plugin.so.7
#设置动态链接库路径
vim ~/.bashrc
export LD_LIBRARY_PATH=~/anaconda3/envs/python3.10/lib/python3.10/site-packages/tensorrt_libs:$LD_LIBRARY_PATH
```

##### 6.2.Error /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.34’ not found

```
#教程
https://blog.csdn.net/huazhang_001/article/details/128828999

#查看libc.so.6版本
strings /lib/x86_64-linux-gnu/libc.so.6 | grep GLIBC_

#编辑源/etc/apt/sources.list
sudo vi /etc/apt/sources.list
#添加高版本的源
deb http://cn.archive.ubuntu.com/ubuntu jammy main #添加该行到文件

#升级libc.so.6
sudo apt update
sudo apt install libc6
```

