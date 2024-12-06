#!/usr/bin/env bash

gblcmd_fe_watch(){
    cd fe
    npm run dev
}
gblcmd_fe_install(){
    local fe_path=$(git rev-parse --show-toplevel)/fe
    pushd "$fe_path" > /dev/null
    npm install
    popd > /dev/null
}

gblcmd_fe_build(){
    local fe_path=$(git rev-parse --show-toplevel)/fe
    pushd "$fe_path" > /dev/null
    npm run build 
    popd > /dev/null
}