**xkcd-wall** is a python script for Windows 7 that changes your wallpaper to a random [http://xkcd.com/](xkcd) comic daily.

Credits
=======
The xkcd API uses [the xkcd library](https://github.com/gtklocker/xkcd) by **Kostis "gtklocker" Karantias** licensed under the MIT license.

Wallpaper code is by [ AKM](http://gabbpuy.blogspot.gr/2007/02/set-windows-wallpaper-from-python.html).

Installing
==========
xkcd-wall is a script for Windows only tested under Windows 7.

 * Install [Python 2.7+](http://python.org/)
 * Install [PIL](http://www.pythonware.com/products/pil/) for your Python version.
 * Install [pywin32](http://sourceforge.net/projects/pywin32/)
 * [The xkcd library](https://github.com/gtklocker/xkcd) is included in this repository, so you won't have to install it.
 * Create a directory and clone the source code there. For me that was "C:\Users\dionyziz\Documents\xkcd-wall".
 * Open the Windows Task Scheduler. In the Start menu type "Task Scheduler"
 * Create a new task with the following settings:
   * Run only **when user is logged in**
   * Triggers: **Daily**
   * Actions: **Start program**
   * Program/script: **"C:\python27\python.exe"** (or your version of Python; include quotation marks)
   * Arguments: **"C:\Users\dionyziz\Documents\xkcd-wall\xkcd-wall-2.py"** (full path to your location of the script file; include quotation marks)
   * Start in: **C:\Users\dionyziz\Documents\xkcd-wall** (full path to your location of the script directory without quotes)
   * Stop the task if it runs longer than **1 hour**

You can test that it works by selecting the task, right clicking and picking **"Run"**. Alternatively, you can import Wallpaper.xml from the repository into the Windows Task Scheduler and modify the settings accordingly.

License
=======
xkcd-wall is licensed under the MIT license. See the file LICENSE for more information.
