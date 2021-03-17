# Update Flatpak via systemd

1) Copy these to `/etc/systemd/system`. That seems wrong, but `systemd` doesn't
   seem to have a user location.
2) Run these commands:

```sh
$ sudo systemctl enable flatkpak-update.service
$ sudo systemctl enable flatkpak-update.timer
```

You can see what it's up to via:

```sh
$ sudo journalctl -u flatkpak-update
```
