#!/usr/bin/env python3

import os
import re
import glob
import string
from PIL import Image
import subprocess

class GenerateThumbsAndZooms:
    def __init__(self):
        self.carosel_glob_path = '/home/charliepi/atsVercel/src/lib/images/caroselimages/*.jpg'
        self.page1_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage1/*.jpg'
        self.page2_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage2/*.jpg'
        
        self.carosel_out_dir = '/home/charliepi/atsVercel/src/lib/images/caroselimages/'
        self.galPage1_out_dir = '/home/charliepi/atsVercel/src/lib/images/galPage1/'
        self.galPage2_out_dir = '/home/charliepi/atsVercel/src/lib/images/galPage2/'

    def get_new_outfile(self, apath):
        adir, fullfilename = os.path.split(apath)
        filename, ext = os.path.splitext(fullfilename)
        carosel_rotate_outfile = self.carosel_out_dir + filename + "_rotated" + ext
        carosel_full_webp = self.carosel_out_dir + filename + "_rotated.webp"

        galPage1_rotate_outfile = self.galPage1_out_dir + filename + "_rotated" + ext
        galPage1_full_webp_outfile = self.galPage1_out_dir + filename + "_rotated.webp"
        galPage1_thumb_webp_outfile = self.galPage1_out_dir + filename + "_rotated_thumb.webp"

        galPage2_rotate_outfile = self.galPage2_out_dir + filename + "_rotated" + ext
        galPage2_full_webp_outfile = self.galPage2_out_dir + filename + "_rotated.webp"
        galPage2_thumb_webp_outfile = self.galPage2_out_dir + filename + "_rotated_thumb.webp"

        return (carosel_rotate_outfile, carosel_full_webp, galPage1_rotate_outfile, galPage1_full_webp_outfile,
            galPage1_thumb_webp_outfile, galPage2_rotate_outfile, galPage2_full_webp_outfile, galPage2_thumb_webp_outfile)



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
        outfile = outf[5]
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
        self.create_webp()

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
        page1_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage1/*main.webp'
        p1glob = glob.glob(page1_glob_path)
        for p1 in p1glob:
            _, fname = os.path.split(p1)
            page_content = self.galPage1_page_string(fname)
            fname_noext, _ = os.path.splitext(fname)
            newfilename =  '/home/charliepi/atsVercel/src/routes/gallery/page1zoom/' + fname_noext + ".svelte"
            with open(newfilename, "w") as outfile:
                outfile.writelines([page_content[0], "\n", page_content[1], "\n", page_content[2]])

    def create_galPage2_pages(self):
        page2_glob_path = '/home/charliepi/atsVercel/src/lib/images/galPage2/*main.webp'
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

    def gallery_script_string(self):
        thumb_glob = self.galPage1_thumbs()
        stringList = ["<script>", "\n", ]
        count = 0
        for thumb in thumb_glob:
            




# import pic16thumb from '$lib/images/galPage2/20210114_111858_rotated_thumb.webp';

    def main(self):
        # self.create_webp_images()
        self.create_galPage1_pages()
        self.create_galPage2_pages()
        

if __name__ == "__main__":
    RF = GenerateThumbsAndZooms()
    RF.main()

