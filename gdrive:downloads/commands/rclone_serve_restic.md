---
date: 2022-09-23T22:05:46+05:00
title: "rclone serve restic"
slug: rclone_serve_restic
url: /commands/rclone_serve_restic/
---
## rclone serve restic

Serve the remote for restic's REST API.

### Synopsis

rclone serve restic implements restic's REST backend API
over HTTP.  This allows restic to use rclone as a data storage
mechanism for cloud providers that restic does not support directly.

[Restic](https://restic.net/) is a command line program for doing
backups.

The server will log errors.  Use -v to see access logs.

--bwlimit will be respected for file transfers.  Use --stats to
control the stats printing.

### Setting up rclone for use by restic ###

First [set up a remote for your chosen cloud provider](/docs/#configure).

Once you have set up the remote, check it is working with, for example
"rclone lsd remote:".  You may have called the remote something other
than "remote:" - just substitute whatever you called it in the
following instructions.

Now start the rclone restic server

    rclone serve restic -v remote:backup

Where you can replace "backup" in the above by whatever path in the
remote you wish to use.

By default this will serve on "localhost:8080" you can change this
with use of the "--addr" flag.

You might wish to start this server on boot.

### Setting up restic to use rclone ###

Now you can [follow the restic
instructions](http://restic.readthedocs.io/en/latest/030_preparing_a_new_repo.html#rest-server)
on setting up restic.

Note that you will need restic 0.8.2 or later to interoperate with
rclone.

For the example above you will want to use "http://localhost:8080/" as
the URL for the REST server.

For example:

    $ export RESTIC_REPOSITORY=rest:http://localhost:8080/
    $ export RESTIC_PASSWORD=yourpassword
    $ restic init
    created restic backend 8b1a4b56ae at rest:http://localhost:8080/

    Please note that knowledge of your password is required to access
    the repository. Losing your password means that your data is
    irrecoverably lost.
    $ restic backup /path/to/files/to/backup
    scan [/path/to/files/to/backup]
    scanned 189 directories, 312 files in 0:00
    [0:00] 100.00%  38.128 MiB / 38.128 MiB  501 / 501 items  0 errors  ETA 0:00
    duration: 0:00
    snapshot 45c8fdd8 saved

#### Multiple repositories ####

Note that you can use the endpoint to host multiple repositories.  Do
this by adding a directory name or path after the URL.  Note that
these **must** end with /.  Eg

    $ export RESTIC_REPOSITORY=rest:http://localhost:8080/user1repo/
    # backup user1 stuff
    $ export RESTIC_REPOSITORY=rest:http://localhost:8080/user2repo/
    # backup user2 stuff

#### Private repositories ####

The "--private-repos" flag can be used to limit users to repositories starting
with a path of "/<username>/".

### Server options

Use --addr to specify which IP address and port the server should
listen on, eg --addr 1.2.3.4:8000 or --addr :8080 to listen to all
IPs.  By default it only listens on localhost.  You can use port
:0 to let the OS choose an available port.

If you set --addr to listen on a public or LAN accessible IP address
then using Authentication is advised - see the next section for info.

--server-read-timeout and --server-write-timeout can be used to
control the timeouts on the server.  Note that this is the total time
for a transfer.

--max-header-bytes controls the maximum number of bytes the server will
accept in the HTTP header.

--baseurl controls the URL prefix that rclone serves from.  By default
rclone will serve from the root.  If you used --baseurl "/rclone" then
rclone would serve from a URL starting with "/rclone/".  This is
useful if you wish to proxy rclone serve.  Rclone automatically
inserts leading and trailing "/" on --baseurl, so --baseurl "rclone",
--baseurl "/rclone" and --baseurl "/rclone/" are all treated
identically.

#### Authentication

By default this will serve files without needing a login.

You can either use an htpasswd file which can take lots of users, or
set a single username and password with the --user and --pass flags.

Use --htpasswd /path/to/htpasswd to provide an htpasswd file.  This is
in standard apache format and supports MD5, SHA1 and BCrypt for basic
authentication.  Bcrypt is recommended.

To create an htpasswd file:

    touch htpasswd
    htpasswd -B htpasswd user
    htpasswd -B htpasswd anotherUser

The password file can be updated while rclone is running.

Use --realm to set the authentication realm.

#### SSL/TLS

By default this will serve over http.  If you want you can serve over
https.  You will need to supply the --cert and --key flags.  If you
wish to do client side certificate validation then you will need to
supply --client-ca also.

--cert should be a either a PEM encoded certificate or a concatenation
of that with the CA certificate.  --key should be the PEM encoded
private key and --client-ca should be the PEM encoded client
certificate authority certificate.


```
rclone serve restic remote:path [flags]
```

### Options

```
      --addr string                     IPaddress:Port or :Port to bind server to. (default "localhost:8080")
      --append-only                     disallow deletion of repository data
      --baseurl string                  Prefix for URLs - leave blank for root.
      --cert string                     SSL PEM key (concatenation of certificate and CA certificate)
      --client-ca string                Client certificate authority to verify clients with
  -h, --help                            help for restic
      --htpasswd string                 htpasswd file - if not provided no authentication is done
      --key string                      SSL PEM Private key
      --max-header-bytes int            Maximum size of request header (default 4096)
      --pass string                     Password for authentication.
      --private-repos                   users can only access their private repo
      --realm string                    realm for authentication (default "rclone")
      --server-read-timeout duration    Timeout for server reading data (default 1h0m0s)
      --server-write-timeout duration   Timeout for server writing data (default 1h0m0s)
      --stdio                           run an HTTP2 server on stdin/stdout
      --user string                     User name for authentication.
```

See the [global flags page](/flags/) for global options not listed here.

### SEE ALSO

* [rclone serve](/commands/rclone_serve/)	 - Serve a remote over a protocol.

