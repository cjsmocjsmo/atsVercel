#!/usr/bin/env python3

import os
import re
import glob
import string
from PIL import Image
import subprocess

STYLESTRING = """
<style>
    .grid-container {
        display: grid;
        grid-gap: 10px;
        grid-template-columns: auto auto auto;
        justify-content: space-evenly;
        align-content: center;
    }

    img {
        width: 275px;
    }

    @media only screen and (max-width: 900px) {
        img {
            max-width: 200px;
        }
    }

    @media only screen and (max-width: 700px) {
        img {
            max-width: 175px;
        }
    }

    @media only screen and (max-width: 414px) {
        img {
            max-width: 125px;
        }
    }
</style>"""

class GenerateThumbsAndZooms:
    def __init__(self):
        self.carosel_glob_path = '/home/charliepi/atsVercel/src/lib/images/caroselimages/*.jpg'
        self.carosel_glob_path2 = '/home/charliepi/atsVercel/src/lib/images/caroselimages/*.webp'
        self.page1_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage1/*.jpg'
        self.page2_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage2/*.jpg'
        self.page2_glob_path2 = '/home/charliepi/atsVercel/src/lib/images/galPage2/*.webp'
        
        self.carosel_out_dir = '/home/charliepi/atsVercel/src/lib/images/caroselimages/'
        self.galPage1_out_dir = '/home/charliepi/atsVercel/src/lib/images/galPage1/'
        self.galPage2_out_dir = '/home/charliepi/atsVercel/src/lib/images/galPage2/'

        # self.search1 = re.compile(r"_rotated.webp")
        # self.search2 = re.compile(r"_rotated_thumb.webp")

    def get_new_outfile(self, apath):
        _, fullfilename = os.path.split(apath)
        filename, ext = os.path.splitext(fullfilename)
        carosel_rotate_outfile = self.carosel_out_dir + filename + ".jpeg"
        carosel_full_webp = self.carosel_out_dir + filename + ".webp"

        # galPage1_rotate_outfile = self.galPage1_out_dir + filename + "jpeg"
        # galPage1_full_webp_outfile = self.galPage1_out_dir + filename + "_rotated.webp"
        # galPage1_thumb_webp_outfile = self.galPage1_out_dir + filename + "_rotated_thumb.webp"

        galPage2_rotate_outfile = self.galPage2_out_dir + filename + ".jpeg"
        # galPage2_full_webp_outfile = self.galPage2_out_dir + filename + "_rotated.webp"
        # galPage2_thumb_webp_outfile = self.galPage2_out_dir + filename + "_rotated_thumb.webp"

        return (carosel_rotate_outfile, galPage2_rotate_outfile)
        
        # carosel_full_webp, galPage1_rotate_outfile, galPage1_full_webp_outfile,
        #     galPage1_thumb_webp_outfile,  galPage2_full_webp_outfile, galPage2_thumb_webp_outfile)



    def create_webp(self):
        print("Starting CWEBP")
        subprocess.run(["sh", "/home/charliepi/atsVercel/webpconvert.sh"])

    def rotate_pic_carosel(self, apath):
        outf = self.get_new_outfile(apath)
        outfile = outf[0]
        print(outfile)
        im = Image.open(apath)
        ir = im.rotate(270, expand=True)
        print("complete")
        ir.save(outfile)
        
    def rotate_pic_page2(self, apath):
        outf = self.get_new_outfile(apath)
        outfile = outf[1]
        print(outfile)
        im = Image.open(apath)
        ir = im.rotate(270, expand=True)
        print("complete")
        ir.save(outfile)

    def create_webp_images(self):
        caroselglob = glob.glob(self.carosel_glob_path)
        # page1glob = glob.glob(self.page1_glob_path)
        page2glob = glob.glob(self.page2_glob_path)

        for p1 in caroselglob:
            print("starting p1glob")
            self.rotate_pic_carosel(p1)

        for p2 in page2glob:
            print(p2)
            self.rotate_pic_page2(p2)

    # def remove_rotated(self):
    #     caroselglob = glob.glob(self.carosel_glob_path2)
    #     page2glob = glob.glob(self.page2_glob_path2)
    #     for car in caroselglob:
    #         if re.search(self.search1, car) != None:
    #             fn, ext = os.path.splitext(car)
    #             fn2 = fn[:-6] + ext
    #             print(fn2)
    #         elif re.search(self.search2) != None:
    #             fn = car[:-11] + "_thumb.webp"
    #             print(fn)




    def galPage1_page_string(self, filename):
        s1 = "<script> import p1 from '$lib/images/galPage1/{}'</script>".format(filename)
        s2 = """<img src={p1} alt='fuckti'/>"""
        s3 = """<style> img { border-radius: 10px; } </style>"""
        
        return s1, s2, s3

    def galPage2_page_string(self, filename):
        s1 = "<script> import p2 from '$lib/images/galPage2/{}'</script>".format(filename)
        s2 = """<img src={p2} alt='fuckti'/>"""
        s3 = """<style> img { border-radius: 10px; } </style>"""
        return s1, s2, s3

    def create_galPage1_pages(self):
        page1_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage1/*.webp'
        p1glob = glob.glob(page1_glob_path)
        for p1 in p1glob:
            _, fname = os.path.split(p1)
            page_content = self.galPage1_page_string(fname)
            fname_noext, _ = os.path.splitext(fname)
            newfilename =  '/home/charliepi/atsVercel/src/routes/gallery/page1zoom/' + fname_noext + ".svelte"
            with open(newfilename, "w") as outfile:
                outfile.writelines([page_content[0], "\n", page_content[1], "\n", page_content[2]])

    def create_galPage2_pages(self):
        page2_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage2/*.webp'
        p2glob = glob.glob(page2_glob_path)
        for p2 in p2glob:
            print(p2)
            _, fname = os.path.split(p2)
            page_content = self.galPage2_page_string(fname)
            fname_noext, _ = os.path.splitext(fname)
            newfilename =  '/home/charliepi/atsVercel/src/routes/gallery/page2zoom/' + fname_noext + ".svelte"
            with open(newfilename, "w") as outfile:
                outfile.writelines([page_content[0], "\n", page_content[1], "\n", page_content[2]])

    def galPage1_thumbs(self):
        page1_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage1/*thumb.webp'
        return glob.glob(page1_glob_path)

    def galPage2_thumbs(self):
        page2_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage2/*thumb.webp'
        return glob.glob(page2_glob_path)

    def gallery_script(self):
        thumb_glob2 = self.galPage2_thumbs()
        thumb_glob = self.galPage1_thumbs()
        pic1thumbList = []
        pic2thumbList = []
        stringList = ["<script>", "\n", ]
        count = 0
        for thumb1 in thumb_glob2:
            count += 1
            _, filename1 = os.path.split(thumb1)
            picthumb1 = "pic{}thumb".format(count)
            zoo1 = (picthumb1, filename1)
            pic1thumbList.append(zoo1)
            importstr = "import {} from '$lib/images/galPage2/{}';".format(picthumb1, filename1)
            stringList.append(importstr)
            stringList.append("\n")

        for thumb in thumb_glob:
            count += 1
            _, filename = os.path.split(thumb)
            picthumb = "pic{}thumb".format(count)
            zoo = (picthumb, filename)
            pic2thumbList.append(zoo)
            importstr = "import {} from '$lib/images/galPage1/{}';".format(picthumb, filename)
            stringList.append(importstr)
            stringList.append("\n")
        stringList.append("</script>")
        stringList.append("\n")
        stringList.append("<h1>360 516 8933</h1>")
        stringList.append("\n")
        stringList.append("<div class='grid-container'>")
        stringList.append("\n")

        for pic in pic2thumbList:
            p, _ = os.path.splitext(pic[1])
            g1 = "<div class='grid-item'><a href='"
            g2 = "/gallery/pic1zoom/" + p[:-6] + ".svelte"
            g3 = "'><img src={"
            g4 = pic[0]
            g5 = "} alt='fuckit' /></a></div>"
            gridItem = g1 + g2 + g3 + g4 + g5
            stringList.append(gridItem)
            stringList.append("\n")

        for pic in pic1thumbList:
            p, _ = os.path.splitext(pic[1])
            g1 = "<div class='grid-item'><a href='"
            print(p[:-6])
            g2 = "/gallery/pic1zoom/" + p[:-6] + ".svelte"
            g3 = "'><img src={"
            g4 = pic[0]
            g5 = "} alt='fuckit' /></a></div>"
            gridItem = g1 + g2 + g3 + g4 + g5
            stringList.append(gridItem)
            stringList.append("\n")
        
        stringList.append("</div>")
        stringList.append("\n")
        stringList.append("<h1>360 516 8933</h1>")
        stringList.append("\n")
        stringList.append(STYLESTRING)
        newoutfile = "/home/charliepi/atsVercel/src/routes/gallery.svelte"
        with open(newoutfile, "w") as ouf:
            ouf.writelines(stringList)

    def main(self):
        self.create_webp_images()
        self.create_webp()
        # self.create_galPage1_pages()
        # self.create_galPage2_pages()
        # self.gallery_script()

if __name__ == "__main__":
    RF = GenerateThumbsAndZooms()
    RF.main()

