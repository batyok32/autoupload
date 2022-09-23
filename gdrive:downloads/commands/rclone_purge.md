---
date: 2022-09-23T22:05:46+05:00
title: "rclone purge"
slug: rclone_purge
url: /commands/rclone_purge/
---
## rclone purge

Remove the path and all of its contents.

### Synopsis


Remove the path and all of its contents.  Note that this does not obey
include/exclude filters - everything will be removed.  Use `delete` if
you want to selectively delete files.


```
rclone purge remote:path [flags]
```

### Options

```
  -h, --help   help for purge
```

See the [global flags page](/flags/) for global options not listed here.

### SEE ALSO

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.

