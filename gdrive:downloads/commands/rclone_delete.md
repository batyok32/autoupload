---
date: 2022-09-23T22:05:46+05:00
title: "rclone delete"
slug: rclone_delete
url: /commands/rclone_delete/
---
## rclone delete

Remove the contents of path.

### Synopsis


Remove the files in path.  Unlike `purge` it obeys include/exclude
filters so can be used to selectively delete files.

`rclone delete` only deletes objects but leaves the directory structure
alone. If you want to delete a directory and all of its contents use
`rclone purge`

Eg delete all files bigger than 100MBytes

Check what would be deleted first (use either)

    rclone --min-size 100M lsl remote:path
    rclone --dry-run --min-size 100M delete remote:path

Then delete

    rclone --min-size 100M delete remote:path

That reads "delete everything with a minimum size of 100 MB", hence
delete all files bigger than 100MBytes.


```
rclone delete remote:path [flags]
```

### Options

```
  -h, --help   help for delete
```

See the [global flags page](/flags/) for global options not listed here.

### SEE ALSO

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.

