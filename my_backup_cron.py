import sublime
import sublime_plugin
import time
import os
import datetime
from pathlib import Path

HOME_DIR = str(Path.home())
BASE_BACKUP_DIR = f'{HOME_DIR}/Desktop/SublimeBackup'
os.makedirs(BASE_BACKUP_DIR, mode=0o755, exist_ok=True)

DATE_FORMAT = "%Y-%m-%d"
TIMESTAMP_FORMAT = f"{DATE_FORMAT}T%H:%M:%SZ"

USE_EPOCH_SECONDS_AS_FILE_NAME_PREFIX = False


def save_view(view):
    view.run_command("save")


def assign_filename_to_view(view, filename):
    # Retarget the view to save to the given file path
    view.retarget(filename)


i = 0
prev_time = 0


def generate_file_name():
    global i, prev_time

    if USE_EPOCH_SECONDS_AS_FILE_NAME_PREFIX:
        now = int(time.time())
    else:
        now = datetime.datetime.now().strftime(TIMESTAMP_FORMAT)

    if prev_time == now:
        i = i + 1
    prev_time = now

    return f"{now}-file-{i}.txt"


class BackupCronCommand(sublime_plugin.EventListener):
    def run(self, edit):
        pass

    # Entry point
    def on_deactivated(self, view):
        windows = sublime.windows()
        for w in windows:
            for v in w.views():
                if v.is_dirty():  # Backup all dirty views
                    if not v.file_name():
                        assign_filename_to_view(v, f"{BASE_BACKUP_DIR}/{generate_file_name()}")
                    save_view(v)
                else:
                    # Handle the case when sublime has a deleted file open
                    if v.file_name() and not os.path.isfile(v.file_name()):
                        assign_filename_to_view(v, f"{BASE_BACKUP_DIR}/{generate_file_name()}")
                        save_view(v)

