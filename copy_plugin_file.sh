#!/bin/bash

if [[ $(uname) != "Darwin" ]]
then
    echo "This script is tested to work in Mac. Since this is not Mac, exiting early"
    exit 1
fi

HOME_DIR=$(echo "echo ~" | bash)

# https://stackoverflow.com/questions/7808452/what-is-the-full-path-to-the-packages-folder-for-sublime-text-2-on-mac-os-lion
SUBLIME_3_PLUGIN_PATH="${HOME_DIR}/Library/Application Support/Sublime Text 3/Packages/User/"
SUBLIME_4_PLUGIN_PATH="${HOME_DIR}/Library/Application Support/Sublime Text/Packages/User/"

SUBLIME_PLUGIN_PATHS=(
    "${SUBLIME_3_PLUGIN_PATH}"
    "${SUBLIME_4_PLUGIN_PATH}"
)


for plugin_path in "${SUBLIME_PLUGIN_PATHS[@]}"
do
    if [[ -d "${plugin_path}" ]]
    then
        cp my_backup_cron.py "${plugin_path}"
        echo "Plugin file copied to ${plugin_path}"
    fi
done

