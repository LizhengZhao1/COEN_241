qemu-system-x86_64 \
    -machine type=q35,accel=hvf \
    -smp 4 \
    -cpu host \
    -hda ubuntu.img \
    -m 4G \
    -vga virtio \
    -usb \
    -device usb-tablet \
    -display default,show-cursor=on -cdrom ./ubuntu-20.04.4-live-server-amd64.iso