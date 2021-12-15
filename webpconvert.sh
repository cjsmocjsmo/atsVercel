for f in /home/charliepi/atsVercel/src/lib/images/caroselimages/*.jpeg; do
cwebp -q 95 -resize 600 0 "$f" -o "${f%.jpg}_thumb.webp"
done

for f in /home/charliepi/atsVercel/src/lib/images/galPage1/*.jpeg; do
cwebp -q 95 "$f" -o "${f%.jpg}.webp"
done

for f in /home/charliepi/atsVercel/src/lib/images/galPage1/*.jpeg; do
cwebp -q 95 -resize 600 0 "$f" -o "${f%.jpg}_thumb.webp"
done

for f in /home/charliepi/atsVercel/src/lib/images/galPage2/*.jpeg; do
cwebp -q 95 "$f" -o "${f%.jpg}.webp"
done

for f in /home/charliepi/atsVercel/src/lib/images/galPage2/*.jpeg; do
cwebp -q 95 -resize 600 0 "$f" -o "${f%.jpg}_thumb.webp"
done
