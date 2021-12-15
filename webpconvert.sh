for f in /home/charliepi/atsVercel/src/lib/images/caroselimages/*_rotated.jpg; do
cwebp -q 95 -resize 600 0 "$f" -o "${f%.jpg}_thumb.webp"
done

for f in /home/charliepi/atsVercel/src/lib/images/galPage1/*.jpg; do
cwebp -q 95 "$f" -o "${f%.jpg}_main.webp"
done

for f in /home/charliepi/atsVercel/src/lib/images/galPage1/*.jpg; do
cwebp -q 95 -resize 600 0 "$f" -o "${f%.jpg}_thumb.webp"
done

for f in /home/charliepi/atsVercel/src/lib/images/galPage2/*_rotated.jpg; do
cwebp -q 95 "$f" -o "${f%.jpg}_main.webp"
done

for f in /home/charliepi/atsVercel/src/lib/images/galPage2/*_rotated.jpg; do
cwebp -q 95 -resize 600 0 "$f" -o "${f%.jpg}_thumb.webp"
done
