# Sublime Backup Cron Plugin

A sublime plugin that will automatically save unsaved files in a folder within Desktop.
This works with Mac. Not tested with other OS.

This helps you to use Sublime as a working buffer without the anxiety of losing
information stored in the buffer.

## How to use?

Clone this repo and run the following command which will copy the plugin file to the
correct directory.

```bash
./copy_plugin_file.sh
```

Now, when you switch focus away from Sublime text, all files will be automatically
saved to `~/Desktop/SublimeBackup`.

If you open an existing file from a different folder, that file will be saved in
place. Only unnamed editors will be saved under `~/Desktop/SublimeBackup`.

If you backup `~/Desktop/SublimeBackup` using TimeMachine, you will automatically
version control your sublime buffers.

## References

The following plugins helped in learning how to write this plugin

* https://github.com/oakkitten/save_unnamed/blob/master/save_unnamed.py
* https://github.com/kilgore5/sublime-force-saver/blob/master/ForceSaver.py

