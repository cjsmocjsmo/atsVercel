for f in /home/charliepi/atsVercel/src/lib/images/page3/*_rotated.jpg; do
cwebp -q 95 -resize 600 0 "$f" -o "${f%.jpg}_thumb.webp"
done
