#!/bin/sh

src_directory="$HOME/lib/src"
log_file="$src_directory/git_pull.log"

# 判断目录是否存在
if [ -e "$src_directory" ];then
    eval cd $src_directory
else
    mkdir -p $src_directory && eval cd $src_directory
fi

# 是否存在日志文件
if [ ! -e "$log_file" ];then
  touch "$log_file"
fi

# 更新项目
echo "$(date  +"%Y-%m-%d %H:%M:%S")----[begin]所有项目将要开始更新！" >> "$log_file"

for project in `ls`
do
    project_dir="$src_directory/$project"

    if [ -d $project_dir ] && [ $project != ".git" ];then
        echo "$(date  +"%Y-%m-%d %H:%M:%S")----项目 $project 将更新." >> "$log_file"
        eval cd $project && git pull >> "$log_file" ;eval cd $src_directory
        #echo "$(date  +"%Y-%m-%d %H:%M:%S")----项目 $project 更新完成." >> "$log_file"
    fi
done

echo "$(date  +"%Y-%m-%d %H:%M:%S")----[finish]所有项目更新完成！" >> "$log_file"